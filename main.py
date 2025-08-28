import time
import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    def test_click_phone_number_field(self):
        pass

    def test_enter_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()
        time.sleep(3)
        urban_routes_page.click_phone_number_field()
        time.sleep(3)
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(3)
        urban_routes_page.click_next_button()
        actual_value = urban_routes_page.get_fill_phone_number()
        expected_value = '+1 123 123 12 12'
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_next_button(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()
        time.sleep(3)
        urban_routes_page.click_phone_number_field()
        time.sleep(3)
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(3)
        urban_routes_page.click_next_button()
        assert urban_routes_page.click_next_button

    def test_set_phone(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()
        time.sleep(3)
        urban_routes_page.click_phone_number_field()
        time.sleep(3)
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(3)
        urban_routes_page.click_next_button()
        code = helpers.retrieve_phone_code(self.driver)
        print(f"Retrieved phone code: {code}")
        time.sleep(10)
        urban_routes_page.fill_sms_code(code)
        urban_routes_page.click_confirm_button()
        # Add a wait to ensure the element is loaded
        time.sleep(2)
        actual_value = urban_routes_page.get_phone_value()
        expected_value = '+1 123 123 12 12'
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_payment_method(self):
        self.driver.get(data.URBAN_ROBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()
        time.sleep(3)
        urban_routes_page.click_phone_number_field()
        time.sleep(3)
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        time.sleep(3)
        urban_routes_page.click_next_button()
        code = helpers.retrieve_phone_code(self.driver)
        print(f"Retrieved phone code: {code}")
        time.sleep(10)
        urban_routes_page.fill_sms_code(code)
        urban_routes_page.click_confirm_button()
        # Add a wait to ensure the element is loaded
        time.sleep(2)
        urban_routes_page.click_payment_button()

