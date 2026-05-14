from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.data import BASE_URL, FEED_URL

class MainPage(BasePage):

    def click_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_TAB)
     
    def wait_url_constructor(self):
        return self.wait_for_url(BASE_URL)
    
    def wait_url_order(self):
        return self.wait_for_url(FEED_URL)
    
    def click_order_button(self):
        self.wait_clickable(MainPageLocators.ORDER_FEED_TAB)
        self.click(MainPageLocators.ORDER_FEED_TAB)
    
    def click_ingredient(self):
        self.wait_visible(MainPageLocators.BUN_ITEM)
        self.click(MainPageLocators.BUN_ITEM)

    def get_details_ingredients(self):    
        return self.wait_visible(MainPageLocators.INGREDIENT_DETAILS)
    

    def close_details_ingredients(self):    
        return self.click(MainPageLocators.DETAILS_CLOSE_BUTTON)
    

    def wait_close_details_ingredient(self):
        return self.wait_invisible(MainPageLocators.INGREDIENT_DETAILS)
    
    
    def add_ingredient_to_basket(self):
        return self.drag_and_drop_ingredient(MainPageLocators.BUN_ITEM , MainPageLocators.CONSTRUCTOR_BASKET)

    def check_counter_of_ingredients(self):
        return self.text(MainPageLocators.INGREDIENT_COUNTER)    


    def wait_for_ingredient_count_changing(self):    
        return self.wait_visible(MainPageLocators.INGREDIENT_COUNTER)
    

    def get_order_number(self):

        self.drag_and_drop_ingredient(MainPageLocators.BUN_ITEM, MainPageLocators.CONSTRUCTOR_BASKET)

        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

        self.wait_visible(MainPageLocators.MODAL_WINDOW)
        self.wait_invisible(MainPageLocators.DEFAULT_ORDER_NUMBER)
        order_number = self.text(MainPageLocators.ORDER_NUMBER)
        self.click(MainPageLocators.CLOSE_MODAL)
        return order_number
    




    
    


