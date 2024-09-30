import time
import logging
import pytest
from setup.browser_setup import browser
from pages.payment_page import PaymentPage
from util.properties_reader import read_properties

def test_payment_process(browser):
    properties = read_properties('config.properties')

    url = properties['url']
    card_number = properties['card_number']
    expiry_date = properties['expiry_date']
    cvv = properties['cvv']

    print("Opening payment page: {url}")
    browser.get(url)

    payment_page = PaymentPage(browser)

    print("Clicking on 'Pay Bill' button.")
    payment_page.click_pay_bill()

    # Wait for progress bar loading
    time.sleep(10)

    print("Clicking on 'Split Bill' button.")
    payment_page.click_split_bill()

    print("Clicking on 'Custom Pay' button.")
    payment_page.click_custom_pay()

    print("Checking if confirm button is disabled.")
    assert payment_page.is_confirmbtn_disabled(), "Confirm button not disabled before adding an amount"

    print("Setting custom amount to 20.")
    payment_page.set_custom_amount(20)

    print("Checking if confirm button is enabled after adding an amount.")
    assert payment_page.is_confirmbtn_enabled(), "Confirm button not available after adding an amount"

    print("Clicking on 'Confirm' button.")
    payment_page.clickConfirmBtn()
    print("Confirmation clicked.")

    time.sleep(5)

    print("Clicking on tip button for amount '10'.")
    payment_page.clickOnTipBtn("10")

    print("Entering card information.")
    payment_page.enter_card_info(card_number, expiry_date, cvv)

    print(f"Clicking on 'Pay' button.")
    payment_page.click_pay()

    print("Validating payment success.")
    assert "Payment was successful!" == payment_page.getSuccessText()
    print("Payment process completed successfully.")
