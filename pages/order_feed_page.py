from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class OrderFeedPage(BasePage):

    def drag_ingredient(self):
        self.drag_and_drop(OrderFeedPageLocators.INGREDIENT,
                           OrderFeedPageLocators.CONSTRUCTOR)

    def click_order(self):
        self.driver.find_element(*OrderFeedPageLocators.BUTTON_ORDER).click()

    def get_total_all_time(self):
        return self.driver.find_element(*OrderFeedPageLocators.TOTAL_ALL_TIME).text

    def get_total_today(self):
        return self.driver.find_element(*OrderFeedPageLocators.TOTAL_TODAY).text

    def close_modal(self):
        self.driver.find_element(*OrderFeedPageLocators.CLOSE_MODAL).click()

    def open_feed(self):
        self.driver.find_element(*OrderFeedPageLocators.ORDER_FEED_TAB).click()

    def get_in_progress(self):
        return self.driver.find_element(*OrderFeedPageLocators.IN_PROGRESS)

    def wait_order_number_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderFeedPageLocators.ORDER_TITLE)
        )

