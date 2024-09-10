import os
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from utilites.utility_tools import CommonUtils


class SeleniumBase:

    def __init__(self,driver,timeout=20):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver,self.timeout)
        self.utils = CommonUtils()
        self.logs_folder_path = self.utils.create_unique_folder_logs()
        self.log = logging.getLogger(__name__)


    def take_screenshot(self,filename):
        filepath = os.path.join(self.logs_folder_path,f'{filename}_{self.utils.get_unique_name()}.png')
        self.log.info(f"screenshot: {filepath }")
        self.driver.save_screenshot(filepath)


    def get_element(self,locator):
        try:
            element = self.wait.until(ec.presence_of_element_located(locator))
            self.log.info(f"found element with locator: {locator}")
            return element
        except Exception as e:
            self.log.info(f"{locator} {e}")
            self.take_screenshot(filename="element not found")

    def get_elements(self,locator):
        try:
            elements = self.wait.until(ec.presence_of_all_elements_located(locator))
            self.log.info(f"found element with locator: {locator}")
            return elements
        except Exception as e:
            self.log.info(f"{locator}{e}")
            self.take_screenshot(filename="element not found")

    def click_element(self,locator):
        try:
            element = self.get_element(locator)
            self.log.info(f"clicking to the element: {locator}")
            element.click()
        except Exception as e:
            self.log.info(f"{locator}{e}")
            self.take_screenshot(filename="element not found")
            raise

    def enter_text(self,data,locator):
        try:
            element = self.get_element(locator)
            self.log.info(f'enter value: {data} to the element: {locator}')
            element.send_keys(data)
        except Exception as e:
            self.log.info(f"{locator}{e}")
            self.take_screenshot(filename="element not found")
            raise

    def get_text(self,locator):
        try:
            element = self.get_element(locator)
            self.log.info(f"getting text from the element: {locator}")
            return element.text
        except Exception as e:
            self.log.info(f"{locator}{e}")
            self.take_screenshot(filename="element not found")
            raise

    def select_value_from_dropdown(self,value,locater):
        try:
            element = self.get_element(locater)
            select = Select(element)
            self.log.info(f"selecting value: {value} from the dropdown: {locater}")
            select.select_by_visible_text(value)
        except Exception as e:
            self.log.info(f"{locater}{e}")
            self.take_screenshot(filename="element not found")
            raise

    def move_the_element(self,locator):
        try:
            element = self.get_element(locator)
            self.log.info(f"Cursor placed on element:{locator}")
            action= ActionChains(self.driver)
            action.move_to_element(element)
            action.perform()
        except Exception as e:
            self.log.info(f"{locator}{e}")
            self.take_screenshot(filename="element not found")
            raise



