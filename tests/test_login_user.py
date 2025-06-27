import allure
from data.messages import INCORRECT_EMAIL_OR_PASSWORD_MESSAGE
from helper.helper_user import create_fake_password, create_fake_email
from methods.login_user import LoginUser


@allure.feature("Тесты на авторизацию пользователя")
class TestLoginUser:

    @allure.title("Проверка успешной авторизации пользователя")
    def test_login_user_success(self, create_user):
        with allure.step("Запись данных пользователя в переменную"):
            payload = {
                "email": create_user["payload"]["email"],
                "password": create_user["payload"]["password"]
            }
        with allure.step("Авторизация пользователя"):
            status_code, response_body, token = LoginUser.post_login_user(payload=payload)
        with allure.step("Проверка, что статус код: 200"):
            assert status_code == 200
        with allure.step("Проверка, что параметр 'success': True"):
            assert response_body["success"] is True
        with allure.step("Проверка, что 'accessToken' присутствует в теле ответа"):
            assert "accessToken" in response_body

    @allure.title("Проверка авторизации с неверным логином и паролем")
    def test_login_user_unsuccessful(self):
        with allure.step("Запись данных пользователя в переменную"):
            payload = {
                "email": create_fake_email(),
                "password": create_fake_password()
            }
        with allure.step("Авторизация пользователя"):
            status_code, response_body, token = LoginUser.post_login_user(payload=payload)
        with allure.step("Проверка, что статус код: 401"):
            assert status_code == 401
        with allure.step("Проверка корректности сообщения"):
            assert response_body["message"] == INCORRECT_EMAIL_OR_PASSWORD_MESSAGE
