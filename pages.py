from selenium.webdriver import support
from selenium.webdriver.common.by import By
import data
import helpers
from selenium.webdriver import Keys

from data import CARD_NUMBER, CARD_CODE
from helpers import retrieve_phone_code
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    supportive_plan_card = (By.XPATH, '//div[contains(text(), "Supportive")]')
    supportive_plan_card_parent = (By.XPATH, '//div[contains(text(), "Supportive")]//..')
    active_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    call_taxi_button = (By.XPATH, '//button[contains(text(), "Call a taxi:)]')
    LINK_BUTTON = (By.XPATH, '//div[@class="pp-buttons"]//button[@type="submit"]')
    PAYMENT_CLOSE_BUTTON = (By.XPATH,
                            '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')

    def __init__(self, driver):
        self.PHONE_NUMBER_confirm_button = driver
        self.PHONE_NUMBER_next_button = driver
        self.PHONE_NUMBER_input = driver
        self.CARD_CODE = driver
        self.CARD_NUMBER = driver
        self.payment_method_button = driver
        self.driver = driver

    def set_from(self, from_address):
        from_field = self.driver.find_element(*self.from_field)
        from_field.send_keys(from_address)

    def set_to(self, to_address):
        to_field = self.driver.find_element(*self.to_field)
        to_field.send_keys(to_address)
