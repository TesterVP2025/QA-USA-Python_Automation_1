import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages import UrbanRoutesPage
from data import URBAN_ROUTES_URL, ADDRESS_TO, PHONE_NUMBER, CARD_NUMBER, CARD_CODE, MESSAGE_FOR_DRIVER


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get(URBAN_ROUTES_URL)
    yield driver
    driver.quit()


class TestUrbanRoutes:

    def test_set_route(self, setup):
        driver = setup
        page = UrbanRoutesPage(driver)

        page.set_route("Central Park", ADDRESS_TO)
        from_value = page.get_from()
        to_value = page.get_to()

        assert from_value == "Central Park", "From address did not set correctly"
        assert to_value == ADDRESS_TO, "To address did not set correctly"

    def test_select_plan(self, setup):
        driver = setup
        page = UrbanRoutesPage(driver)

        page.set_route("Central Park", ADDRESS_TO)
        page.click_call_a_taxi_button()
        page.click_supportive_plan()

        supportive_status = page.get_supportive_status()
        assert "active" in supportive_status, "Supportive plan was not selected"

    def test_enter_phone_number(self, setup):
        driver = setup
        page = UrbanRoutesPage(driver)

        page.set_route("Central Park", ADDRESS_TO)
        page.click_call_a_taxi_button()
        page.click_supportive_plan()
        page.click_next_button()
        page.set_phone_number(PHONE_NUMBER)
        page.set_sms_code("1234")

        assert True, "Phone number flow failed"

    def test_add_card(self, setup):
        driver = setup
        page = UrbanRoutesPage(driver)

        page.set_route("Central Park", ADDRESS_TO)
        page.click_call_a_taxi_button()
        page.click_supportive_plan()
        page.click_next_button()
        page.set_phone_number(PHONE_NUMBER)
        page.set_sms_code("1234")
        page.add_card(CARD_NUMBER, "12/25", CARD_CODE)

        assert True, "Failed to add card"

    def test_leave_comment(self, setup):
        driver = setup
        page = UrbanRoutesPage(driver)

        page.set_route("Central Park", ADDRESS_TO)
        page.click_call_a_taxi_button()
        page.click_supportive_plan()
        page.click_next_button()
        page.set_phone_number(PHONE_NUMBER)
        page.set_sms_code("1234")
        page.leave_comment(MESSAGE_FOR_DRIVER)

        assert True, "Failed to leave a comment"

    def test_add_blanket_and_ice_cream(self, setup):
        driver = setup
        page = UrbanRoutesPage(driver)

        page.set_route("Central Park", ADDRESS_TO)
        page.click_call_a_taxi_button()
        page.click_supportive_plan()
        page.click_next_button()
        page.set_phone_number(PHONE_NUMBER)
        page.set_sms_code("1234")
        page.add_blanket_handkerchiefs()
        page.add_ice_cream(2)
        count = page.get_ice_cream_count()

        assert count == 2, f"Expected 2 ice creams, got {count}"

    def test_order_taxi(self, setup):
        driver = setup
        page = UrbanRoutesPage(driver)

        page.set_route("Central Park", ADDRESS_TO)
        page.click_call_a_taxi_button()
        page.click_supportive_plan()
        page.click_next_button()
        page.set_phone_number(PHONE_NUMBER)
        page.set_sms_code("1234")
        page.add_blanket_handkerchiefs()
        page.add_ice_cream(1)
        page.click_order_button()

        assert page.is_car_search_modal_displayed(), "Car search modal did not appear"
