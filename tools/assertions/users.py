from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    assert_equal(response.user.email, request.email,"email")
    assert_equal(response.user.email, request.email, "last_name")
    assert_equal(response.user.email, request.email, "first_name")
    assert_equal(response.user.email, request.email, "middle_name")