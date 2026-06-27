# 🚁 DroneSentinel Agent

> **AI-Powered Drone Surveillance & Threat Intelligence Platform**

DroneSentinel Agent is an end-to-end AI surveillance platform that combines **Computer Vision**, **Generative AI**, and **Cloud Computing** to analyze drone surveillance imagery, detect threats, store incidents, generate analytics, and provide an AI-powered investigation assistant.

The platform leverages **YOLOv8** for object detection, **Google Gemini Vision** for scene understanding, **FastAPI** for backend services, **PostgreSQL** for persistent storage, and **React + TypeScript** for an interactive dashboard. The application is fully containerized using **Docker** and deployed on **AWS EC2** and **Amazon S3 Static Website Hosting**.

---

# 🌐 Live Demo

| Service | URL |
|---------|-----|
| 🚀 Frontend | http://dronesentinel-agent-ajay.s3-website.ap-south-1.amazonaws.com |
| 📘 Backend API | http://13.234.78.158:8000/docs |
| 🔗 Backend Base URL | http://13.234.78.158:8000 |

---

# 📖 Table of Contents

- Overview
- Features
- Technology Stack
- System Architecture
- AI Workflow
- Project Structure
- Database Schema
- API Endpoints
- Installation
- Docker Deployment
- AWS Deployment
- Screenshots
- Future Enhancements
- Project Highlights
- Author

---

# 🚀 Overview

DroneSentinel Agent is a production-ready AI surveillance platform that enables users to upload drone surveillance images, automatically detect objects using **YOLOv8**, generate intelligent scene understanding using **Google Gemini Vision**, classify threats, store surveillance incidents, visualize historical analytics, and investigate incidents using an **LLM-powered AI Investigator**.

The project demonstrates an end-to-end AI pipeline from image ingestion to cloud deployment.

---

# ✨ Features

## 🤖 AI Drone Image Analysis

- Upload drone surveillance images
- YOLOv8 object detection
- AI-powered scene understanding
- Automatic threat assessment
- AI-generated surveillance summary
- Zone detection
- Threat classification
- Automatic incident logging

---

## 📊 Interactive Dashboard

- Total Incidents
- Active Alerts
- Threat Level
- AI Status
- Incident Timeline
- Zone Analytics
- Live Dashboard Statistics

---

## 🤖 AI Security Investigator

Ask natural language questions like:

- Show the latest incident
- How many incidents occurred?
- Any HIGH threat incidents?
- Show incidents in the Loading Dock
- What happened yesterday?
- Summarize surveillance history

Powered by **Google Gemini LLM**.

---

## 📈 Incident Analytics

- Historical Timeline
- Zone Distribution
- Threat Level Statistics
- Incident Summaries
- Alert History

---

## ☁ Cloud Deployment

- AWS EC2 Backend
- Amazon S3 Static Website Hosting
- Docker Compose
- PostgreSQL
- FastAPI REST APIs

---

# 🛠 Technology Stack

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Recharts
- React Dropzone

---

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

---

## Artificial Intelligence

- YOLOv8
- Google Gemini Vision
- Gemini LLM
- Prompt Engineering

---

## DevOps

- Docker
- Docker Compose
- AWS EC2
- Amazon S3
- Git
- GitHub

---

# 🏗 High-Level System Architecture

```mermaid
flowchart LR

    U[User]

    F[React Dashboard]

    API[FastAPI Backend]

    YOLO[YOLOv8 Detection]

    GEMINI[Gemini Vision]

    THREAT[Threat Assessment]

    DB[(PostgreSQL)]

    INVESTIGATOR[AI Investigator]

    LLM[Gemini LLM]

    U --> F

    F --> API

    API --> YOLO

    YOLO --> GEMINI

    GEMINI --> THREAT

    THREAT --> DB

    DB --> F

    DB --> INVESTIGATOR

    INVESTIGATOR --> LLM

    LLM --> F
```

---

# 🏛 Production Architecture

