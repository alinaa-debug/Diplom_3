from selenium.webdriver.common.by import By

class AccountPageLocators:
    NAME_BUTTON = (By.XPATH, "(//input[@type='text'])[1]")
    EMAIL_BUTTON = (By.XPATH, "(//input[@type='text'])[2]")
    PASSWORD_BUTTON = (By.XPATH, "//input[@type='password']")
    
    REGISTRATION_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")
    REGISTRATION = (By.XPATH, "//button[text()='Зарегистрироваться']")
    EMAIL_BUTTON_LOGIN = (By.NAME, "name")
    PASSWORD_BUTTON_LOGIN = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    LOG_IN = (By.XPATH, "//h2[text()='Вход']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()= 'Личный Кабинет']")

    MAIN_PAGE_TITLE = (By.XPATH, "//span[text()='Булки']")