import time

import pytest
from modules.goibibo_website.goibibo_flight_booking import FlightBooking
from resource.goibibo_website.flight_page_locators import *
@pytest.mark.usefixtures("get_driver_goibibo")
class TestGoibiboFlight:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.gof = FlightBooking(self.driver)

    def test_one_way_flight_booking(self):
        self.gof.login_pop_up()
        self.gof.select_one_way_button()
        self.gof.clicking_from_city()
        self.gof.enter_city_name(from_city1)
        self.gof.select_city_from_list(from_city1)
        self.gof.enter_to_name(to_city1)
        self.gof.select_city_from_list(to_city1)
        self.gof.select_departure_date(date)
        self.gof.travellers_class()
        self.gof.clicking_submit_button()
        time.sleep(20)
