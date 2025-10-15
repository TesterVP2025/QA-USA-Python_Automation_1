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
        from_value = page.get_from()
        to_value = page.get_to()
        assert from_value == data.ADDRESS_FROM
        assert to_value == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()
        selected_class = page.get_supportive_status()
        assert "active" in selected_class

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()
        page.set_phone_number(data.PHONE_NUMBER)
        helpers.complete_phone_login(page, self.driver)
        phone_value = self.driver.find_element(*page.phone_number_field).get_attribute("value")
        assert data.PHONE_NUMBER in phone_value

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()
        page.add_card(data.CARD_NUMBER, data.CARD_EXPIRY, data.CARD_CODE)
        payment_text = self.driver.find_element(*page.link_card_button).text
        assert "Card" in payment_text

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()
        page.leave_comment(data.MESSAGE_FOR_DRIVER)
        comment_value = self.driver.find_element(*page.comment_field).get_attribute("value")
        assert comment_value == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()
        checked = page.add_blanket_handkerchiefs()
        assert checked is True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()
        page.add_ice_cream(2)
        ice_count = page.get_ice_cream_count()
        assert ice_count == 2

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()
        page.click_order_button()
        assert page.is_car_search_modal_displayed() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

