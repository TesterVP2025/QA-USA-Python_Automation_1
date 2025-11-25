import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages import UrbanRoutesPage
import data
import helpers


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # Enable performance logs for retrieving SMS code
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

        helpers.is_url_reachable(data.URBAN_ROUTES_URL)

    def test_set_route(self):
        """Verify route fields are set correctly"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        from_value = page.get_from()
        to_value = page.get_to()

        assert from_value == data.ADDRESS_FROM
        assert to_value == data.ADDRESS_TO

    def test_select_plan(self):
        """Verify Supportive plan selection"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()

        selected_class = page.get_supportive_status()
        assert "active" in selected_class

    def test_fill_phone_number(self):
        """Verify full phone login flow"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()

        page.open_phone_modal()
        page.enter_phone_number(data.PHONE_NUMBER)
        page.click_next_button()

        code = helpers.retrieve_phone_code(self.driver)
        page.enter_code(code)
        page.click_confirm_button()

        assert page.get_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        """Verify card is added and linked"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()

        page.open_payment_method()
        page.add_card(data.CARD_NUMBER, data.CARD_CODE)
        assert "Card" in page.get_card_number()

    def test_comment_for_driver(self):
        """Verify comment can be entered"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()

        page.leave_comment(data.MESSAGE_FOR_DRIVER)
        assert page.get_comment_value() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        """Verify blanket & handkerchiefs selection"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()

        checked = page.add_blanket_handkerchiefs()
        assert checked is True

    def test_order_2_ice_creams(self):
        """Verify adding two ice creams"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()

        page.add_ice_cream(2)
        assert page.get_ice_cream_count() == 2

    def test_car_search_modal_appears(self):
        """Verify modal appears after order"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()

        page.open_phone_modal()
        page.enter_phone_number(data.PHONE_NUMBER)
        page.click_next_button()

        code = helpers.retrieve_phone_code(self.driver)
        page.enter_code(code)
        page.click_confirm_button()

        page.leave_comment(data.MESSAGE_FOR_DRIVER)
        page.click_order_button()

        assert page.is_car_search_modal_displayed() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
