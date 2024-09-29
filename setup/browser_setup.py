# setup/browser_setup.py

from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def browser():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    # Set the browser to full-screen mode
    driver.maximize_window()

    yield driver  # Provide the driver to the tests

    driver.quit()  # Clean up after tests
