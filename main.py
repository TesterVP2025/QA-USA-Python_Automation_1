import pytest
from selenium import webdriver
from pages import UrbanRoutesPage
import data
import helpers
import time

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        from_value = self.driver.find_element(*page.from_field).get_attribute("value")
        to_value = self.driver.find_element(*page.to_field).get_attribute("value")
        assert from_value == data.ADDRESS_FROM
        assert to_value == data.ADDRESS_TO

    def test_select_plan(self):
        page = UrbanRoutesPage(self.driver)
        page.click_call_a_taxi_button()
        page.click_supportive_plan()
        selected_class = self.driver.find_element(*page.supportive_plan_button).get_attribute("class")
        assert "active" in selected_class

    def test_fill_phone_number(self):
        page = UrbanRoutesPage(self.driver)
        page.set_phone_number(data.PHONE_NUMBER)
        sms_code = helpers.retrieve_phone_code(data.PHONE_NUMBER)
        page.set_phone_number(sms_code)
        phone_value = self.driver.find_element(*page.phone_number_field).get_attribute("value")
        assert phone_value == data.PHONE_NUMBER

    def test_fill_card(self):
        page = UrbanRoutesPage(self.driver)
        page.fill_card_info(data.CARD_NUMBER, data.CARD_EXPIRY, data.CARD_CVV)
        payment_text = self.driver.find_element(*page.payment_method_display).text
        assert "Card" in payment_text

    def test_comment_for_driver(self):
        page = UrbanRoutesPage(self.driver)
        page.fill_comment(data.DRIVER_COMMENT)
        comment_value = self.driver.find_element(*page.comment_field).get_attribute("value")
        assert comment_value == data.DRIVER_COMMENT

    def test_order_blanket_and_handkerchiefs(self):
        page = UrbanRoutesPage(self.driver)
        checked = page.add_blanket_handkerchiefs()
        assert checked is True

    def test_order_2_ice_creams(self):
        page = UrbanRoutesPage(self.driver)
        page.add_ice_cream(2)
        ice_count = page.get_ice_cream_count()
        assert ice_count == 2

    def test_car_search_model_appears(self):
        page = UrbanRoutesPage(self.driver)
        page.click_order_button()
        assert page.car_search_modal_is_displayed() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

