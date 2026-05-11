from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def click_constructor(self):

        self.click_element(MainPageLocators.CONSTRUCTOR_TAB)

    def click_order_feed(self):

        self.click_element(MainPageLocators.ORDER_FEED_TAB)

    def open_ingredient(self):

        self.click_element(MainPageLocators.INGREDIENT)

    def close_modal(self):

        self.click_element(MainPageLocators.CLOSE_MODAL)

    def is_constructor_title_visible(self):

        return self.is_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    def is_order_feed_title_visible(self):

        return self.is_visible(MainPageLocators.ORDER_FEED_TITLE)

    def is_modal_open(self):

        return self.is_visible(MainPageLocators.MODAL)

    def is_modal_closed(self):

        return self.is_invisible(MainPageLocators.MODAL)

    def get_counter_value(self):

        text = self.get_first_element_text(MainPageLocators.COUNTER)
        return int(text) if text else 0

    def add_ingredient_to_constructor(self):

        self.drag_and_drop(
            MainPageLocators.INGREDIENT,
            MainPageLocators.DROP_AREA
        )



    
    


