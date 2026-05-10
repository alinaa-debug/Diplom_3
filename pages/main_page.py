from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):

    def click_constructor(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_TAB)
        )
        self.driver.find_element(*MainPageLocators.CONSTRUCTOR_TAB).click()

    def click_order_feed(self):
        self.driver.find_element(*MainPageLocators.ORDER_FEED_TAB).click()

    def open_ingredient(self):
        self.driver.find_element(*MainPageLocators.INGREDIENT).click()

    def is_constructor_title_visible(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)).is_displayed()
    
    def is_order_feed_title_visible(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_FEED_TAB)).is_displayed()

    def close_modal(self):
        self.driver.find_element(*MainPageLocators.CLOSE_MODAL).click()

    def is_modal_open(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.MODAL)
        )

    def is_modal_closed(self):
        return WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL)
        )

    def get_counter_value(self):
        elements = self.driver.find_elements(*MainPageLocators.COUNTER)
        return int(elements[0].text) if elements else 0

    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
 


    def drag_and_drop(self, source_locator, target_locator):

        self.find_element_with_wait(source_locator)
        self.find_element_with_wait(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0,
                               false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0,
                               false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0,
                               false, false, false, false, 0, null);
            target.dispatchEvent(evt);
        """, element_from, element_to)
    
    


