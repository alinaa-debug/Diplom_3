from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.main_page_locators import MainPageLocators
from data.data import FEED_URL


class OrderPage(BasePage):

    def open_feed(self):
        self.click(MainPageLocators.ORDER_FEED_TAB)

    def wait_feed(self):
        return self.wait_for_url(FEED_URL)

    def total_all(self):
        return self.wait_visible(OrderFeedPageLocators.TOTAL_DONE)
    
    def text_total_all(self):
        self.wait_visible(OrderFeedPageLocators.TOTAL_DONE)
        return self.text(OrderFeedPageLocators.TOTAL_DONE)
    

    def total_today(self):
        return self.wait_visible(OrderFeedPageLocators.TODAY_DONE)
    
    def text_total_today(self):
        self.wait_visible(OrderFeedPageLocators.TODAY_DONE)
        return self.text(OrderFeedPageLocators.TODAY_DONE)
    
    def in_progress(self):
        return self.wait_visible(OrderFeedPageLocators.ORDER_IN_PROGRESS)

    
    def text_in_progress(self):
        self.wait_visible(OrderFeedPageLocators.ORDER_IN_PROGRESS)
        return self.text(OrderFeedPageLocators.ORDER_IN_PROGRESS)

    

    