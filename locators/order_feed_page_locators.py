from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    FEED_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')

    TOTAL_DONE = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")

    TODAY_DONE = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    ALL_ORDERS_DONE_TEXT = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')
    
    ORDER_IN_PROGRESS = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')

