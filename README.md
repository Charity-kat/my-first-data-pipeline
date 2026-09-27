# DevSecOps Data Pipeline

![CI/CD Pipeline](https://github.com/Charity-kat/my-first-data-pipeline/actions/workflows/devsecops-pipeline.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)
![Docker](https://img.shields.io/badge/docker-enabled-blue.svg)
![Security](https://img.shields.io/badge/security-bandit-green.svg)

An automated, end-to-end DevSecOps cryptocurrency data ingestion and transformation pipeline built with Python, Docker, and GitHub Actions.

## 📌 Architecture Overview

Pipeline Runner [pipeline.py]
  │
  ├─► Price Extraction [extract.py]    ──► CoinGecko REST API ──► Raw CSV
  ├─► Price Transformation [transform.py] ──► Reads Raw CSV    ──► Clean CSV
  └─► Database Loading [load.py]       ──► Reads Clean CSV  ──► SQLite DB (crypto_pipeline.db)

## 🔐 DevSecOps CI/CD Workflow

The pipeline is fully automated using GitHub Actions (.github/workflows/devsecops-pipeline.yml). On every code push:

1. Environment Setup: Configures Python 3.11 environment.
2. Dependency Management: Installs required packages cleanly via requirements.txt.
3. Unit Testing: Executes unit tests with pytest.
4. Security Audit: Conducts static code analysis using Bandit to catch security risks before containerization.
5. Containerization: Builds a lightweight Docker image (crypto-pipeline:latest).
6. Execution: Runs the containerized pipeline end-to-end in an isolated container environment.

## 🛠️ Tech Stack

- Language: Python 3.11
- Data Processing: Pandas, NumPy, SQLite3
- API Integration: Requests (CoinGecko API)
- Testing & Quality: Pytest
- Security Scanning: Bandit
- Containerization: Docker
- CI/CD Automation: GitHub Actions

## 🚀 How to Run Locally

### Prerequisites
- Python 3.11+
- Docker Desktop (Optional)

### Setup & Execution
git clone https://github.com/Charity-kat/my-first-data-pipeline.git
cd my-first-data-pipeline

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt
python pipeline.py

pytest
bandit -r . -ll -s B101 -x ./venv

### Docker Execution
docker build -t crypto-pipeline:latest .
docker run --rm crypto-pipeline:latest
