from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RestorePasswordPage(BasePage):
    def page_title(self):
        return self.browser.find_element(By.CSS_SELECTOR, "h1.card-container__title")

    def should_be_restore_page(self):
        assert self.page_title().text == 'Восстановление пароля', f'Некорректный текст в заголовке'