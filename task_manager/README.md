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
```

### 2. Setup DATABASE_URL on local

```bash
DATABASE_URL=postgresql://postgres:password@db:5432/tasks

```

### 3. Run docker

```bash
docker-compose up --build
```

### 4. Run Swagger doc to check tasks

```bash
Start with swagger doc here
http://localhost:8000/docs#/
http://localhost:8000/redoc
```