```mermaid
flowchart TB

subgraph User

Browser

end

subgraph Frontend

React

Dashboard

ImageUpload

AIInvestigator

Analytics

end

subgraph Backend

FastAPI

AnalyzeAPI

IncidentAPI

AnalyticsAPI

AlertAPI

InvestigatorAPI

end

subgraph AI

YOLOv8

GeminiVision

GeminiLLM

end

subgraph Database

PostgreSQL

Incidents

Alerts

end

Browser --> React

React --> AnalyzeAPI

React --> IncidentAPI

React --> AnalyticsAPI

React --> AlertAPI

React --> InvestigatorAPI

AnalyzeAPI --> YOLOv8

YOLOv8 --> GeminiVision

GeminiVision --> PostgreSQL

IncidentAPI --> PostgreSQL

AnalyticsAPI --> PostgreSQL

AlertAPI --> PostgreSQL

InvestigatorAPI --> GeminiLLM

GeminiLLM --> PostgreSQL

PostgreSQL --> React
```

---
# 🤖 AI Image Analysis Workflow

```mermaid
flowchart LR

A["Drone Image Upload"]
B["YOLOv8 Object Detection"]
C["Detected Objects"]
D["Gemini Vision Analysis"]
E["Threat Assessment"]
F["Store Incident"]
G["Dashboard Analytics"]

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
```

---

# 🧠 AI Investigator Workflow

```mermaid
sequenceDiagram

actor User

participant Frontend

participant Backend

participant PostgreSQL

participant Gemini

User->>Frontend: Ask Question

Frontend->>Backend: POST /investigator

Backend->>PostgreSQL: Retrieve Incident History

PostgreSQL-->>Backend: Historical Incidents

Backend->>Gemini: Build Prompt

Gemini-->>Backend: AI Response

Backend-->>Frontend: Natural Language Answer
```

---

# 🔄 Complete Processing Pipeline

```mermaid
flowchart TD

A["Upload Image"]

B["FastAPI"]

C["YOLOv8 Detection"]

D["Gemini Vision"]

E["Threat Classification"]

F["Save to PostgreSQL"]

G["Update Dashboard"]

H["AI Investigator"]

A --> B

B --> C

C --> D

D --> E

E --> F

F --> G

F --> H
```

---

# 📂 Project Structure

```text
DroneSentinel-Agent
│
├── backend
│   │
│   ├── app
│   │   │
│   │   ├── agents
│   │   │   ├── workflow.py
│   │   │   ├── nodes.py
│   │   │   └── investigator.py
│   │   │
│   │   ├── api
│   │   │   ├── analyze.py
│   │   │   ├── analytics.py
│   │   │   ├── alerts.py
│   │   │   ├── incidents.py
│   │   │   ├── investigator.py
│   │   │   └── search.py
│   │   │
│   │   ├── services
│   │   │   ├── vision_service.py
│   │   │   └── yolo_service.py
│   │   │
│   │   ├── vectorstore
│   │   │
│   │   ├── database.py
│   │   ├── models.py
│   │   └── main.py
│   │
│   └── Dockerfile
│
├── frontend
│   │
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── layouts
│   │   ├── hooks
│   │   ├── services
│   │   └── types
│   │
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🗄 Database Schema

## incidents

| Column | Type | Description |
|---------|------|-------------|
| id | Integer | Primary Key |
| image_name | String | Uploaded image |
| timestamp | String | Detection timestamp |
| event | Text | AI generated alert |
| detected_objects | Text | Objects detected |
| threat_level | String | LOW / MEDIUM / HIGH |
| zone | String | Detection zone |

---

## alerts

| Column | Type | Description |
|---------|------|-------------|
| id | Integer | Primary Key |
| severity | String | Alert severity |
| message | Text | Alert message |

---

# 🔌 REST API Endpoints

## Image Analysis

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/analyze` | Analyze uploaded drone image |

---

## Dashboard

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/analytics/` | Zone analytics |
| GET | `/analytics/stats` | Dashboard statistics |

---

## Incidents

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/incidents/` | Retrieve all incidents |

---

## Alerts

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/alerts/` | Retrieve all alerts |

---

## AI Investigator

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/investigator/` | Natural language investigation |

---

