from fastapi import APIRouter
from .handlers.dtos import CreateUserRequest, UserResponse, ListUserResponse, UpdateUserRequest, UpdateUserResponse
from .handlers.create_user import create_user
from .handlers.list_users import list_users
from .handlers.update_user import update_user


router = APIRouter()


@router.get("/.health")
def health():
    return {"status": "ok"}


@router.post("/")
def create_user_route(request: CreateUserRequest) -> UserResponse:
    return create_user(request)


@router.put("/{id}")
def update_user_route(request: UpdateUserRequest) -> UpdateUserResponse:
    return update_user(request)


@router.get("/{id}")
def get_user_route(id: int):
    # Informacion del usuario
    return {
        "id": id
    }


@router.get("/")
def list_users_route() -> ListUserResponse:
    return list_users()


@router.delete("/{id}")
def delete_user_route(id: int):
    pass