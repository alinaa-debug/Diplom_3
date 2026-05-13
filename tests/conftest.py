import pytest
from selenium import webdriver
from data.data import BASE_URL
from pages.account_page import AccountPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(BASE_URL)

    page = AccountPage(driver)
    page.login_in_system()

    yield driver
    driver.quit()






