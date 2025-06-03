# Gym Membership Management System Backend
This repository contains the backend of GMMS

## Clone the project with the submodule

The `supabase` folder is a Git submodule linked to the [GMMS-supabase](<SUPABASE_REPO_URL>) repository.

To clone the projet with the submodule:
```bash
git clone --recursive <MAIN_REPO_URL>
```

Update the submodule after pulling changes
```bash
git submodule update --remote
```
## Setup FastAPI & Supabase

### Python FastAPI

Install python packages

```bash
pip install -r requirements.txt
```

Run the uvicorn server
```bash
uvicorn main:app --reload
```
or

```
npm run uvi-dev
```

### Import the GMMS-supabase module

Add the supabase repository as a submodule
```bash
git submodule add <supabase_repo_url> supabase
```

git submodule add https://github.com/Rokhai/GMMS-supabase.git supabase

Initialize the submodule to fetch it contents
```bash
git submodule init
```
Update the submodule to fetch its contents
```bash
git submodule update
```

### Supabase Setup

Initialize supabase project local dev
```bash
npx supabase init
```

Start supabase stack
```bash
npx supabase start
```
Stop supabase
```bash
npx supabase stop
```

- Npm scripts
```bash
#Start the supabase
npm run sup-start

#Stop the supabase
npm run sup-stop
```

## Python Environment Setup

Create and activate a Python virtual environment to isolate dependencies:

```bash
python3 -m venv env
source env/bin/activate
```
Install FastAPI and Uvicorn (ASGI server to run FastAPI apps):

```bash
pip install fastapi uvicorn
```
Create a basic FastAPI app file, e.g., main.py:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```   
Run the server locally:

```bash
uvicorn main:app --reload
```

Visit http://127.0.0.1:8000 to see the API and http://127.0.0.1:8000/docs for auto-generated API docs.