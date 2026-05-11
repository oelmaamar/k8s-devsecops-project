# Hardened Kubernetes DevSecOps Showcase

A production-inspired Kubernetes DevSecOps portfolio project designed to demonstrate Kubernetes administration, secure CI/CD workflows, and Day-2 operational readiness.

---

## 🎯 Project Vision

This repository showcases a production-oriented Kubernetes DevSecOps platform designed to demonstrate **real-world infrastructure practices**.

The long-term objective is to build a complete, enterprise-inspired platform covering:

* **Kubernetes administration (CKA)**
* **Secure CI/CD automation**
* **Infrastructure as Code with Terraform**
* **Cloud-native deployment on AWS**
* **Day-2 Operations and observability**
* **Advanced Kubernetes security hardening (CKS roadmap)**
* **Scalable and secure application delivery**

The platform is being built progressively to reflect a realistic infrastructure evolution:

**Local Kubernetes → Secure CI/CD → Infrastructure as Code → Cloud Migration → Advanced DevSecOps practices**

The current implementation focuses on building a strong Kubernetes and CI/CD foundation before expanding into Terraform, AWS, and advanced CKS-level security.

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
  * **Checkov** → Kubernetes manifest security scanning
  * **Trivy** → Container vulnerability scanning
* 🖥️ **Infrastructure:** Hybrid Linux (CentOS / Ubuntu)
* 🏷️ **Image Strategy:** Immutable tagging using Git metadata

---

## 🛡️ Implemented Features

### 🔐 Kubernetes Security Foundations

Implemented baseline Kubernetes security controls that prepare the project for future CKS-level hardening:

* Dedicated namespace isolation (`devsecops`)
* Kubernetes Secrets used to externalize sensitive configuration
* Baseline NetworkPolicy restricting ingress traffic to the Flask API on port `5000`
* Hardened container runtime configuration:

  * `runAsNonRoot: true`
  * `runAsUser: 10001`
  * `allowPrivilegeEscalation: false`
  * Linux capabilities dropped

---

### ⚡ Reliability & Operations

* Liveness and readiness probes
* CPU and memory requests/limits
* Declarative Kubernetes manifests
* Rolling deployments with rollout validation
* Multi-replica deployment on Kubernetes worker node

---

## 🔄 CI/CD Pipeline

The project includes a production-inspired **GitHub Actions CI/CD workflow** using a **self-hosted runner** connected to the local Kubernetes cluster.

### Pipeline Stages

1. **SAST — Bandit**
   Static analysis of Python source code.

2. **Kubernetes Manifest Security Scan — Checkov**
   Security validation of Kubernetes YAML manifests.

3. **Container Build**
   Docker image build with immutable tagging.

4. **Container Vulnerability Scan — Trivy**
   CVE detection for OS packages and Python libraries.

5. **Automated Kubernetes Deployment**
   Deployment to the local kubeadm cluster through a self-hosted runner.

6. **Deployment Validation**
   Rollout verification using:

```bash
kubectl rollout status deployment/flask-api -n devsecops
```

This architecture avoids exposing Kubernetes credentials to GitHub-hosted runners while preserving automated deployment workflows.

---

## 🚀 Deployment Workflow

This project uses a **GitHub Actions CI/CD pipeline** for automated delivery.

### Trigger Deployment

```bash
git add .
git commit -m "update application"
git push origin main
```

### Verify Deployment

```bash
kubectl get pods -n devsecops
kubectl get deployment -n devsecops
kubectl rollout status deployment/flask-api -n devsecops
```

---

## 🗺️ Roadmap & Evolution

### 🔐 RBAC Implementation

Introduce fine-grained Kubernetes access control using ServiceAccounts, Roles, and RoleBindings.

### 🌐 NetworkPolicy Hardening

Move from basic ingress restriction to stricter pod-to-pod communication rules.

### 📈 Horizontal Pod Autoscaling

Add HPA to dynamically scale workloads based on resource consumption.

### 📊 Observability Stack

Add metrics and monitoring with Prometheus and Grafana.

### ☁️ Cloud Migration — AWS

Move the platform from local kubeadm infrastructure to AWS-based Kubernetes infrastructure.

### 🏗️ Infrastructure as Code — Terraform

Provision infrastructure declaratively using Terraform.

### 📦 Helm Packaging

Package the Kubernetes application using reusable Helm charts.

### 🔒 Advanced CKS Hardening

Future CKS-oriented improvements:

* Pod Security Standards
* Admission policies
* Runtime security improvements
* Stronger NetworkPolicies
* Least-privilege RBAC
* Image policy enforcement

### 🚀 GitOps Evolution

Introduce ArgoCD-based Kubernetes delivery after the CI/CD foundation is stable.

