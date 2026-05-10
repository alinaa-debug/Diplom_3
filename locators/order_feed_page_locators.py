from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    TOTAL_ALL_TIME = (
        By.XPATH,
        "(//p[contains(@class,'OrderFeed_number')])[1]")
    
    TOTAL_TODAY = (
        By.XPATH,
        "(//p[contains(@class,'OrderFeed_number')])[2]")

    BUTTON_ORDER = (By.XPATH,"//button[text()='Оформить заказ']")
    
    ORDER_TITLE = (By.XPATH,"//p[text()='идентификатор заказа']")

    CLOSE_MODAL = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

    ORDER_FEED_TAB = (By.XPATH,"//p[text()='Лента заказов']")

    INGREDIENT = (By.XPATH,"//p[text()='Флюоресцентная булка R2-D3']/ancestor::a")

    CONSTRUCTOR = (By.XPATH,"//ul[contains(@class,'BurgerConstructor_basket__list')]")

    IN_PROGRESS = (By.XPATH,"//ul[contains(@class,'orderListReady')]")