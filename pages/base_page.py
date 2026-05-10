from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def drag_and_drop(self, source_locator, target_locator):
        self.find_element_with_wait(source_locator)
        self.find_element_with_wait(target_locator)
        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)
        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
            source.dispatchEvent(new DragEvent('dragstart', {
            dataTransfer: dataTransfer
            }));
            target.dispatchEvent(new DragEvent('drop', {
                dataTransfer: dataTransfer
            }));
            source.dispatchEvent(new DragEvent('dragend', {
                dataTransfer: dataTransfer  }));
        """, element_from, element_to)

    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
