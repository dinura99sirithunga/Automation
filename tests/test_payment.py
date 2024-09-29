import time
import logging
import pytest
from setup.browser_setup import browser
from pages.payment_page import PaymentPage
from util.properties_reader import read_properties

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_payment_process(browser):
    properties = read_properties('config.properties')

    # Load configuration values
    url = properties['url']
    card_number = properties['card_number']
    expiry_date = properties['expiry_date']
    cvv = properties['cvv']

    # Open the payment page
    logging.info("Opening payment page: {url}")
    browser.get(url)


    # Create an instance of the PaymentPage
    payment_page = PaymentPage(browser)

    # Perform payment actions
    logging.info("Clicking on 'Pay Bill' button.")
    payment_page.click_pay_bill()

    # Wait for progress bar
    time.sleep(10)


    logging.info("Clicking on 'Split Bill' button.")
    payment_page.click_split_bill()


    logging.info("Clicking on 'Custom Pay' button.")
    payment_page.click_custom_pay()


    logging.info("Checking if confirm button is disabled.")
    assert payment_page.is_confirmbtn_disabled(), "Confirm button not disabled before adding an amount"

    logging.info("Setting custom amount to 20.")
    payment_page.set_custom_amount(20)

    logging.info("Checking if confirm button is enabled after adding an amount.")
    assert payment_page.is_confirmbtn_enabled(), "Confirm button not available after adding an amount"

    logging.info("Clicking on 'Confirm' button.")
    payment_page.clickConfirmBtn()
    logging.info("Confirmation clicked.")

    time.sleep(5)

    logging.info("Clicking on tip button for amount '10'.")
    payment_page.clickOnTipBtn("10")

    logging.info("Entering card information.")
    payment_page.enter_card_info(card_number, expiry_date, cvv)

    logging.info("Clicking on 'Pay' button.")
    payment_page.click_pay()

    logging.info("Validating payment success.")
    assert "Payment was successful!" == payment_page.getSuccessText()
    logging.info("Payment process completed successfully.")
