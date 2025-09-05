from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

        # Route fields
        self.from_field = (By.ID, "from")
        self.to_field = (By.ID, "to")

        # Buttons
        self.get_routes_button = (By.CLASS_NAME, "button.round")
        self.call_a_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")
        self.supportive_plan_button = (By.CSS_SELECTOR, ".supportive-plan")
        self.next_button = (By.CSS_SELECTOR, ".next-button")

        # Phone field
        self.phone_number_field = (By.ID, "phone-number")
        self.sms_code_field = (By.ID, "sms-code")  # make sure your HTML matches
        self.confirm_button = (By.CSS_SELECTOR, ".confirm-button")

        # Payment fields
        self.card_number_field = (By.ID, "card-number")
        self.expiry_field = (By.ID, "expiry-date")
        self.cvv_field = (By.ID, "cvv")
        self.link_card_button = (By.CSS_SELECTOR, ".link-card-button")

        # Comment field
        self.comment_field = (By.ID, "comment-input")

        # Ice cream & blanket sliders
        self.blanket_slider = (By.ID, "blanket-slider")
        self.ice_cream_add_button = (By.CSS_SELECTOR, ".ice-cream-add")
        self.ice_cream_count = (By.CSS_SELECTOR, ".ice-cream-count")

        # Order button & modal
        self.order_button = (By.CSS_SELECTOR, ".order-button")
        self.car_search_modal = (By.ID, "car-search-modal")

    # ---------- Helper methods ----------
    def _click_element(self, locator, retries=3, wait_time=20):
        # Handle iframe if present
        switched = False
        try:
            iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe")
            self.driver.switch_to.frame(iframe)
            switched = True
        except:
            pass

        for _ in range(retries):
            try:
                WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable(locator)
                ).click()
                break
            except TimeoutException:
                self.driver.refresh()
                time.sleep(3)
        else:
            raise TimeoutException(f"Element not clickable: {locator}")

        if switched:
            self.driver.switch_to.default_content()

    def _set_input(self, locator, value, wait_time=20):
        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator)
        ).clear()
        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(value)

    # ---------- Actions ----------
    def set_route(self, from_address, to_address):
        self._set_input(self.from_field, from_address)
        self._set_input(self.to_field, to_address)
        self._click_element(self.get_routes_button)

    def click_call_a_taxi_button(self):
        self._click_element(self.call_a_taxi_button)

    def click_supportive_plan(self):
        self._click_element(self.supportive_plan_button)

    def click_next_button(self):
        self._click_element(self.next_button)

    def set_phone_number(self, phone_number):
        self._set_input(self.phone_number_field, phone_number)

    def set_sms_code(self, code):
        self._set_input(self.sms_code_field, code)
        self._click_element(self.confirm_button)

    def add_card(self, number, expiry, cvv):
        self._set_input(self.card_number_field, number)
        self._set_input(self.expiry_field, expiry)
        self._set_input(self.cvv_field, cvv)
        self._click_element(self.link_card_button)

    def leave_comment(self, comment_text):
        self._set_input(self.comment_field, comment_text)

    def order_blanket_and_handkerchiefs(self):
        self._click_element(self.blanket_slider)

    def add_ice_cream(self, quantity=1):
        for _ in range(quantity):
            self._click_element(self.ice_cream_add_button)

    def get_ice_cream_count(self):
        return int(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ice_cream_count)
        ).text)

    def click_order_button(self):
        self._click_element(self.order_button)

    def is_car_search_modal_displayed(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.car_search_modal)
        ).is_displayed()


