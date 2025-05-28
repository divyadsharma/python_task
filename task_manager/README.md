# ✅ FastAPI Task Manager

A simple Task Manager API built with FastAPI, SQLAlchemy, PostgreSQL, and Docker — inspired by Rails project structure.

---

## 📂 Project Structure

task_manager/
├── app/
│ ├── config.py
│ ├── main.py
│ ├── database.py
│ ├── models/
│ │ └── task.py
│ ├── schemas/
│ │ └── task_schema.py
│ ├── controllers/
│ │ └── task_controller.py
│ ├── crud/
│ │ └── task_crud.py
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


--- YAML

## 🧰 Tech Stack

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **PostgreSQL** – Database
- **Pydantic** – Schema validation
- **Docker** – Containerization
- **Uvicorn** – ASGI server

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/fastapi-task-manager.git
cd fastapi-task-manager

```bash
DATABASE_URL=postgresql://postgres:password@db:5432/tasks

```bash
docker-compose up --build
