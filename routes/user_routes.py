from fastapi import APIRouter
from models.user_model import User, UserUpdate
from controllers.user_controller import create_user, fetch_all_users, update_user, delete_user

router = APIRouter()


@router.post("/users")
async def create(user: User):
    print("routes: Creating user:", user)
    """
    Create a new user in the 'users' table in Supabase.
    
    Args:
        user (dict): The user data to be created.
        
    Returns:
        dict: The created user record or an error message.
    """
    # from controllers.user_controller import create_user as create_user_controller
    return create_user(user)

@router.get("/users")
async def get_users():
    """
    Fetch all users from the 'users' table in Supabase.
    
    Returns:
        list: A list of user records.
    """
    return fetch_all_users()

@router.put("/users/{user_id}")
async def update(user_id: int, user: UserUpdate):
    """
    Update an existing user in the 'users' table in Supabase.
    
    Args:
        user_id (int): The ID of the user to be updated.
        user (User): The updated user data.
        
    Returns:
        dict: The updated user record or an error message.
    """
    # from controllers.user_controller import update_user as update_user_controller
    return update_user(user_id, user)

@router.delete("/users/{user_id}")
async def delete(user_id: int):
    """
    Delete a user from the 'users' table in Supabase.
    
    Args:
        user_id (int): The ID of the user to be deleted.
        
    Returns:
        dict: A success message or an error message.
    """
    # from controllers.user_controller import delete_user as delete_user_controller
    return delete_user(user_id)