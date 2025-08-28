from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    get_routes_button = (By.CLASS_NAME, "button.round")
    phone_number = (By.ID, "phone")
    next_button = (By.CLASS_NAME, "button.full")
    confirm_button = (By.CLASS_NAME, "button.confirm")
    enter_sms_code = (By.ID, "code")
    click_payment_method = (By.XPATH, "//div[@class='pp-text']")
    click_add_card = (By.CLASS_NAME, "pp-plus")
    enter_card_number = (By.ID, "number")
    enter_card_code = (By.ID, "code")
    click_outside_box = (By.CLASS_NAME, "payment-title")
    card_link_button = (By.CLASS_NAME, "pp-button")
    payment_close = (By.CLASS_NAME, "pp-close")
    card_confirm = (By.CLASS_NAME, "pp-value-text")
    blanket_and_handkerchiefs = (By.CLASS_NAME, "r-sw")
    order_ice_cream = (By.CLASS_NAME, "r-ice")
    message_to_driver = (By.ID, "comment")
    click_arrow_dropdown = (By.CLASS_NAME, "arrow")
    order_button = (By.CLASS_NAME, "smart-button")
    car_modal = (By.CLASS_NAME, "car")
    confirm_message = (By.CLASS_NAME, "order-confirm")

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, location):
        self.driver.find_element(*self.from_field).send_keys(location)

    def enter_to_location(self, location):
        self.driver.find_element(*self.to_field).send_keys(location)

    def click_get_routes(self):
        self.driver.find_element(*self.get_routes_button).click()

    def enter_phone_number(self, phone):
        self.driver.find_element(*self.phone_number).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    def enter_sms_code(self, code):
        self.driver.find_element(*self.enter_sms_code).send_keys(code)

    def click_payment_method(self):
        self.driver.find_element(*self.click_payment_method).click()

    def click_add_card(self):
        self.driver.find_element(*self.click_add_card).click()

    def enter_card_number(self, number):
        self.driver.find_element(*self.enter_card_number).send_keys(number)

    def enter_card_code(self, code):
        self.driver.find_element(*self.enter_card_code).send_keys(code)

    def click_outside_box(self):
        self.driver.find_element(*self.click_outside_box).click()

    def click_card_link_button(self):
        self.driver.find_element(*self.card_link_button).click()

    def click_payment_close(self):
        self.driver.find_element(*self.payment_close).click()

    def get_card_confirm_text(self):
        return self.driver.find_element(*self.card_confirm).text

    def toggle_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.blanket_and_handkerchiefs).click()

    def order_ice_cream(self):
        self.driver.find_element(*self.order_ice_cream).click()

    def enter_message_to_driver(self, message):
        self.driver.find_element(*self.message_to_driver).send_keys(message)

    def click_arrow_dropdown(self):
        self.driver.find_element(*self.click_arrow_dropdown).click()

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def is_car_modal_displayed(self):
        return self.driver.find_element(*self.car_modal).is_displayed()

    def get_confirm_message_text(self):
        return self.driver.find_element(*self.confirm_message).text 




