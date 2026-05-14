from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
    
    def get_current_url(self):
        return self.driver.current_url
    
    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 20).until(EC.url_to_be(url))
    
    def wait_clickable(self,locator):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
       
    def find_locator(self, locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        self.driver.get(url)

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):

        element = self.wait_visible(locator)
        self.scroll_to_element(element)
        WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable(locator))
        element.click()

    def text(self, locator):
        return self.find_locator(locator).text

    def wait_invisible(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(locator)
        )
    
    def drag_and_drop_ingredient(self, ingridients_locator, constructor_locator):
        ingridients = self.wait_visible(ingridients_locator)
        constructor = self.wait_visible(constructor_locator)
        actions = ActionChains(self.driver)
        actions.click_and_hold(ingridients).move_to_element(constructor).release().perform()
        self.driver.execute_script("arguments[1].dispatchEvent(new Event('drop', { bubbles: true }));", ingridients, constructor)
  
    
    