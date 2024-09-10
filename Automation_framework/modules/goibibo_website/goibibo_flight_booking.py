from selenium.webdriver.common.by import By
from base.selenium_base import SeleniumBase
from resource.goibibo_website.flight_page_locators import *

class FlightBooking(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)

    def login_pop_up(self):
        self.click_element(close_pop_up)

    def select_one_way_button(self):
        self.click_element(one_way_button)

    def clicking_from_city(self):
        self.click_element(from_city)

    def enter_city_name(self,data):
        self.enter_text(data,from_city_input)

    def enter_to_name(self,data):
        self.enter_text(data,to_city_input)

    def select_city_from_list(self,city_name):
        locator = (By.XPATH,f"//span[text()='{city_name}']")
        self.click_element(locator)

    def select_departure_date(self,travel_date):
        self.click_element(Departure)
        date_locator = (By.XPATH,f"//div[contains(@aria-label ,'{travel_date}')]")
        self.click_element(date_locator)

    def travellers_class(self):
        self.click_element(Travellers_Class)
        for _ in range(2):
            self.click_element(Adults)
        for _ in range(2):
            self.click_element(Children)
        for _ in range(2):
            self.click_element(Infants)
        self.click_element(premium_economy)
        self.click_element(Done_button)

    def clicking_submit_button(self):
        self.click_element(SEARCH_FLIGHTS)