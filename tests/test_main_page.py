from data.data import BASE_URL, FEED_URL
from pages.main_page import MainPage
from pages.account_page import AccountPage

class TestMainPage:

    def test_click_constructor_tab_opens_constructor_page(self, driver):

        main_page = MainPage(driver)
        main_page.click_order_button()
        main_page.click_constructor_button()
        
        main_page.wait_url_constructor()
        assert main_page.get_current_url() == BASE_URL

    def test_click_order_feed_tab_opens_feed_page(self, driver):
        main_page = MainPage(driver)

        main_page.click_order_button()

        main_page.wait_url_order()
        assert main_page.get_current_url() == FEED_URL


    def test_click_ingredient_opens_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.get_details_ingredients()
        details_popup = main_page.get_details_ingredients()
        assert details_popup.is_displayed()



    def test_close_ingredient_popup_by_click_cross(self, driver):
        main_page = MainPage(driver)

        main_page.click_ingredient()
        main_page.get_details_ingredients()

        main_page.close_details_ingredients()

        assert main_page.wait_close_details_ingredient()

    def test_counter_increases_after_adding_ingredient(self, driver):
        main_page = MainPage(driver)

        main_page.add_ingredient_to_basket()
        main_page.wait_for_ingredient_count_changing()

        assert main_page.check_counter_of_ingredients() == '2'