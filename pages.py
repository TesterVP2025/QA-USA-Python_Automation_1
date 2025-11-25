from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import helpers


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===============================================================
    #                       LOCATORS (ALL CAPS)
    # ===============================================================

    # Route fields
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(),'Call a taxi')]")

    # Supportive plan
    SUPPORTIVE_PLAN_BUTTON = (By.XPATH, "//div[text()='Supportive']")
    SUPPORTIVE_PLAN_STATUS = (By.XPATH, "//div[text()='Supportive']/..")

    # Phone modal (based on what we SEE on your UI)
    PHONE_MODAL_BUTTON = (By.CLASS_NAME, "np-text")
    # input with placeholder "Phone number"
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='Phone number']")
    # any element whose visible text is exactly "Next"
    NEXT_BUTTON = (By.XPATH, "//*[normalize-space(text())='Next']")
    # 4-digit code field – most builds still use id="code"
    CODE_INPUT = (By.ID, "code")
    # any element whose visible text is exactly "Confirm"
    CONFIRM_BUTTON = (By.XPATH, "//*[normalize-space(text())='Confirm']")

    # Payment
    PAYMENT_METHOD_BUTTON = (By.CSS_SELECTOR, "[data-test='payment']")
    ADD_CARD_BUTTON = (By.CSS_SELECTOR, "[data-test='add-card']")
    CARD_NUMBER_FIELD = (By.ID, "number")
    CARD_CODE_FIELD = (By.ID, "code")
    LINK_CARD_BUTTON = (By.CSS_SELECTOR, "[data-test='link-card']")
    CARD_TEXT_LABEL = (By.CSS_SELECTOR, "[data-test='card-info']")

    # Comment
    COMMENT_FIELD = (By.ID, "comment")

    # Blanket/handkerchiefs
    BLANKET_CHECKBOX = (By.CSS_SELECTOR, "[data-test='blanket']")

    # Ice cream
    ICE_CREAM_PLUS_BUTTON = (By.CSS_SELECTOR, "[data-test='counter-plus']")
    ICE_CREAM_COUNTER = (By.CSS_SELECTOR, "[data-test='counter-value']")

    # Order + search modal
    ORDER_BUTTON = (By.CSS_SELECTOR, "[data-test='order']")
    CAR_SEARCH_MODAL = (By.CSS_SELECTOR, "[data-test='order-body']")

    # ===============================================================
    #                       UTILITY METHODS
    # ===============================================================

    def _click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def _type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    # ===============================================================
    #                       CORE ACTIONS
    # ===============================================================

    def set_route(self, from_address, to_address):
        self._type(self.FROM_FIELD, from_address)
        self._type(self.TO_FIELD, to_address)
        self._click(self.CALL_TAXI_BUTTON)

    def click_supportive_plan(self):
        self._click(self.SUPPORTIVE_PLAN_BUTTON)

    def get_supportive_status(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_STATUS).get_attribute("class")

    def get_from(self):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute("value")

    def get_to(self):
        return self.driver.find_element(*self.TO_FIELD).get_attribute("value")

    # ===============================================================
    #                     PHONE LOGIN FLOW
    # ===============================================================

    def open_phone_modal(self):
        self._click(self.PHONE_MODAL_BUTTON)

    def enter_phone_number(self, phone):
        self._type(self.PHONE_INPUT, phone)

    def click_next_button(self):
        self._click(self.NEXT_BUTTON)

    def enter_code(self, code):
        self._type(self.CODE_INPUT, code)

    def click_confirm_button(self):
        self._click(self.CONFIRM_BUTTON)

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_INPUT).get_attribute("value")

    # ===============================================================
    #                         PAYMENT
    # ===============================================================

    def open_payment_method(self):
        self._click(self.PAYMENT_METHOD_BUTTON)

    def add_card(self, card_number, card_code):
        self._click(self.ADD_CARD_BUTTON)
        self._type(self.CARD_NUMBER_FIELD, card_number)
        self._type(self.CARD_CODE_FIELD, card_code)
        self.driver.find_element(*self.CARD_CODE_FIELD).send_keys(Keys.TAB)
        self._click(self.LINK_CARD_BUTTON)

    def get_card_number(self):
        return self.driver.find_element(*self.CARD_TEXT_LABEL).text

    # ===============================================================
    #                       COMMENT
    # ===============================================================

    def leave_comment(self, message):
        self._type(self.COMMENT_FIELD, message)

    def get_comment_value(self):
        return self.driver.find_element(*self.COMMENT_FIELD).get_attribute("value")

    # ===============================================================
    #                   BLANKET & HANDKERCHIEFS
    # ===============================================================

    def add_blanket_handkerchiefs(self):
        self._click(self.BLANKET_CHECKBOX)
        return self.driver.find_element(*self.BLANKET_CHECKBOX).get_property("checked")

    # ===============================================================
    #                         ICE CREAM
    # ===============================================================

    def add_ice_cream(self, count):
        for _ in range(count):
            self._click(self.ICE_CREAM_PLUS_BUTTON)

    def get_ice_cream_count(self):
        return int(self.driver.find_element(*self.ICE_CREAM_COUNTER).text)

    # ===============================================================
    #                           ORDER
    # ===============================================================

    def click_order_button(self):
        self._click(self.ORDER_BUTTON)

    def is_car_search_modal_displayed(self):
        try:
            modal = self.wait.until(EC.visibility_of_element_located(self.CAR_SEARCH_MODAL))
            return modal.is_displayed()
        except:
            return False
