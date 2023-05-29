from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, browser: webdriver.Chrome, timeout=10):
        self.browser = browser
        self.url = None
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def error_message_text(self):
        return self.browser.find_element(By.CSS_SELECTOR, "span.rt-input-container__meta--error")

    def check_error_message(self, message_text: str):
        assert message_text == self.error_message_text().text, f'Некорректный текст ошибки'
