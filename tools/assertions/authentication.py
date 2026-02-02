import allure

from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true
from tools.logger import get_logger

logger = get_logger("AUTHENTICATION_ASSERTIONS")


@allure.step("Check login response")
def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет ответ на авторизацию.

    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если отсутствует токен или есть пустыне поля.
    """
    logger.info("Check login response")
    assert_equal(
        name='tokenType',
        actual=response.token.token_type,
        expected="bearer",
    )
    assert_is_true(
        name='accessToken',
        actual=response.token.access_token,
    )
    assert_is_true(
        name='refreshToken',
        actual=response.token.refresh_token,
    )
