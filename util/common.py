from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


def wait_for_element_to_be_visible(driver, locator):
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.visibility_of_element_located(locator))
    print(f"Element visible {element}")
    return element
