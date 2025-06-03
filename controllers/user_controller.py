from config.supabase import get_supabase_client
from models.user_model import User, UserUpdate

supabase = get_supabase_client()


def create_user(user: User):
    """
    Create a new user in the 'users' table in Supabase.
    
    Args:
        user (User): The user data to be created.
        
    Returns:
        dict: The created user record or an error message.
    """
    data = user.dict(exclude_unset=True)
    print("Creating user:", user)
    print("Creating user data:", data)

    try:
        response = supabase.table("users").insert(data).execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}

def fetch_all_users():
    """
    Fetch all users from the 'users' table in Supabase.
    
    Returns:
        list: A list of user records.
    """
    try:
        response = supabase.table("users").select("*").execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}

def update_user(user_id: int, user: UserUpdate):
    """
    Update an existing user in the 'users' table in Supabase.
    
    Args:
        user_id (int): The ID of the user to be updated.
        user (User): The updated user data.
        
    Returns:
        dict: The updated user record or an error message.
    """
    data = user.dict(exclude_unset=True)  # Exclude unset fields
    try:
        # if not user.email or not user.password:
        #     return {"error": "Email and password are required for update."}
        # if not isinstance(user_id, int):
        #     return {"error": "User ID must be an integer."}
        
        # if user.email is not None:
        #     # Update only if email is provided
        #     response = supabase.table("users").update({
        #         "email": user.email
        #     }).eq("id", user_id).execute()

        # if user.password is not None:
        #     # Update only if password is provided
        #     response = supabase.table("users").update({
        #         "password": user.password
        #     }).eq("id", user_id).execute()

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
    Delete a user from the 'users' table in Supabase.
    
    Args:
        user_id (int): The ID of the user to be deleted.
        
    Returns:
        dict: A success message or an error message.
    """
    try:
        response = supabase.table("users").delete().eq("id", user_id).execute()
        if response.data is None or len(response.data) == 0:
            return {"error": "User not found."}
        return {"message": "User deleted successfully."}
    except Exception as e:
        return {"error": str(e)}
