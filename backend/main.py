import io
import cv2
import numpy as np
import torch
import torch.nn as nn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from PIL import Image

app = FastAPI(title="Multi-Scale Retinex AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Multi-Scale Retinex Inspired Advanced Neural Network
class MultiScaleRetinexNet(nn.Module):
    def __init__(self):
        super(MultiScaleRetinexNet, self).__init__()
        # Multi-scale feature extraction layers
        self.scale1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(inplace=True)
        )
        self.scale2 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=5, padding=2),
            nn.ReLU(inplace=True)
        )
        # Fusion and Illumination prediction
        self.fusion = nn.Sequential(
            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(32, 1, kernel_size=3, padding=1),
            nn.Sigmoid()
        )

    def forward(self, x):
        # Extract multi-scale features
        feat1 = self.scale1(x)
        feat2 = self.scale2(x)
        combined = torch.cat([feat1, feat2], dim=1)
        
        # Estimate illumination map
        illum_map = self.fusion(combined)
        illum_map = torch.clamp(illum_map, min=0.01)
        
        # Retinex decomposition: Reflection = Input / Illumination
        reflection = x / illum_map
        
        # Custom multi-scale gamma curve adjustment for natural lighting
        enhanced_illum = torch.pow(illum_map, 0.55)
        enhanced_img = reflection * enhanced_illum
        
        return torch.clamp(enhanced_img, 0.0, 1.0)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = MultiScaleRetinexNet().to(device)
model.eval()

@app.post("/api/enhance")
async def enhance_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    img_np = np.array(image).astype(np.float32) / 255.0
    input_tensor = torch.from_numpy(img_np).permute(2, 0, 1).unsqueeze(0).to(device)

    with torch.no_grad():
        output_tensor = model(input_tensor)

    output_np = output_tensor.squeeze(0).permute(1, 2, 0).cpu().numpy() * 255.0
    output_np = np.clip(output_np, 0, 255).astype(np.uint8)

    _, encoded_img = cv2.imencode(".jpg", cv2.cvtColor(output_np, cv2.COLOR_RGB2BGR))
    return Response(content=encoded_img.tobytes(), media_type="image/jpeg")