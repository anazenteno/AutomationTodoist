from playwright.sync_api import Page

from page_object.utilities import Utilities


class LoginPage:
    click_login = "//a[@class='Z2j5FoeQ_umI7vX0SmxF zA288Pg0ZRE8YcTi8CRc AisLsJaE_AWnIhDlnTUV yJmXDmy7f2C2dFexmqOR'][contains(.,'Iniciar sesión')]"
    username_input = "//input[contains(@id,'element-0')]"
    password_input = "//input[contains(@id,'element-3')]"
    login_btn = "//button[contains(@data-gtm-id,'start-email-login')]"

    def __init__(self, page: Page):
        self.page = page
        self.utilities = Utilities(page)

    def click_login_link(self):
        self.utilities.click_element(self.click_login)

    def set_text_username_input(self, text):
        self.utilities.fill_input_element(self.username_input, text)

    def set_text_password_input(self, text):
        self.utilities.fill_input_element(self.password_input, text)

    def click_login_btn(self):
        self.utilities.click_element(self.login_btn)
