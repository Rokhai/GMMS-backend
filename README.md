# Gym Membership Management System Backend
This repository contains the backend of GMMS

## Prerequisites
- Python 3.12+


## Setup Python FastAPI

Create virtual environment
```bash
python3 -m venv env
```

Activate the virtual environment
-   Linux/macOS
```bash
source env/bin/activate
```
- Windows
```bash
env/Scripts/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Manual Installation
```bash
pip install fastapi uvicorn supabase
```

Run the uvicorn server
```bash
uvicorn main:app --reload
```

Visit http://127.0.0.1:8000 to see the API and http://127.0.0.1:8000/docs for auto-generated API docs.

## API Endpoints

### Default
- `GET /` - Root

### Users
- `GET /api/v1/users` - Get Users
- `POST /api/v1/users` - Create User
- `PUT /api/v1/users` - Update User
- `DELETE /api/v1/users` - Delete User

### Auth

- `POST /api/v1/auth/register` - Register 
- `POST /api/v1/auth/login` - Login
- `POST /api/v1/auth/logout` - Logout
-  `GET /api/v1/auth/profile` - Get Profile