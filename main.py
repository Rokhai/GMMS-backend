from fastapi import FastAPI
from models.user_model import User

# Import routes
from routes.user_routes import router as user_router

# Initialize FastAPI app
app = FastAPI()

# user = User(email="rokh@gmail.com", password="123456")
# print(user)

# Register the user router
app.include_router(user_router, prefix="/api/v1", tags=["users"])


# Define a simple route
@app.get("/")
async def root():
    
    return {"message": "Hello World!, this is a FastAPI app with Supabase integration."}