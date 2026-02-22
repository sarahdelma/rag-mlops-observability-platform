# RAG MLOps Observability Platform

A cloud-native, production-oriented Retrieval-Augmented Generation (RAG) system with full MLOps lifecycle management, containerized deployment, Kubernetes orchestration, and real-time AI observability using Prometheus and Grafana.

---

## Overview

This project demonstrates how modern LLM-powered systems can be built and deployed using enterprise-grade MLOps principles.

The system simulates a production-ready AI infrastructure stack suitable for enterprise and regulated environments.

---

##  Core Features

-  RAG-based Intelligent Product Query System  
-  Vector Search Integration  
-  LLM Inference Pipeline  
-  Dockerized Microservices Architecture  
-  Kubernetes Deployment  
-  Prometheus Metrics Collection  
-  Grafana AI Observability Dashboards  
-  Structured Logging & Exception Handling  
-  Secure Environment Variable Secret Handling  

---
---

##  System Architecture

User Query  
⬇  
FastAPI Backend  
⬇  
RAG Retrieval Pipeline  
⬇  
LLM Inference Engine  
⬇  
Response Generation  
⬇  
Prometheus Metrics  
⬇  
Grafana Dashboard Visualization  

---

##  Tech Stack

| Layer | Technology |
|--------|------------|
| Backend | Python, FastAPI |
| LLM Provider | Groq API |
| Embeddings | HuggingFace |
| Vector Database | AstraDB |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Containerization | Docker |
| Orchestration | Kubernetes |
| Logging | Custom Python Logger |

---
##  Observability & Monitoring

Prometheus collects:

- API request latency  
- Model inference duration  
- Error rates  
- Throughput metrics  
- System resource usage  

Grafana dashboards provide:

- Real-time LLM performance monitoring  
- Service health insights  
- AI pipeline latency visualization  
- Failure detection tracking  

This ensures production-level AI system transparency.

---

## Secure Secret Management

Sensitive credentials are handled via:

- `.env` (local development only)
- Environment variable injection
- GitHub Secrets (for CI/CD)
- Docker runtime configuration

No secrets are stored in version control.

---
##  Running the Project

### Run Locally

pip install -r requirements.txt
python app.py
docker build -t rag-mlops-observability-platform
docker run -p 8000:8000 rag-mlops-observability-platform
---
