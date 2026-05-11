# Hardened Kubernetes DevSecOps Showcase

A production-inspired Kubernetes DevSecOps portfolio project designed to demonstrate CKA/CKS-aligned practices, secure CI/CD workflows, and Day-2 operational readiness.

---

## 🎯 Project Vision

This repository showcases a production-oriented Kubernetes deployment focused on **security, reliability, automation, and operational readiness**.

The goal is to demonstrate real-world Kubernetes engineering practices beyond simple deployments, including:

* Kubernetes hardening
* Secure CI/CD automation
* Day-2 Operations
* Infrastructure isolation
* Immutable deployments
* DevSecOps best practices

Built following **CKA / CKS-inspired standards**.

---

## 🖥️ Infrastructure

Hybrid manually provisioned multi-node Kubernetes cluster:

| Component     | OS     | Role                     |
| ------------- | ------ | ------------------------ |
| Control Plane | CentOS | Kubernetes Control Plane |
| Worker Node   | Ubuntu | Application Workloads    |

Cluster provisioning: **kubeadm multi-node architecture**

---

## ⚙️ Technical Stack

* 🐍 **Application:** Flask (Python)
* ☸️ **Orchestration:** Kubernetes (kubeadm)
* 🐳 **Containerization:** Docker
* 🔄 **CI/CD:** GitHub Actions + Self-Hosted Runner
* 🔎 **Security Scanning:**

  * **Bandit** → Static Application Security Testing (SAST)
  * **Checkov** → Kubernetes IaC Security Scanning
  * **Trivy** → Container Vulnerability Scanning
* 🖥️ **Infrastructure:** Hybrid Linux (CentOS / Ubuntu)
* 🏷️ **Tagging Strategy:** Immutable image tagging using Git metadata

---

## 🛡️ Implemented Features

### 🔐 Security Hardening (CKS Aligned)

* Dedicated Kubernetes namespace isolation (`devsecops`)
* Network segmentation using **NetworkPolicy**
* Secrets externalized via **Kubernetes Secrets**
* Immutable filesystem:

```yaml
readOnlyRootFilesystem: true
```

Container runtime hardening:

```yaml
runAsNonRoot: true
runAsUser: 10001
allowPrivilegeEscalation: false
capabilities:
  drop:
    - ALL
```

---

### ⚡ Reliability & Performance (CKA Aligned)

* **Liveness & Readiness probes**
* **CPU / Memory requests & limits**
* Declarative Kubernetes manifests
* Immutable image deployment strategy
* Rolling deployments with rollout validation

---

## 🔄 CI/CD Pipeline

The project includes a production-inspired CI/CD workflow using **GitHub Actions** and a **self-hosted runner** connected to the Kubernetes cluster.

### Pipeline Stages

1. **SAST (Bandit)**
   Static analysis of Python code

2. **IaC Security Scan (Checkov)**
   Kubernetes manifest validation and security checks

3. **Container Build**
   Docker image build using immutable tags

4. **Container Security Scan (Trivy)**
   CVE detection for OS packages and Python libraries

5. **Automated Kubernetes Deployment**
   Deployment to a local kubeadm cluster through a self-hosted runner

6. **Deployment Validation**
   Rollout verification using:

```bash
kubectl rollout status
```

This architecture avoids exposing Kubernetes credentials to GitHub-hosted runners while preserving deployment automation.

---

## 🚀 Deployment Guide

```bash
# Clone repository
git clone https://github.com/oelmaamar/k8s-devsecops-project.git

# Deploy namespace
kubectl apply -f k8s/namespace.yaml

# Deploy application
kubectl apply -f k8s/
```

---

## 🗺️ Roadmap & Evolution

### ☁️ Cloud Migration

Move the platform to AWS infrastructure.

### 🏗️ Infrastructure as Code (Terraform)

Provision infrastructure declaratively.

### 🔐 RBAC Implementation

Fine-grained Kubernetes access control.

### 📦 Helm Packaging

Reusable Helm-based application packaging.

### 🔒 Advanced Security (CKS Level)

* Pod Security Standards
* Runtime security hardening
* Admission policies

### 📊 Observability Stack

Prometheus + Grafana + Kubernetes monitoring.

### 🚀 GitOps Evolution

ArgoCD-based Kubernetes delivery model.

