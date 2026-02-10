 Full-Stack Digital Dashboard (Authentication + CRUD + Analytics)

A modern, production-ready **full-stack dashboard application** built as part of a technical assessment.  
The project demonstrates **secure authentication, clean UI/UX, scalable architecture, and real-world backend logic**.

---

# Features Overview

## Authentication & Security
- User **Signup / Login / Logout**
- **JWT-based authentication**
- Password hashing using **bcrypt**
- Protected routes (dashboard accessible only after login)
- Token-based API authorization

---

## Frontend (Primary Focus)
- Built with **Next.js (App Router) + TypeScript**
- Modern UI using **TailwindCSS**
- Responsive, high-end layout
- Glassmorphism cards & subtle shadows
- Client-side + server-side form validation
- User feedback (success / error messages)
- Clean navigation flow

---

## Backend (Supportive)
- Built with **FastAPI (Python)**
- RESTful APIs
- JWT authentication middleware
- SQLAlchemy ORM
- PostgreSQL / SQLite compatible
- Clean modular structure

---

## Dashboard Features
- User profile display
- CRUD operations on sample entities (Tasks / Worker Updates)
- Search & filter functionality
- Risk score computation (Digital Twin logic)
- Logout flow

---

## Scalability & Architecture
- Modular backend (routes / models / schemas / services)
- Clear separation of concerns
- Ready for production scaling
- Environment-based configuration
- Easy to plug into CI/CD pipelines

---

# Tech Stack

## Frontend
- **Next.js (App Router)**
- **TypeScript**
- **TailwindCSS**
- React Hooks

## Backend
- **FastAPI**
- **SQLAlchemy**
- **JWT (python-jose)**
- **bcrypt / passlib**

## Database
- PostgreSQL / SQLite (configurable)
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd fullstack-dashboard
 2️⃣ Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Backend runs on:
http://127.0.0.1:8000


API Docs:
http://127.0.0.1:8000/docs