## Search

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/search/` | Search historical incidents |

---

# 📊 Dashboard Components

The frontend dashboard consists of:

- 📈 Stats Cards
- 📡 Drone Image Upload
- 🤖 AI Analysis Results
- 🚨 Alert Feed
- 📅 Incident Timeline
- 📊 Zone Analytics
- 🧠 AI Investigator

All dashboard components fetch live data from the FastAPI backend using REST APIs and update automatically after image analysis.
# 🚀 Installation

## Prerequisites

Before running the project, ensure the following software is installed:

- Python 3.12+
- Node.js 20+
- Docker
- Docker Compose
- Git
- PostgreSQL (optional if using Docker)

---

# 📥 Clone Repository

```bash
git clone https://github.com/ajaysathriai-afk/Drone-Sentinel-Agent.git

cd Drone-Sentinel-Agent
```

---

# ⚙ Backend Setup

Navigate to the backend.

```bash
cd backend
```

Create virtual environment.

```bash
python -m venv venv
```

Activate virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run backend.

```bash
uvicorn app.main:app --reload
```

Backend runs on

```
http://localhost:8000
```

Swagger API

```
http://localhost:8000/docs
```

---

# 💻 Frontend Setup

Navigate to frontend.

```bash
cd frontend
```

Install packages.

```bash
npm install
```

Run development server.

```bash
npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# 🐳 Docker Deployment

Build containers.

```bash
docker compose build
```

Run services.

```bash
docker compose up -d
```

Stop services.

```bash
docker compose down
```

View logs.

```bash
docker compose logs -f
```

---

# ☁ AWS Deployment

## Backend

The FastAPI backend is deployed on

- AWS EC2
- Docker
- PostgreSQL Container

Expose port

```
8000
```

Backend API

```
http://13.234.78.158:8000
```

Swagger

```
http://13.234.78.158:8000/docs
```

---

## Frontend

The React frontend is hosted using

- Amazon S3 Static Website Hosting

Frontend URL

```
http://dronesentinel-agent-ajay.s3-website.ap-south-1.amazonaws.com
```

---

# 🔐 Environment Variables

Create

```
backend/.env
```

Example

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

DATABASE_URL=postgresql://postgres:postgres@postgres:5432/dronesentinel_db
```

---

# 📸 Screenshots

## Dashboard

> Add dashboard screenshot here

---

## Drone Image Upload

> Add upload screen screenshot here

---

## AI Analysis Result

> Add AI analysis screenshot here

---

## Incident Timeline

> Add timeline screenshot here

---

## Zone Analytics

> Add analytics screenshot here

---

## AI Investigator

> Add AI Investigator screenshot here

---

# 🔍 Example Workflow

1. Upload drone surveillance image.

2. YOLOv8 detects objects.

3. Gemini Vision analyzes scene.

4. Threat Assessment Engine determines risk.

5. Incident is stored inside PostgreSQL.

6. Dashboard automatically updates.

7. AI Investigator can answer questions using historical incidents.

---

# 📡 Sample API Usage

## Analyze Image

```bash
curl -X POST \
-F "file=@drone_image.jpg" \
http://13.234.78.158:8000/analyze
```

---

## Get Dashboard Statistics

```bash
curl http://13.234.78.158:8000/analytics/stats
```

---

## Get Incidents

```bash
curl http://13.234.78.158:8000/incidents/
```

---

## Get Alerts

```bash
curl http://13.234.78.158:8000/alerts/
```

---

## Ask AI Investigator

```json
POST /investigator

