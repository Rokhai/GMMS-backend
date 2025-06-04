from fastapi import APIRouter   
from models.auth_model import Auth
from controllers.auth_controller import login_user, register_user, logout_user, get_user_profile


router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


@router.post("/register")
async def register(data: Auth):
    """
    Register a new user by creating an account with email and password.
    
    Args:
        email (str): The user's email.
        password (str): The user's password.
        
    Returns:
        dict: A success message or an error message.
    """
    return register_user(data)

@router.post("/login")
async def login(data: Auth):
    """
    Log in a user by verifying their email and password.
    
    Args:
        email (str): The user's email.
        password (str): The user's password.
        
    Returns:
        dict: A success message or an error message.
    """
    return login_user(data.email, data.password)


@router.get("/profile")
async def get_profile():
    """
    Get the profile of the currently logged-in user.
    
    Returns:
        dict: The user's profile information or an error message.
    """
    # This function should return the current user's profile
    # For now, we will return a placeholder response
    return get_user_profile()
   

@router.post("/logout")
async def logout():
    """
    Log out the current user.
    
    Returns:
        dict: A success message or an error message.
    """
    return logout_user()
