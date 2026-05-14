from data.data import BASE_URL
from pages.main_page import MainPage
from pages.order_feed_page import OrderPage


class TestOrderFeedPage:

    def test_total_done_counter_increases_after_order_created(self, driver):
        order_feed = OrderPage(driver)
        main_page = MainPage(driver)
        order_feed.open_feed()
        order_feed.wait_feed()
        order_feed.total_all()
        before = order_feed.text_total_all()
        main_page.click_constructor_button()
        main_page.wait_url_constructor()
        main_page.get_order_number()
        main_page.click_order_button()

        order_feed.wait_feed()
        order_feed.total_all()
        new_total = order_feed.text_total_all()
        assert new_total > before



    def test_today_done_counter_increases_after_order_created(self, driver):
     
        order_feed = OrderPage(driver)
        main_page = MainPage(driver)
        order_feed.open_feed()
        order_feed.wait_feed()
        order_feed.total_today()
        before = order_feed.text_total_today()
        main_page.click_constructor_button()
        main_page.wait_url_constructor()
        main_page.get_order_number()
        main_page.click_order_button()

        order_feed.wait_feed()
        order_feed.total_today()
        new_total = order_feed.text_total_today()
        assert new_total > before


    def test_order_number_appears_in_progress_section(self, driver):
        order_feed = OrderPage(driver)
        main_page = MainPage(driver)
    
        number = main_page.get_order_number()
        main_page.click_order_button()
        main_page.wait_url_order()
        order_feed.wait_feed()
        order_feed.in_progress()

        order_feed.text_in_progress()
         
        in_work = order_feed.text_in_progress()
        
        assert (f'0{number}') == in_work
