from config.supabase import get_supabase_client
from models.auth_model import Auth

supabase = get_supabase_client()

def register_user(data: Auth):
    """
    Register a new user by creating an account with email and password.
    
    Args:
        email (str): The user's email.
        password (str): The user's password.
        
    Returns:
        dict: A success message or an error message.
    """
    data = data.dict(exclude_unset=True)
    try:
        response = supabase.auth.sign_up(data)
        return {"message": "Registration successful", "user": response.user}
    except Exception as e:
        return {"error": str(e)}

def login_user(email: str, password: str):
    """
    Log in a user by verifying their email and password.
    
    Args:
        email (str): The user's email.
        password (str): The user's password.
        
    Returns:
        dict: A success message or an error message.
    """
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        if not response.user:
            return {"error": "Invalid email or password"}

        
        return {"message": "Login successful", "user": response.user}
    except Exception as e:
        return {"error": str(e)}

def get_user_profile():
    """
    Get the profile of the currently logged-in user.
    
    Returns:
        dict: The user's profile information or an error message.
    """
    try:
        user = supabase.auth.get_user()
        if not user:
            return {"error": "User not found"}
        return {"data": user}
    except Exception as e:
        return {"error": str(e)}

def logout_user():
    """
    Log out the current user.
    
    Returns:
        dict: A success message or an error message.
    """
    try:
        response = supabase.auth.sign_out()
        if not response:
            return {"error": "Logout failed"}

        return {"message": "Logout successful"}
    except Exception as e:
        return {"error": str(e)}