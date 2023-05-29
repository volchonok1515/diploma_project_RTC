from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    def name_field(self):
        return self.browser.find_element(By.CSS_SELECTOR, "input[name='firstName']")

    def last_name_field(self):
        return self.browser.find_element(By.CSS_SELECTOR, "input[name='lastName']")

    def region_input(self):
        return self.browser.find_element(By.XPATH, "//div[contains(@class, 'register-form__dropdown')]//input")

    def email_field(self):
        return self.browser.find_element(By.CSS_SELECTOR, "input#address")

    def password_field(self):
        return self.browser.find_element(By.CSS_SELECTOR, "input#password")

    def password_confirm_field(self):
        return self.browser.find_element(By.CSS_SELECTOR, "input#password-confirm")

    def register_btn(self):
        return self.browser.find_element(By.CSS_SELECTOR, "button[name='register']")

    def policy_link(self):
        return self.browser.find_element(By.CSS_SELECTOR, "a.rt-link")

    def field_placeholders(self):
        return self.browser.find_elements(By.CSS_SELECTOR, "span.rt-input__placeholder")

    def confirm_email_title(self):
        return self.browser.find_element(By.CSS_SELECTOR, "h1.card-container__title")

    def error_message_text(self):
        return self.browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta--error")

    def error_message_text_list(self):
        return self.browser.find_elements(By.CSS_SELECTOR, "span.rt-input-container__meta--error")

    def check_register_form_field(self):
        self.name_field().is_displayed()
        self.last_name_field().is_displayed()
        self.region_input().is_displayed()
        self.email_field().is_displayed()
        self.password_field().is_displayed()
        self.password_confirm_field().is_displayed()
        self.register_btn().is_displayed()
        assert self.register_btn().text == 'Продолжить', f'Ожидаемый текст в кнопке' \
                                                         f' "Продолжить" фактический: {self.register_btn().text}'
        self.policy_link().is_displayed()

    def check_confirm_email_title(self):
        assert self.confirm_email_title().text == 'Подтверждение email', f'Некорректный текст в заголовке'

    def check_error_message(self, message_text: str):
        assert message_text == self.error_message_text().text, f'Некорректный текст ошибки'

    def check_error_messages_for_all_fields(self):
        error_msg_list = [
            'Необходимо заполнить поле кириллицей. От 2 до 30 символов.',
            'Необходимо заполнить поле кириллицей. От 2 до 30 символов.',
            'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru',
            'Длина пароля должна быть не менее 8 символов',
            'Длина пароля должна быть не менее 8 символов'
        ]
        for index, item in enumerate(self.error_message_text_list()):
            assert item.text == error_msg_list[index], f'Некорректный текст ошибки'

    def check_default_region(self):
        assert self.region_input().get_property('value') == 'Москва г'