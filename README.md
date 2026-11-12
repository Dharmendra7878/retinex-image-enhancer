🌓 Multi-Scale Retinex Image Enhancer

A full-stack AI-powered web application that restores and enhances underexposed, low-light images   using Retinex theory and deep learning. Built with **FastAPI**, **PyTorch**, and **Next.js**.

---

## 📖 Academic Reference & Inspiration
This project is a practical learning implementation inspired by the research publication:
> **"Low-Light Image Enhancement Method Based on Retinex Theory by Improving Illumination Map"**  
> *Authors:* Dr. Changli Li et al.  
> *Journal:* Applied Sciences (MDPI), 2022, 12(10), 5257  
> *Link:* [MDPI Publication](https://www.mdpi.com/2076-3417/12/10/5257)

*Note: This project translates core theoretical concepts—specifically separating reflectance $R(x,y)$ and illumination $I(x,y)$ components—into an accessible, cloud-deployed web studio.*

---

## 🏗️ System Architecture

The application follows a decoupled client-server architecture:

| Component | Tech Stack | Hosting | Purpose |
| :--- | :--- | :--- | :--- |
| **Frontend** | Next.js, React, Tailwind CSS, TypeScript | Vercel | Drag-and-drop studio UI with side-by-side image comparison. |
| **Backend** | FastAPI, PyTorch, NumPy, Python | Render | REST API (`/api/enhance`) for multi-scale illumination estimation & gamma correction. |

---

## ✨ Key Features
- **Retinex-Based Processing:** Separates illumination from reflectance to brighten deep shadows without overexposing highlights.
- **Interactive Web Studio:** Clean, distraction-free UI for uploading dark photos and previewing real-time enhancements.
- **Cloud-Ready Deployment:** Configured for seamless CI/CD deployment across Vercel and Render.

---

## 📂 Project Structure

```text
retinex-image-enhancer/
├── backend/                  # FastAPI & PyTorch inference engine
│   ├── main.py               # API routes and Retinex processing logic
│   └── requirements.txt      # Python dependencies
├── frontend/                 # Next.js web application
│   ├── src/                  # React components & pages
│   ├── public/               # Static assets
│   └── package.json          # Node.js dependencies
└── README.md                 # Project documentation
```

---

## 🚀 Local Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Dharmendra7878/retinex-image-enhancer.git
cd retinex-image-enhancer
```

### 2. Backend Setup (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
The API will run at `http://localhost:8000`.

### 3. Frontend Setup (Next.js)
```bash
cd frontend
npm install
npm run dev
```


## 🔌 API Reference

### Enhance Image
- **Endpoint:** `POST /api/enhance`
- **Content-Type:** `multipart/form-data`
- **Payload:** `file` (Image file: `.jpg`, `.png`, `.webp`)
- **Response:** Enhanced JPEG image byte stream.

---

## 👨‍💻 Author & Acknowledgments
- **Developer:** Dharmendra Paroda ([GitHub](https://github.com/Dharmendra7878))
- **Special Thanks:** Dr. Changli Li and the open-access research community for foundational work in low-light computer vision.
