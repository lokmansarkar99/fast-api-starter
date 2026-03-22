# ⚡ FastAPI CRUD Starter

A clean, production-ready REST API built with **FastAPI + MySQL**, featuring full CRUD operations with password hashing and Pydantic validation.

> 🚀 Perfect starter template for healthcare, SaaS, or any user-management system.

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI 0.135+ |
| Database | MySQL |
| ORM | SQLAlchemy 2.0 |
| Validation | Pydantic v2 |
| Password Hashing | Passlib + bcrypt |
| Server | Uvicorn |
| Config | python-dotenv |

---

## 📁 Project Structure

```
fastapi-crud/
├── venv/               # Virtual environment
├── .env                # Environment variables (never commit this)
├── database.py         # DB connection & session
├── models.py           # SQLAlchemy table models
├── schemas.py          # Pydantic request/response schemas
├── crud.py             # Database operations (service layer)
├── routes.py           # API route handlers
└── main.py             # App entry point
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- MySQL running locally
- pip

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-crud.git
cd fastapi-crud
```

### 2. Create and activate virtual environment

```bash
# Create
python -m venv venv

# Activate (Windows PowerShell)
venv\Scripts\Activate.ps1

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv "passlib[bcrypt]" "pydantic[email]" "bcrypt==4.0.1"
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_NAME=fast_api
```

### 5. Create the MySQL database

```sql
CREATE DATABASE IF NOT EXISTS fast_api;
```

### 6. Run the server

```bash
uvicorn main:app --reload
venv\Scripts\uvicorn.exe main:app --reload 
```

Server will start at: **`http://127.0.0.1:8000`**

---

## 📖 API Documentation

FastAPI auto-generates interactive docs — no Postman setup needed!

| UI | URL |
|---|---|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

---

## 🔗 API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/users/` | Get all users |
| `GET` | `/users/{id}` | Get a single user by ID |
| `POST` | `/users/` | Create a new user |
| `PUT` | `/users/{id}` | Update a user |
| `DELETE` | `/users/{id}` | Delete a user |

---

## 📝 Request & Response Examples

### ➕ Create User — `POST /users/`

**Request Body:**
```json
{
  "name": "Lokman Sarker",
  "phone": "01700000000",
  "email": "lokman@example.com",
  "password": "secret123"
}
```

**Response `201`:**
```json
{
  "id": 1,
  "name": "Lokman Sarker",
  "phone": "01700000000",
  "email": "lokman@example.com"
}
```

> 🔒 Password is **never** returned in any response.

---

### 📋 Get All Users — `GET /users/`

**Response `200`:**
```json
[
  {
    "id": 1,
    "name": "Lokman Sarker",
    "phone": "01700000000",
    "email": "lokman@example.com"
  }
]
```

---

### 🔍 Get Single User — `GET /users/1`

**Response `200`:**
```json
{
  "id": 1,
  "name": "Lokman Sarker",
  "phone": "01700000000",
  "email": "lokman@example.com"
}
```

**Response `404`:**
```json
{
  "detail": "User not found"
}
```

---

### ✏️ Update User — `PUT /users/1`

**Request Body** (all fields optional):
```json
{
  "name": "Lokman Updated",
  "phone": "01800000000"
}
```

**Response `200`:**
```json
{
  "id": 1,
  "name": "Lokman Updated",
  "phone": "01800000000",
  "email": "lokman@example.com"
}
```

---

### 🗑️ Delete User — `DELETE /users/1`

**Response `200`:**
```json
{
  "message": "User deleted successfully"
}
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE users (
  id       INT AUTO_INCREMENT PRIMARY KEY,
  name     VARCHAR(100) NOT NULL,
  phone    VARCHAR(20)  NOT NULL UNIQUE,
  email    VARCHAR(150) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);
```

> Table is auto-created on server startup via SQLAlchemy — no manual migration needed.

---

## 🔒 Security Notes

- Passwords are hashed using **bcrypt** before storing
- Raw passwords are never logged or returned in responses
- `.env` file is excluded from version control via `.gitignore`

---

## 🚫 .gitignore

Make sure your `.gitignore` includes:

```
venv/
.env
__pycache__/
*.pyc
```

---

## 🗺️ Roadmap

- [ ] JWT Authentication
- [ ] Role-based access control (admin, doctor, patient)
- [ ] Pagination for user list
- [ ] Docker support
- [ ] Unit tests with pytest

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

[MIT](LICENSE)

---

<p align="center">Built with ❤️ using FastAPI</p>
