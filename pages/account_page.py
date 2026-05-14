from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.data import UserData
from locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):

    def login_in_system(self):
        self.click(AccountPageLocators.PROFILE_BUTTON)
        self.wait_visible(AccountPageLocators.ENTERANCE_BUTTON)
        self.wait_visible(AccountPageLocators.EMAIL).send_keys(UserData.EMAIL)
        self.wait_visible(AccountPageLocators.PASSWORD).send_keys(UserData.PASSWORD)
        self.click(AccountPageLocators.ENTERANCE_BUTTON)
        self.wait_visible(MainPageLocators.PLACE_ORDER_BUTTON)