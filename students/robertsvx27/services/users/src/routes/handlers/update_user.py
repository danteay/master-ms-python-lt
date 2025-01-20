from .dtos import UpdateUserRequest, UpdateUserResponse, UserResponse


def update_user(request: UpdateUserRequest) -> UpdateUserResponse:
    updated_user_data = UserResponse (
        id = request.id,
        email = request.email or "example@copelme.com",
        username = request.username or "username",
        app_version = request.app_version
    )

    return UpdateUserResponse(
        id=updated_user_data.id,
        email=updated_user_data.email,
        username=updated_user_data.username,
        app_version=updated_user_data.app_version,
        data=[updated_user_data]
    )