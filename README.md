
# Student Information System - DevOps Mini Project

## Overview
This project demonstrates an end-to-end CI/CD pipeline using a Flask-based Student Information System. Jenkins automates dependency installation, testing, Docker image creation, deployment, and health verification.

## Technologies Used
- Python and Flask
- Pytest
- Git and GitHub
- Jenkins
- Docker

## Features
- Flask web application
- Automated unit testing
- Docker containerization
- Jenkins pipeline automation
- Application health-check endpoint

## Pipeline Stages
1. Checkout source code from GitHub.
2. Install Python dependencies.
3. Execute automated tests using Pytest.
4. Build the Docker image.
5. Deploy the application as a Docker container.
6. Verify deployment through the health endpoint.

## Run Locally
```bash
pip install -r requirements.txt
python app.py
```

## Run with Docker
```bash
docker build -t student-devops-app .
docker run -d --name student-app -p 5001:5001 student-devops-app
```

## Endpoints
- Homepage: http://localhost:5001
- Health check: http://localhost:5001/health

## Test Results
Both automated tests passed successfully in Jenkins.

## Outcome
Successfully implemented and verified an end-to-end CI/CD pipeline integrating GitHub, Jenkins, Python Flask, and Docker.
