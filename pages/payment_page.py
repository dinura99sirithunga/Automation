from selenium.webdriver.common.by import By
from util.common import (
    wait_for_element_to_be_visible,
)


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    def click_pay_bill(self):
        pay_button = wait_for_element_to_be_visible(
            self.driver,
            (By.XPATH, "//button[@data-qa-id='landing-pay-now']")
        )
        pay_button.click()

    def click_split_bill(self):
        wait_for_element_to_be_visible(
            self.driver,
            (By.XPATH, "//button[@data-qa-id='billing-split-bill']")
        )
        split_button = self.driver.find_element(By.XPATH, "//button[@data-qa-id='billing-split-bill']")
        split_button.location_once_scrolled_into_view
        split_button.click()

    def click_custom_pay(self):
        customPayBtn = wait_for_element_to_be_visible(
            self.driver,
            (By.ID, "select-custom")
        )
        customPayBtn.click()

    def set_custom_amount(self, amount):
        setCustomAmountTxtbox = wait_for_element_to_be_visible(
            self.driver,
            (By.ID, "fullWidth")
        )
        setCustomAmountTxtbox.send_keys(amount)

    def is_confirmbtn_disabled(self):
        confirmbtn = wait_for_element_to_be_visible(
            self.driver,
            (By.ID, "split-bill")
        )
        return confirmbtn.get_attribute("disabled") is not None

    def is_confirmbtn_enabled(self):
        confirmbtn = wait_for_element_to_be_visible(
            self.driver,
            (By.ID, "split-bill")
        )
        return confirmbtn.is_enabled()

    def clickConfirmBtn(self):
        confimbtn = wait_for_element_to_be_visible(
            self.driver,
            (By.ID, "split-bill")
        )
        confimbtn.click()



    def clickOnTipBtn(self, amount):
        tipBtn = wait_for_element_to_be_visible(
            self.driver,
            (By.ID, "tip_" + amount)
        )
        tipBtn.click()

    def enter_card_info(self, card_number, expiry_date, cvv):
        self.driver.switch_to.frame("cardNumber")
        card_inputNumber = wait_for_element_to_be_visible(
            self.driver,
            (By.XPATH, "//input[@name='cardnumber']")
        )
        card_inputNumber.send_keys(card_number)
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame("expiryDate")
        expiry_inputExpDate = wait_for_element_to_be_visible(
            self.driver,
            (By.XPATH, "//input[@name='exp-date']")
        )
        expiry_inputExpDate.send_keys(expiry_date)
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame("cvv")
        cvv_input = wait_for_element_to_be_visible(
            self.driver,
            (By.XPATH, "//input[@name='cvc']")
        )
        cvv_input.send_keys(cvv)
        self.driver.switch_to.default_content()

    def click_pay(self):
        pay_final_button = wait_for_element_to_be_visible(
            self.driver,
            (By.ID, "checkout-action-btn")
        )
        pay_final_button.click()

    def getSuccessText(self):
        successTxt = wait_for_element_to_be_visible(
            self.driver,
            (By.XPATH, "//p[text()='Payment was successful!']")
        )
        return successTxt.text
