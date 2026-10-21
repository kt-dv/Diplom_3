from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_to_disappear(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))