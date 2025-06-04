from fastapi import FastAPI
from models.user_model import User

# Import routes
from routes.user_routes import router as user_router
from routes.auth_routes import router as auth_router

# Initialize FastAPI app
app = FastAPI()

# Register the user router
app.include_router(user_router, prefix="/api/v1", tags=["users"])
# Register the auth router
app.include_router(auth_router)

# Define a simple route
@app.get("/")
async def root():
    return {"message": "Hello World!, this is a FastAPI app with Supabase integration."}