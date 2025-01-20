from fastapi import APIRouter

from .handlers.delete_user import delete_user
from .handlers.dtos import CreateUserRequest, UserResponse, ListUserResponse, UpdateUserRequest, UpdateUserResponse, \
    GetUserResponse, GetUserRequest, DeleteUserResponse, DeleteUserRequest
from .handlers.create_user import create_user
from .handlers.get_user import get_user
from .handlers.list_users import list_users
from .handlers.update_user import update_user

router = APIRouter()


@router.get("/.health")
def health():
    return {"status": "ok"}


@router.post("/users/")
def create_user_route(request: CreateUserRequest) -> UserResponse:
    return create_user(request)


@router.put("/users/{user_id}")
def update_user_route(request: UpdateUserRequest) -> UpdateUserResponse:
    return update_user(request)


@router.get("/users/{user_id}", response_model=GetUserResponse)
def get_user_route(user_id: int):
    request = GetUserRequest(id=user_id)
    return get_user(request)


@router.get("/users/")
def list_users_route() -> ListUserResponse:
    return list_users()


@router.delete("/users/{user_id}", response_model=DeleteUserResponse)
def delete_user_route(user_id: int):
    request = DeleteUserRequest(id=user_id)
    return delete_user(request)