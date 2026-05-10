from locators.order_feed_page_locators import OrderFeedPageLocators


class TestOrderFeed:

    def test_total_all_time_increases(self, created_order):
        page = created_order
        before = int(page.get_total_all_time())
        page.drag_ingredient()
        page.click_order()
        page.wait_order_number_visible()
        page.close_modal()
        page.open_feed()
        after = int(page.get_total_all_time())
        assert after > before


    def test_total_today_increases(self, created_order):
        page = created_order
        before = int(page.get_total_today())
        page.drag_ingredient()
        page.click_order()
        page.wait_order_number_visible()
        page.close_modal()
        page.open_feed()
        after = int(page.get_total_today())
        assert after > before


    def test_order_appears_in_progress(self, created_order):
        page = created_order
        page.drag_ingredient()
        page.click_order()
        page.wait_order_number_visible()
        page.close_modal()
        page.open_feed()

        in_progress = page.get_in_progress()

        assert in_progress != []
    