{
  "question":"Summarize all HIGH threat incidents."
}
```

---

# 📈 Current Capabilities

✅ Drone Image Upload

✅ YOLOv8 Object Detection

✅ Gemini Vision Analysis

✅ Threat Classification

✅ Automatic Incident Logging

✅ Dashboard Analytics

✅ AI Investigator

✅ Docker Deployment

✅ PostgreSQL Storage

✅ AWS EC2 Deployment

✅ Amazon S3 Frontend

---

# ⚡ Performance

- FastAPI asynchronous backend
- Dockerized deployment
- PostgreSQL persistent storage
- Lightweight React frontend
- REST API architecture
- Cloud-ready deployment

---
# 🔮 Future Enhancements

The current version focuses on image-based AI surveillance. Future releases will expand the platform into a production-grade intelligent monitoring system.

## Computer Vision

- 🎥 Live RTSP Drone Video Streaming
- 📹 Multi-Camera Monitoring
- 😀 Face Recognition
- 🚗 License Plate Recognition (ANPR)
- 🚶 Human Activity Recognition
- 🛰 Object Tracking Across Frames
- 🔥 Fire & Smoke Detection
- 🌊 Flood Detection
- 🛑 Intrusion Detection
- 🚨 Suspicious Activity Detection

---

## Artificial Intelligence

- Multi-Agent AI using LangGraph
- Retrieval-Augmented Generation (RAG)
- Long-Term Incident Memory
- Semantic Search
- Automatic Incident Summarization
- AI Risk Prediction
- Intelligent Patrol Recommendations

---

## Dashboard

- Real-Time Live Feed
- Heat Maps
- Interactive Map View
- Geofencing
- Custom Alert Rules
- Incident Export
- PDF Reports
- CSV Export
- Advanced Filters

---

## Cloud

- AWS ECS
- Kubernetes
- CloudFront CDN
- Amazon ECR
- CI/CD using GitHub Actions
- Monitoring with Prometheus & Grafana

---

## Security

- JWT Authentication
- OAuth Login
- Role-Based Access Control (RBAC)
- Audit Logs
- API Rate Limiting

---

# 💼 Resume Highlights

This project demonstrates practical experience with:

- End-to-End Full Stack Development
- Computer Vision
- Generative AI
- Large Language Models (LLMs)
- Prompt Engineering
- REST API Development
- PostgreSQL Database Design
- Docker Containerization
- Cloud Deployment on AWS
- Production Debugging
- AI Application Development

---

# 🏆 Project Highlights

- End-to-End AI Surveillance Platform
- YOLOv8 Computer Vision
- Google Gemini Vision Integration
- AI Threat Assessment Engine
- Natural Language AI Investigator
- Interactive React Dashboard
- PostgreSQL Analytics
- FastAPI REST Backend
- Dockerized Deployment
- AWS EC2 Backend
- Amazon S3 Static Website
- Production-Ready Architecture

---

# 📚 Learning Outcomes

During this project, the following concepts were implemented:

- FastAPI Backend Development
- REST API Design
- React Component Architecture
- TypeScript Development
- SQLAlchemy ORM
- PostgreSQL Integration
- Docker & Docker Compose
- AWS EC2 Deployment
- Amazon S3 Static Website Hosting
- CORS Configuration
- Computer Vision using YOLOv8
- Google Gemini Vision API
- LLM-powered AI Applications
- Prompt Engineering
- Cloud Deployment & Debugging

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve DroneSentinel Agent:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 🐞 Known Limitations

Current version supports:

- Image-based surveillance only
- Single image inference
- Rule-based threat assessment
- Manual image uploads

Future releases will support:

- Live video streams
- Multi-camera monitoring
- Advanced AI agents
- Automated notifications
- Real-time event processing

---

# 📄 License

This project is released under the **MIT License**.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.

---

# 👨‍💻 Author

## Ajay Kumar Sathri

**MS in Computer Science**

University of North Texas

### Areas of Interest

- Artificial Intelligence
- Generative AI
- Agentic AI
- Computer Vision
- Large Language Models
- Full Stack Development
- Cloud Computing
- MLOps

---

## Connect

GitHub

https://github.com/ajaysathriai-afk

LinkedIn

> Add your LinkedIn profile URL here

Portfolio

> Add your portfolio website here

---

# 🙏 Acknowledgements

This project was built using the following technologies and communities:

- FastAPI
- React
- TypeScript
- YOLOv8
- Google Gemini
- PostgreSQL
- Docker
- AWS
- SQLAlchemy
- Tailwind CSS
- Recharts

Special thanks to the open-source community for providing the tools and frameworks that made this project possible.

---

# 🚀 Final Thoughts

DroneSentinel Agent demonstrates the integration of modern AI technologies with full-stack software engineering and cloud deployment practices. The project showcases how Computer Vision, Large Language Models, and scalable backend systems can be combined to build an intelligent surveillance platform capable of analyzing aerial imagery, tracking incidents, and assisting security personnel through natural language interaction.

This project serves as a practical demonstration of production-ready AI application development, covering the complete lifecycle from model inference and backend APIs to cloud deployment and interactive dashboards.

---

<div align="center">

### ⭐ If you like this project, please consider giving it a star!

Made with ❤️ using FastAPI, React, YOLOv8, Google Gemini, PostgreSQL, Docker, and AWS.

</div>