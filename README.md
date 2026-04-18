# 🔐 Hardened Kubernetes DevSecOps Showcase

> 🚧 **Project Status:** Active Development — Phase 1: Core Kubernetes Hardening

---

## 🎯 Project Vision
This repository is a **production-oriented Kubernetes showcase** focused on **Day 2 Operations**:
- Security hardening
- Resource optimization
- Network isolation  

Built following **CKA / CKS industry standards**.

🖥️ Infrastructure: manually provisioned **hybrid multi-node cluster**
- Control Plane: CentOS  
- Worker Node: Ubuntu  

---

## ⚙️ Technical Stack
- 🐍 **App Framework:** Flask (Python)  
- ☸️ **Orchestration:** Kubernetes (kubeadm multi-node)  
- 🖥️ **Infrastructure:** Hybrid Linux (CentOS / Ubuntu)  
- 🔎 **Security:** Trivy + Kubernetes native security features  
- 🏷️ **Tagging Policy:** Immutable Semantic Versioning (`v1.0.x`)  

---

## 🛡️ Implemented Features (Core K8s)

### 🔐 Security & Hardening (CKS Aligned)
- 🚧 **Network Segmentation:** NetworkPolicy enforcing zero-trust (port 5000 only)  
- 🔑 **Secrets Management:** Sensitive data externalized via Kubernetes Secrets  
- 📦 **Immutable Filesystem:** `readOnlyRootFilesystem: true`  
- 👤 **Runtime Hardening:**  
  - `runAsNonRoot: true` (UID 10001)  
  - All Linux capabilities dropped  
- 🧱 **Isolation:** Dedicated `devsecops` namespace  

---

### ⚡ Reliability & Performance (CKA Aligned)
- 🔁 **Self-Healing:** Liveness & Readiness probes configured  
- 📊 **Resource Management:** CPU/Memory requests & limits enforced  
- 🚀 **Deployment Strategy:** Declarative manifests + immutable image tagging  

---

## 🚀 Deployment Guide

```bash
# Clone the repository
git clone https://github.com/oelmaamar/k8s-devsecops-project.git

# Deploy all resources
kubectl apply -f k8s/
```

---

## 🗺️ Roadmap & Evolution

- ⚙️ **CI/CD Pipeline**  
  Implement automated pipelines with image tagging based on Git SHA

- 🔐 **RBAC Implementation**  
  Define fine-grained access control for secure cluster operations

- 🌐 **Ingress Controller Setup**  
  Expose services externally with proper routing and TLS

- ☁️ **Infrastructure as Code (Terraform)**  
  Automate infrastructure provisioning and Kubernetes setup

- 📦 **Helm Packaging**  
  Package and manage Kubernetes applications with Helm charts

- 🔒 **Advanced Security (CKS Level)**  
  Implement deeper security practices (Pod Security, runtime security, policies)

---

