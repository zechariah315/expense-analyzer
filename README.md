# Expense Analyzer

Expense Analyzer is a web application for managing and analyzing personal expenses.

The project consists of a FastAPI backend and a frontend application. The backend provides a REST API for user management, authentication, and expense management.

## Features

- User registration and management
- User authentication
- JWT-based authentication
- Secure password hashing
- Create expenses
- Retrieve expenses belonging to a user
- PostgreSQL database
- SQLAlchemy ORM
- Database migrations with Alembic
- Interactive API documentation with Swagger UI

## Tech Stack

### Backend

- Python 3.12
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- psycopg2
- Alembic
- Pydantic
- PyJWT
- pwdlib
- Argon2
- python-dotenv

### Frontend

The frontend application is located in the `frontend` directory.

Frontend setup and technologies will be documented as the frontend development progresses.

---

# Project Structure

```text
expense-analyzer/
│
├── backend/
│   ├── alembic/
│   │   ├── versions/
│   │   └── env.py
│   │
│   ├── crud/
│   │   ├── expense.py
│   │   ├── user.py
│   │   └── __init__.py
│   │
│   ├── models/
│   │   ├── Expense.py
│   │   ├── User.py
│   │   └── __init__.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── expenses.py
│   │   ├── users.py
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── auth.py
│   │   ├── user.py
│   │   └── __init__.py
│   │
│   ├── database.py
│   ├── main.py
│   ├── schemas.py
│   ├── alembic.ini
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│
└── README.md

**Backend Architecture**

The backend is organized into several layers.

**Routers**
The routers directory contains the API endpoints.
The routers receive HTTP requests and pass the required work to the appropriate services or CRUD functions.

**Services**
The services directory contains application logic that is separate from the API routes.

**CRUD**
The crud directory contains database operations.

**Models**
The models directory contains SQLAlchemy ORM models that represent database tables.

**Schemas**
schemas.py contains Pydantic schemas.

**Database**
database.py contains the SQLAlchemy database configuration.

**Alembic**
Alembic is used to keep the PostgreSQL database schema synchronized with changes made to the SQLAlchemy models.


**Requirements**
Before running the backend, make sure you have:

Python 3.12
PostgreSQL
Git

**1. Clone the Repository**
Clone the repository and move into the project directory:
git clone <https://github.com/zechariah315/expense-analyzer>
cd expense-analyzer

**2. Create a Python Virtual Environment**
python -m venv backend/venv

**3. Activate the Virtual Environment**
.\backend\venv\Scripts\Activate.ps1

**4. Install Backend Dependencies**
cd backend
pip install -r requirements.txt

**Environment Variables**
Create a file named .env inside the backend directory
The .env file should contain:
DATABASE_URL=your_database_connection_string
SECRET_KEY=your_secret_key

**Database Setup**
The project uses PostgreSQL as its database.

After creating your PostgreSQL database and configuring DATABASE_URL, apply the existing Alembic migrations.

From the backend directory:
alembic upgrade head
This applies all existing migrations up to the latest version.

**Creating a New Migration**
After changing a SQLAlchemy model, a new Alembic migration can be generated with:
alembic revision --autogenerate -m "describe your change"
Then apply the migration:
alembic upgrade head

**Running the Backend**
Make sure the virtual environment is activated:
cd backend
uvicorn main:app --reload