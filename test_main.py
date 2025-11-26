import pytest
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage
import data
import helpers


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # Enable performance logs for retrieving SMS code
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

        # Ensure container is reachable
        helpers.is_url_reachable(data.URBAN_ROUTES_URL)

    def test_set_route(self):
        """Verify route fields are set correctly"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert page.get_from() == data.ADDRESS_FROM
        assert page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        """Verify Supportive plan selection"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()

        assert "active" in page.get_supportive_status()

    def test_fill_phone_number(self):
        """Verify phone login flow"""
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
        """Verify card is added successfully"""
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
        """Verify blanket & handkerchiefs can be added"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()

        assert page.add_blanket_handkerchiefs() is True

    def test_order_2_ice_creams(self):
        """Verify ordering ice cream increments correctly"""
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()

        page.add_ice_cream(2)
        assert page.get_ice_cream_count() == 2

    # ⭐⭐ TEMPORARY VERSION SO I CAN FIX YOUR LOCATORS ⭐⭐
    # DO NOT REMOVE THIS UNTIL I TELL YOU TO.
    def test_car_search_modal_appears(self):
        """TEMP: Freeze after opening phone modal + dump HTML"""

        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        # Route + Supportive Plan
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_plan()

        # Open phone modal
        page.open_phone_modal()

        # ⭐ TEMP DEBUG — we need the HTML for the phone input
        time.sleep(3)
        html = self.driver.page_source

        print("\n\n========== PAGE SOURCE START ==========\n\n")
        print(html)
        print("\n\n========== PAGE SOURCE END ==========\n\n")

        # Freeze browser so modal stays open
        time.sleep(9999)

        # Once we fix locators, we will restore:
        # page.enter_phone_number(data.PHONE_NUMBER)
        # page.click_next_button()
        # code = helpers.retrieve_phone_code(self.driver)
        # page.enter_code(code)
        # page.click_confirm_button()
        # page.leave_comment(data.MESSAGE_FOR_DRIVER)
        # page.click_order_button()
        # assert page.is_car_search_modal_displayed() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
