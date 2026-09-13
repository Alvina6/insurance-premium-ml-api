# Insurance Premium Predictor

A machine learning application that predicts an insurance premium category based on user information. The project uses a **FastAPI backend**, **Streamlit frontend**, and **Docker** for containerization.

## Project Architecture

```text
User
  ↓
Streamlit Frontend
  ↓ HTTP Request
FastAPI Backend
  ↓
Machine Learning Model
  ↓
Predicted Premium Category
```

## Project Structure

```text
insurance-premium-predictor/
│
├── Backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── model/
│   └── schema/
│
├── Frontend/
│   ├── Dockerfile
│   └── frontend.py
│
├── requirements.txt
├── docker-compose.yml
├── .dockerignore
└── README.md
```

## Tech Stack

* Python
* FastAPI
* Streamlit
* Scikit-learn
* Pandas
* Pydantic
* Docker
* Docker Compose

## Features

* Insurance premium category prediction
* FastAPI REST API
* Streamlit user interface
* Machine learning model integration
* Confidence score and class probabilities
* Dockerized frontend and backend
* Separate Docker images for frontend and backend

## Docker Hub Images

### Backend

```text
alvinarahim/insurance-premium-backend:latest
```

### Frontend

```text
alvinarahim/insurance-premium-frontend:latest
```

## Run Locally with Docker Compose

Clone the repository and move into the project directory:

```bash
git clone https://github.com/Alvina6/insurance-premium-ml-api.git
cd insurance-premium-predictor
```

Build and start the containers:

```bash
docker compose up --build
```

The Streamlit frontend will be available at:

```text
http://localhost:8501
```

The FastAPI backend will be available at:

```text
http://localhost:8000
```

## FastAPI Endpoints

### Home

```text
GET /
```

### Health Check

```text
GET /health
```

### Prediction

```text
POST /predict
```

Example request:

```json
{
  "bmi": 22.0,
  "age_group": "Young",
  "lifestyle_risk": "Low",
  "city_tier": "Tier 1",
  "income_lpa": 5.0,
  "occupation": "Software Engineer"
}
```

## Run Published Docker Hub Images

Create a Docker network:

```bash
docker network create insurance-network
```

Run the backend:

```bash
docker run -d --name backend -p 8000:8000 --network insurance-network alvinarahim/insurance-premium-backend:latest
```

Run the frontend:

```bash
docker run -d --name frontend -p 8501:8501 --network insurance-network alvinarahim/insurance-premium-frontend:latest
```

Open the application:

```text
http://localhost:8501
```

The frontend communicates with the backend through:

```text
http://backend:8000/predict
```

## Docker Workflow

```text
Source Code
     ↓
Docker Build
     ↓
Backend Image + Frontend Image
     ↓
Docker Hub
     ↓
Docker Pull
     ↓
Docker Containers
     ↓
Frontend ↔ Backend
```

## Learning Outcome

This project helped strengthen practical understanding of:

* Machine learning model deployment
* REST API development with FastAPI
* Frontend and backend communication
* Docker image creation
* Docker containers and networking
* Docker Compose
* Publishing images to Docker Hub

## Author

**Alvina Rahim**
