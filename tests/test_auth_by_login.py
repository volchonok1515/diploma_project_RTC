import pytest

from pages.code_auth_page import CodeAuthPage


class TestAuthByPhone:
    login = 'rtkid_1683378325024'
    password = 'Pro33160900'

    @staticmethod
    def auth_page(browser):
        code_auth_page = CodeAuthPage(browser).open()
        pass_auth_page = code_auth_page.click_on_enter_with_password_btn()
        return pass_auth_page

    @pytest.mark.xfail(reason="Не корректное название вкладки 'Номер'")
    def test_check_auth_tabs(self, browser):
        auth_page = self.auth_page(browser)
        auth_page.check_tabs_text()

    def test_check_default_active_tab(self, browser):
        auth_page = self.auth_page(browser)
        auth_page.phone_tab_should_be_activ_by_default()

    @pytest.mark.xfail(reason="Редирект после логина на не правильную страницу")
    def test_auth_by_login(self, browser):
        auth_page = self.auth_page(browser)
        auth_page.user_name_input().send_keys(self.login)
        auth_page.password_input().send_keys(self.password)
        auth_page.enter_btn().click()
        auth_page.url_should_have('redirect_uri')

    def test_auth_with_login_like_password(self, browser):
        auth_page = self.auth_page(browser)
        auth_page.user_name_input().send_keys(self.password)
        auth_page.password_input().send_keys(self.login)
        auth_page.enter_btn().click()
        auth_page.check_wrong_login_error_message('Неверный логин или пароль')

    def test_auth_with_correct_login_and_wrong_password(self, browser):
        auth_page = self.auth_page(browser)
        auth_page.user_name_input().send_keys(self.login)
        auth_page.password_input().send_keys(self.password + '1')
        auth_page.enter_btn().click()
        auth_page.check_wrong_login_error_message('Неверный логин или пароль')

    def test_auth_with_correct_password_and_wrong_login(self, browser):
        auth_page = self.auth_page(browser)
        auth_page.user_name_input().send_keys(self.login + '1')
        auth_page.password_input().send_keys(self.password)
        auth_page.enter_btn().click()
        auth_page.check_wrong_login_error_message('Неверный логин или пароль')