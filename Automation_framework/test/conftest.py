from selenium import webdriver
import pytest
from resource.goibibo_website.flight_page_locators import *

@pytest.fixture(scope="class")
def get_driver_goibibo(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(goibibo_url)
    request.cls.driver = driver
    yield
    driver.close()