# DevSecOps Kubernetes Project

## 🚧 Work in progress
This project implements a DevSecOps pipeline with Kubernetes, CI and security scanning. Additional features are being added.

## Description
Flask application containerized with Docker and deployed on Kubernetes.

## Stack
- Docker
- Kubernetes (kubeadm)
- GitHub Actions
- Trivy

## Features
- Flask API
- Dockerized application
- Kubernetes Deployment & Service
- ConfigMap & Secret
- NetworkPolicy
- CI pipeline with security scan

## Run locally
docker build -t devsecops-app .
docker run -p 5000:5000 devsecops-app

## Kubernetes
kubectl apply -f k8s/

## CI
- Build Docker image
- Scan with Trivy
- Push to Docker Hub
