from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class TestMainPage:
    def test_constructor_navigation(self, driver2):
        page = MainPage(driver2)
        page.click_constructor()
        assert page.is_constructor_title_visible()

    def test_order_feed_navigation(self, driver):
        page = MainPage(driver)
        page.click_order_feed()
        assert page.is_order_feed_title_visible()

    def test_modal_opens(self, driver):
        page = MainPage(driver)
        page.open_ingredient()
        assert page.is_modal_open()

    def test_modal_closes(self, driver):
        page = MainPage(driver)
        page.open_ingredient()
        page.close_modal()
        assert page.is_modal_closed()

    def test_counter_increases(self, driver):
        page = MainPage(driver)
        before = page.get_counter_value()
        page.drag_and_drop(
            MainPageLocators.INGREDIENT,
            MainPageLocators.DROP_AREA
        )
        WebDriverWait(driver, 10).until(
            lambda d: page.get_counter_value() > before
        )
        assert page.get_counter_value() > before