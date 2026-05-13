from selenium.webdriver.common.by import By

class AccountPageLocators:

    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
 
    PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") 

    ENTERANCE_BUTTON = (By.XPATH, '//button[text()="Войти"]') 

    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")