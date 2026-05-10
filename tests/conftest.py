import pytest
from selenium import webdriver
from data.data import BASE_URL,FEED_URL , UserData
from pages.account_page import AccountPage
from pages.order_feed_page import OrderFeedPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def driver2():
    driver = webdriver.Firefox()
    driver.get(FEED_URL)
    yield driver
    driver.quit()

@pytest.fixture
def account_page(driver):
    return AccountPage(driver)

@pytest.fixture
def login(account_page):
    account_page.go_to_login()
    account_page.login(email= UserData.EMAIL, password= UserData.PASSWORD)

@pytest.fixture
def created_order(driver, login):
    page = OrderFeedPage(driver)
    page.drag_ingredient()
    page.click_order()
    page.wait_order_number_visible()
    page.close_modal()
    page.open_feed()
    return page    







