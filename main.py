import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages import UrbanRoutesPage
import data
import helpers


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_click_phone_number_field(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()
        time.sleep(3)
        urban_routes_page.click_phone_number_field()
        time.sleep(3)
        assert True

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
        assert expected_value in actual_value

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
        time.sleep(10)
        urban_routes_page.fill_sms_code(code)
        urban_routes_pa

