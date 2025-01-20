from .dtos import DeleteUserRequest, DeleteUserResponse
from fastapi import HTTPException

FAKE_USERS_DB = {
    1: {"id": 1, "email": "usr01@eg.com", "username": "usr01", "password": "pwd01", "app_version": "1.0.5"},
    2: {"id": 2, "email": "user02@eg.com", "username": "usr02", "password": "pwd02", "app_version": "1.0.9"},
    3: {"id": 3, "email": "user03@eg.com", "username": "usr03", "password": "pwd03", "app_version": "1.0.9"},
}


def delete_user(request: DeleteUserRequest) -> DeleteUserResponse:

    if request.id not in FAKE_USERS_DB:
        raise HTTPException(status_code=404, detail=f"User ID {request.id} not found..")

    del FAKE_USERS_DB[request.id]
    return DeleteUserResponse(success=True, message="User deleted")