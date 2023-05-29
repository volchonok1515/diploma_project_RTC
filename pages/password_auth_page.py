from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PasswordAuthPage(BasePage):

    def phone_tab(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div#t-btn-tab-phone")

    def email_tab(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div#t-btn-tab-email")

    def login_tab(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div#t-btn-tab-login")

    def ls_tab(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div#t-btn-tab-ls")

    def user_name_input(self):
        return self.browser.find_element(By.CSS_SELECTOR, "input#username")

    def password_input(self):
        return self.browser.find_element(By.CSS_SELECTOR, "input#password")

    def forgot_password_link(self):
        return self.browser.find_element(By.CSS_SELECTOR, "a#forgot_password")

    def enter_btn(self):
        return self.browser.find_element(By.CSS_SELECTOR, "button#kc-login")

    def enter_by_code_btn(self):
        return self.browser.find_element(By.CSS_SELECTOR, "button#back_to_otp_btn")

    def register_link(self):
        return self.browser.find_element(By.CSS_SELECTOR, "a#kc-register")

    def wrong_login_message_text(self):
        return self.browser.find_element(By.CSS_SELECTOR, "span#form-error-message")

    def click_register_link(self):
        from pages.register_page import RegisterPage
        self.register_link().click()
        return RegisterPage(self.browser)

    def url_should_have(self, url: str):
        assert url in self.browser.current_url, f'Неверный URL'

    def check_wrong_login_error_message(self, message_text: str):
        assert message_text == self.wrong_login_message_text().text, f'Некорректный текст ошибки'

    def click_on_enter_by_code_btn(self):
        self.enter_by_code_btn().click()
        from pages.code_auth_page import CodeAuthPage
        return CodeAuthPage(self.browser)

    def click_on_forgot_password_link(self):
        from pages.restore_password_page import RestorePasswordPage
        self.forgot_password_link().click()
        return RestorePasswordPage(self.browser)

    def check_tabs_text(self):
        assert self.phone_tab().text == 'Номер', f'Некорректный текст вкладки'
        assert self.email_tab().text == 'Почта', f'Некорректный текст вкладки'
        assert self.login_tab().text == 'Логин', f'Некорректный текст вкладки'
        assert self.ls_tab().text == 'Лицевой счет', f'Некорректный текст вкладки'

    def phone_tab_should_be_activ_by_default(self):
        assert 'active' in self.phone_tab().get_attribute('class'), f'Вкладка не активна'