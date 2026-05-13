from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")

    ORDER_FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']")

    ORDER_NUMBER = (By.XPATH, '//*[contains(@class, "type_digits-large")]')

    CONSTRUCTOR_BASKET = (By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]')

    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    MODAL_WINDOW = (By.XPATH, './/div[@class ="Modal_modal__container__Wo2l_"]')

    MODAL_TEXT = (By.XPATH, '//p[text()="идентификатор заказа"]')

    CLOSE_MODAL = (By.XPATH, '//button[contains(@class,"close")]')

    BUN_ITEM = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')

    SAUCE_ITEM = (By.XPATH, "//p[text()= 'Соус Spicy-X']")

    INGREDIENT_DETAILS = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//p[text()='Флюоресцентная булка R2-D3']")

    DEFAULT_ORDER_NUMBER = (By.XPATH, '//h2[text()="9999"]')

    INGREDIENT_COUNTER = (By.XPATH, "//a[contains(@href, '/61c0c5a71d1f82001bdaaa6d')]//p[(@class='counter_counter__num__3nue1')]")

    INGRIDIENT_BUN_DETAILS = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//p[text()='Флюоресцентная булка R2-D3']") 
    DETAILS_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]") 
    
    OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")