from helpers import is_url_reachable
from data import URBAN_ROUTES_URL

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if is_url_reachable(URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

    def test_set_route(self):
        print("function created for set route")
        # Your test code here

    def test_select_plan(self):
        print("function created for select plan")
        # Your test code here

    def test_fill_phone_number(self):
        print("function created for fill phone number")
        # Your test code here

    def test_fill_card(self):
        print("function created for fill card")
        # Your test code here

    def test_comment_for_driver(self):
        print("function created for comment for driver")
        # Your test code here

    def test_order_blanket_and_handkerchiefs(self):
        print("function created for order blanket and handkerchiefs")
        # Your test code here

    def test_order_2_ice_creams(self):
        # Your test code here
        print("function created for order 2 ice creams")

    def test_car_search_model_appears(self):
        print("function created for car search model appears")
        # Your test code here


