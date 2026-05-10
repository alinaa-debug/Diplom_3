from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPage(BasePage):

    def go_to_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AccountPageLocators.PERSONAL_ACCOUNT)
        )
        self.driver.find_element(*AccountPageLocators.PERSONAL_ACCOUNT).click()

    def go_to_register(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AccountPageLocators.REGISTRATION_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",button)

        self.driver.find_element(*AccountPageLocators.REGISTRATION_BUTTON).click()

    def register(self, name, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AccountPageLocators.NAME_BUTTON)
        )
        self.driver.find_element(*AccountPageLocators.NAME_BUTTON).send_keys(name)
        self.driver.find_element(*AccountPageLocators.EMAIL_BUTTON).send_keys(email)
        self.driver.find_element(*AccountPageLocators.PASSWORD_BUTTON).send_keys(password)
        self.driver.find_element(*AccountPageLocators.REGISTRATION).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AccountPageLocators.LOG_IN)
        )

    def login(self, email, password):
        self.driver.find_element(*AccountPageLocators.EMAIL_BUTTON_LOGIN).send_keys(email)
        self.driver.find_element(*AccountPageLocators.PASSWORD_BUTTON_LOGIN).send_keys(password)
        self.driver.find_element(*AccountPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AccountPageLocators.MAIN_PAGE_TITLE)
        )


