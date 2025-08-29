from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

        # Route fields
        self.from_field = (By.ID, "from")
        self.to_field = (By.ID, "to")

        # Buttons
        self.get_routes_button = (By.CLASS_NAME, "button.round")
        self.call_a_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")
        self.supportive_plan_button = (By.CSS_SELECTOR, ".supportive-plan")  # Update selector
        self.next_button = (By.CSS_SELECTOR, ".next-button")                 # Update selector

        # Phone field
        self.phone_number_field = (By.ID, "phone-number")

    # ---------- Actions ----------

    def set_route(self, from_address, to_address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.get_routes_button)
        ).click()

    def click_call_a_taxi_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.call_a_taxi_button)
        ).click()

    def click_supportive_plan(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.supportive_plan_button)
        ).click()

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.next_button)
        ).click()

    def set_phone_number(self, phone_number):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.phone_number_field)
        ).send_keys(phone_number)




