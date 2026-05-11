from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):

    def go_to_login(self):
        self.click_element(AccountPageLocators.PERSONAL_ACCOUNT)

    def go_to_register(self):
        self.scroll_to_element(AccountPageLocators.REGISTRATION_BUTTON)
        self.click_element(AccountPageLocators.REGISTRATION_BUTTON)

    def register(self, name, email, password):
        self.send_keys(AccountPageLocators.NAME_BUTTON, name)
        self.send_keys(AccountPageLocators.EMAIL_BUTTON, email)
        self.send_keys(AccountPageLocators.PASSWORD_BUTTON, password)
        self.click_element(AccountPageLocators.REGISTRATION)
        self.is_visible(AccountPageLocators.LOG_IN)

    def login(self, email, password):

        self.send_keys(AccountPageLocators.EMAIL_BUTTON_LOGIN, email)
        self.send_keys(AccountPageLocators.PASSWORD_BUTTON_LOGIN, password)
        self.click_element(AccountPageLocators.LOGIN_BUTTON)
        self.is_visible(AccountPageLocators.MAIN_PAGE_TITLE)


