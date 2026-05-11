from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):
    def drag_ingredient(self):
        self.drag_and_drop(
            OrderFeedPageLocators.INGREDIENT,
            OrderFeedPageLocators.CONSTRUCTOR
        )

    def click_order(self):

        self.click_element(OrderFeedPageLocators.BUTTON_ORDER)

    def get_total_all_time(self):

        return self.find_element(OrderFeedPageLocators.TOTAL_ALL_TIME).text

    def get_total_today(self):

        return self.find_element(OrderFeedPageLocators.TOTAL_TODAY).text

    def close_modal(self):

        self.click_element(OrderFeedPageLocators.CLOSE_MODAL)

    def open_feed(self):

        self.click_element(OrderFeedPageLocators.ORDER_FEED_TAB)

    def get_in_progress(self):

        return self.find_element(OrderFeedPageLocators.IN_PROGRESS)

    def wait_order_number_visible(self):

        return self.is_visible(OrderFeedPageLocators.ORDER_TITLE)




