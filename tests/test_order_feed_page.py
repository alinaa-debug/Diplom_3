
from data.data import BASE_URL
from pages.main_page import MainPage
from pages.order_feed_page import OrderPage


class TestOrderFeedPage:

    def test_total_done_counter_increases_after_order_created(self, driver):
  
        main_page = MainPage(driver)
        order_feed_page = OrderPage(driver)

        main_page.open(BASE_URL)

        order_feed_page.open_feed()

        old_total = int(order_feed_page.text_total_all())

        main_page.click_constructor_button()

        main_page.get_order_number()

        order_feed_page.open_feed()

        new_total = int(order_feed_page.text_total_all())

        assert new_total > old_total

    def test_today_done_counter_increases_after_order_created(self, driver):
     
        main_page = MainPage(driver)
        order_feed_page = OrderPage(driver)

        main_page.open(BASE_URL)

        order_feed_page.open_feed()

        old_today_total = int(order_feed_page.text_total_today())

        main_page.click_constructor_button()

        main_page.get_order_number()

        order_feed_page.open_feed()

        new_today_total = int(order_feed_page.text_total_today())

        assert new_today_total > old_today_total

    def test_order_number_appears_in_progress_section(self, driver):

        main_page = MainPage(driver)
        order_feed_page = OrderPage(driver)

        main_page.open(BASE_URL)

        order_number = main_page.get_order_number()

        order_feed_page.open_feed()

        order_feed_page.in_progress()

        assert order_number in order_feed_page.text_in_progress()