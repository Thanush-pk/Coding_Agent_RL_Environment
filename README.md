# 🤖 Coding Agent RL Environment

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/FastAPI-0.141.1-009688.svg)](https://fastapi.tiangolo.com/)
[![Testing](https://img.shields.io/badge/pytest-9.1.1-yellow.svg)](https://docs.pytest.org/)
[![Dockerized](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

A robust, reproducible Reinforcement Learning (RL) and LLM Coding Agent Evaluation Environment designed for benchmarking automated code-repair and feature-implementation agents on e-commerce API systems.

---

## 📌 Overview

This repository provides a standardized environment (`OrderFlow API`) for training and evaluating autonomous coding agents. The task evaluates an agent's ability to model complex business logic, handle discount eligibility, compute tax & shipping rules, and pass both public unit tests and hidden evaluation suites.

---

## ✨ Key Features

- **⚡ FastAPI Architecture**: High-performance asynchronous API endpoints built with Pydantic validation schemas.
- **🏗️ Modular Service Layer**: Decoupled domain services (`order_service`, `discount_service`, `tax_service`).
- **💯 Automated Evaluation Grader**: Built-in test grader (`grader/grader.py`) that executes both public and hidden test suites to yield a deterministic score (0 or 100).
- **🐳 Containerized Sandbox**: Full Docker support for safe, isolated execution environments.

---

## 📁 Repository Structure

```
coding-agent-rl-environment/
├── app/
│   ├── models/
│   │   └── order.py              # Pydantic schemas (Order, OrderItem)
│   ├── services/
│   │   ├── discount_service.py   # Discount calculation logic & eligibility filtering
│   │   ├── order_service.py      # Master order total orchestration
│   │   └── tax_service.py        # Tax calculation logic
│   └── main.py                   # FastAPI app entry point & routes
├── task/
│   └── task.md                   # Agent task specification & requirements
├── tests/
│   └── test_orders.py            # Public test suite for local verification
├── grader/
│   ├── hidden_tests/             # Holdout test suite for evaluation
│   └── grader.py                 # Automated grading script
├── .dockerignore                 # Docker build ignore configurations
├── .gitignore                    # Version control ignore configurations
├── Dockerfile                    # Container configuration
├── pytest.ini                    # Pytest settings
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.11+
- Git

### 2. Setup Virtual Environment

```bash
# Clone the repository
git clone https://github.com/Thanush-pk/Coding_Agent_RL_Environment.git
cd Coding_Agent_RL_Environment

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows (CMD / PowerShell):
.venv\Scripts\activate
# On Linux / macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Running Tests & Evaluation

### Public Test Suite
Run local unit tests using `pytest`:

```bash
pytest
```

### Automated Grader (Public + Hidden Tests)
To evaluate agent performance across all public and hidden benchmark tests, run:

```bash
python grader/grader.py
```

Expected output upon successful completion:
```text
Running grader...
.
----------------------------------------------------------------------
Ran hidden & public test suites successfully.
Score: 100/100
```

---

## 🌐 Running the Local API Server

Start the FastAPI application locally with Uvicorn:

```bash
uvicorn app.main:app --reload
```

Interactive API documentation will be available at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🐳 Docker Deployment

Build and run the evaluation environment using Docker:

```bash
# Build the Docker image
docker build -t coding-agent-rl-env .

# Run container tests
docker run --rm coding-agent-rl-env
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request if you have ideas for extending the benchmark suites or improving environment stability.

---

## 📜 License

Distributed under the Apache License. See `LICENSE` for more information.
