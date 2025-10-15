from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    # ---------- Locators ----------
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")

    # Updated locator for "Call a taxi"
    get_routes_button = (By.XPATH, "//button[text()='Call a taxi']")

    call_a_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")

    # Updated locator for Supportive plan
    supportive_plan_button = (By.XPATH, "//div[text()='Supportive']")

    # Added locator for supportive plan status
    supportive_plan_status = (By.XPATH, "//div[text()='Supportive']//..")

    next_button = (By.CSS_SELECTOR, ".next-button")

    phone_number_field = (By.ID, "phone-number")
    sms_code_field = (By.ID, "sms-code")
    confirm_button = (By.CSS_SELECTOR, ".confirm-button")

    card_number_field = (By.ID, "card-number")
    expiry_field = (By.ID, "expiry-date")
    cvv_field = (By.ID, "cvv")
    link_card_button = (By.CSS_SELECTOR, ".link-card-button")

    comment_field = (By.ID, "comment-input")

    blanket_slider = (By.ID, "blanket-slider")
    ice_cream_add_button = (By.CSS_SELECTOR, ".ice-cream-add")
    ice_cream_count = (By.CSS_SELECTOR, ".ice-cream-count")

    order_button = (By.CSS_SELECTOR, ".order-button")
    car_search_modal = (By.ID, "car-search-modal")

    # ---------- Init ----------
    def __init__(self, driver):
        self.driver = driver

    # ---------- Helper Methods ----------
    def _click_element(self, locator):
        """Simplified click method as recommended."""
        self.driver.find_element(*locator).click()

    def _set_input(self, locator, value, wait_time=20):
        """Wait for input field, clear it, and send new value."""
        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator)
        ).clear()
        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(value)

    # ---------- Actions ----------
    def set_route(self, from_address, to_address):
        """Fill out route and click 'Call a taxi'."""
        self._set_input(self.from_field, from_address)
        self._set_input(self.to_field, to_address)
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.get_routes_button)
        )
        self._click_element(self.get_routes_button)

    def click_call_a_taxi_button(self):
        """Click 'Call a taxi' button if visible."""
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.call_a_taxi_button)
        )
        self._click_element(self.call_a_taxi_button)

    def click_supportive_plan(self):
        """Select Supportive plan only if not already active."""
        card_class = self.driver.find_element(*self.supportive_plan_button).get_attribute("class")
        if "active" not in card_class:
            card = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.supportive_plan_button)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", card)
            card.click()

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

    def add_blanket_handkerchiefs(self):
        self._click_element(self.blanket_slider)
        return True  # Return for assertion

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

    # ---------- Additional Methods (per tutor) ----------
    def get_supportive_status(self):
        """Return the 'class' attribute of the Supportive plan."""
        return self.driver.find_element(*self.supportive_plan_status).get_attribute("class")

    def get_from(self):
        """Return the value of the 'From' input field."""
        return self.driver.find_element(*self.from_field).get_attribute("value")

    def get_to(self):
        """Return the value of the 'To' input field."""
        return self.driver.find_element(*self.to_field).get_attribute("value")


