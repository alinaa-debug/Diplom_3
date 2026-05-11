from selenium.webdriver.common.by import By

class MainPageLocators:

    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']")
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    ORDER_FEED_TITLE = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a")
    COUNTER = (By.XPATH, "//a[contains(@href, '/61c0c5a71d1f82001bdaaa70')]//p[(@class='counter_counter__num__3nue1')]")
    CONSTRUCTOR = (By.XPATH, "//ul[@class,'BurgerConstructor_basket__list__l9dp_']")
    DROP_AREA = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal')]")
    CLOSE_MODAL = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
