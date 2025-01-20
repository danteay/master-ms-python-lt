from fastapi import HTTPException

from .dtos import GetUserRequest,GetUserResponse


FAKE_USERS_DB = {
    1: {"id": 1, "email": "usr01@eg.com", "username": "usr01", "password": "pwd01", "app_version": "1.0.5"},
    2: {"id": 2, "email": "user02@eg.com", "username": "usr02", "password": "pwd02", "app_version": "1.0.9"},
    3: {"id": 3, "email": "user03@eg.com", "username": "usr03", "password": "pwd03", "app_version": "1.0.9"},
}

def get_user(request: GetUserRequest) -> GetUserResponse:
    user = FAKE_USERS_DB.get(request.id)

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return GetUserResponse(**user)
