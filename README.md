# Auth Portal

A secure authentication REST API built with FastAPI and SQLite.

## Features
- User registration and login
- JWT authentication
- Role-based access control (user/admin)
- Admin panel (ban/unban users, change roles, delete users)
- Brute force protection (coming soon)

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Bcrypt
- Alembic

## Getting Started

### Installation
```bash
git clone https://github.com/yourname/auth-portal
cd auth-portal/backend
pip install -r requirements.txt
```

### Run
```bash
uvicorn app.main:app --reload
```

### API Docs
```
http://localhost:8000/docs
```

## Project Structure
```
auth-portal/
└── backend/
    └── app/
        ├── main.py
        ├── models.py
        ├── schemas.py
        ├── database.py
        ├── auth.py
        └── routers/
            ├── auth.py
            ├── users.py
            └── admin.py
```

## Roadmap
- [ ] Brute force protection
- [ ] Docker support
- [ ] Frontend with admin panel
- [ ] CI/CD pipeline
