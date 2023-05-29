from pages.code_auth_page import CodeAuthPage
from helpers.data_generator import DataGenerator
import pytest


class TestRegistration:
    data_generator = DataGenerator()
    user_name = 'Тест-Юзер'

    @staticmethod
    def register_page(browser):
        code_auth_page = CodeAuthPage(browser).open()
        pass_auth_page = code_auth_page.click_on_enter_with_password_btn()
        register_page = pass_auth_page.click_register_link()
        return register_page

    @pytest.mark.xfail(reason="Не корректное название кнопки 'Продолжить'")
    def test_check_fields_on_register_page(self, browser):
        register_page = self.register_page(browser)
        register_page.check_register_form_field()

    def test_register_user_with_all_valid_date(self, browser):
        password = self.data_generator.get_password
        register_page = self.register_page(browser)
        register_page.name_field().send_keys(self.user_name)
        register_page.last_name_field().send_keys('Тестовый')
        #  регион по умолчанию оставляем
        register_page.email_field().send_keys(self.data_generator.get_email)
        register_page.password_field().send_keys(password)
        register_page.password_confirm_field().send_keys(password)
        register_page.register_btn().click()
        register_page.check_confirm_email_title()

    def test_register_user_with_short_name(self, browser):
        register_page = self.register_page(browser)
        register_page.name_field().send_keys('А')
        register_page.last_name_field().click()
        register_page.check_error_message('Необходимо заполнить поле кириллицей. От 2 до 30 символов.')

    def test_register_user_with_short_last_name(self, browser):
        register_page = self.register_page(browser)
        register_page.last_name_field().send_keys('А')
        register_page.name_field().click()
        register_page.check_error_message('Необходимо заполнить поле кириллицей. От 2 до 30 символов.')

    def test_register_user_with_wrong_email(self, browser):
        register_page = self.register_page(browser)
        register_page.email_field().send_keys('test@')
        register_page.name_field().click()
        register_page.check_error_message('Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, '
                                          'или email в формате example@email.ru')

    def test_register_user_with_wrong_password(self, browser):
        register_page = self.register_page(browser)
        register_page.password_field().send_keys('naya')
        register_page.password_confirm_field().click()
        register_page.check_error_message('Длина пароля должна быть не менее 8 символов')

    def test_register_user_with_wrong_password(self, browser):
        register_page = self.register_page(browser)
        register_page.password_field().send_keys('Наташанат')
        register_page.password_confirm_field().click()
        register_page.check_error_message('Пароль должен содержать только латинские буквы')

    def test_register_user_with_wrong_password(self, browser):
        register_page = self.register_page(browser)
        register_page.password_field().send_keys('123456789')
        register_page.password_confirm_field().click()
        register_page.check_error_message('Пароль должен содержать хотя бы одну заглавную букву')

    def test_register_user_with_wrong_password(self, browser):
        register_page = self.register_page(browser)
        register_page.password_field().send_keys('natashanat')
        register_page.password_confirm_field().click()
        register_page.check_error_message('Пароль должен содержать хотя бы одну заглавную букву')

    def test_register_user_with_wrong_password(self, browser):
        register_page = self.register_page(browser)
        register_page.password_field().send_keys('Natashanat')
        register_page.password_confirm_field().click()
        register_page.check_error_message('Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру')

    def test_register_user_with_wrong_confirm_password(self, browser):
        password = self.data_generator.get_password
        register_page = self.register_page(browser)
        register_page.name_field().send_keys(self.user_name)
        register_page.last_name_field().send_keys('Тестовый')
        register_page.email_field().send_keys(self.data_generator.get_email)
        register_page.password_field().send_keys(password)
        register_page.password_confirm_field().send_keys(password + '1')
        register_page.register_btn().click()
        register_page.check_error_message('Пароли не совпадают')

    def test_register_with_all_blank_fields(self, browser):
        register_page = self.register_page(browser)
        register_page.register_btn().click()
        register_page.check_error_messages_for_all_fields()

    def test_check_default_region(self, browser):
        register_page = self.register_page(browser)
        register_page.check_default_region()
