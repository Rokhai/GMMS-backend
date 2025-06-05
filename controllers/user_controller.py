from config.supabase import get_supabase_client
from models.user_model import User, UserUpdate

supabase = get_supabase_client()


def create_user(user: User):
    """
    Insert a new user into the 'users' table in Supabase.
    Returns the created user record or an error message.
    """
    data = user.model_dump(exclude_unset=True)
    try:
        response = supabase.table("users").insert(data).execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}

def get_all_users():
    """
    Retrieve all users from the 'users' table.
    Returns a list of user records or an error message.
    """
    try:
        response = supabase.table("users").select("*").execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}

def update_user(user_id: int, user: UserUpdate):
    """
    Update an existing user in the 'users' table.
    Returns the updated user record or an error message.
    """
    data = user.model_dump(exclude_unset=True)  # Exclude unset fields
    try:
        if not data:
            return {"error": "No fields to update."}
        
        response = supabase.table("users").update(data).eq("id", user_id).execute()
        if response.data is None or len(response.data) == 0:
            return {"error": "User not found."}
        
        return response.data
    except Exception as e:
        return {"error": str(e)}

def delete_user(user_id: int):
    """
    Remove a user from the 'users' table.
    Returns a success message or an error message.
    """
    try:
        response = supabase.table("users").delete().eq("id", user_id).execute()
        if response.data is None or len(response.data) == 0:
            return {"error": "User not found."}
        return {"message": "User deleted successfully."}
    except Exception as e:
        return {"error": str(e)}
