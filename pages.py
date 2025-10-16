from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Locators ---
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    get_routes_button = (By.XPATH, "//button[text()='Call a taxi']")
    supportive_plan_button = (By.XPATH, "//div[text()='Supportive']")
    supportive_plan_status = (By.XPATH, "//div[text()='Supportive']//..")
    phone_field = (By.ID, "phone")
    next_button = (By.XPATH, "//button[text()='Next']")
    code_input = (By.ID, "code")
    payment_method_button = (By.XPATH, "//div[text()='Payment method']")
    add_card_button = (By.XPATH, "//button[text()='Add card']")
    card_number_field = (By.ID, "card_number")
    card_code_field = (By.ID, "card_code")
    link_card_button = (By.XPATH, "//button[text()='Link']")
    confirm_button = (By.XPATH, "//button[text()='Confirm']")

    # --- Utility methods ---
    def _click_element(self, locator):
        """Simplified element click method per forum feedback"""
        self.driver.find_element(*locator).click()

    def _enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    # --- Page actions ---
    def set_route(self, from_address, to_address):
        self._enter_text(self.from_field, from_address)
        self._enter_text(self.to_field, to_address)
        self._click_element(self.get_routes_button)

    def select_supportive_plan(self):
        self._click_element(self.supportive_plan_button)

    def get_supportive_status(self):
        """Get the 'class' attribute of the Supportive plan container"""
        return self.driver.find_element(*self.supportive_plan_status).get_attribute("class")

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_attribute("value")

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_attribute("value")

    def enter_phone_number(self, phone):
        self._enter_text(self.phone_field, phone)
        self._click_element(self.next_button)

    def enter_code(self, code):
        self._enter_text(self.code_input, code)
        self._click_element(self.next_button)

    def open_payment_method(self):
        self._click_element(self.payment_method_button)

    def add_card(self, card_number, card_code):
        self._click_element(self.add_card_button)
        self._enter_text(self.card_number_field, card_number)
        self._enter_text(self.card_code_field, card_code)
        self._click_element(self.link_card_button)
        self._click_element(self.confirm_button)


