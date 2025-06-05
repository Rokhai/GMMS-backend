from fastapi import APIRouter
from models.user_model import User, UserUpdate
from controllers.user_controller import create_user, get_all_users, update_user, delete_user

router = APIRouter()


@router.post("/users")
async def create_user_route(user: User):
    """
    Create a new user.
    """
    return create_user(user)

@router.get("/users")
async def get_users_route():
    """
    Get all users.
    """
    return get_all_users()

@router.put("/users/{user_id}")
async def update_user_route(user_id: int, user: UserUpdate):
    """
    Update a user by ID.
    """
    return update_user(user_id, user)

@router.delete("/users/{user_id}")
async def delete_user_route(user_id: int):
    """
    Delete a user by ID.
    """
    return delete_user(user_id)