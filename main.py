import data

class TestUrbanRoutes:

    def test_set_route(self):
        # Add in S8
        print("function created for set route")
        if data.is_url_reachable():
            print("Server is running.")
        else:
            print("Server is NOT reachable.")
        pass

    def test_select_plan(self):
        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Add in S8
        print("function created for order 2 ice creams")
        ice_cream_order = "vanilla"
        for count in range(2):
            # Add in S8
            print(f"Ordering ice cream #{count + 1}: {ice_cream_order}")
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car search model appears")
        pass
print('test')
