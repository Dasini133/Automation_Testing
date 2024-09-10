from selenium.webdriver.common.by import By

close_pop_up = (By.XPATH,"//span[@role='presentation']")
round_trip = (By.XPATH,"//p[text()='Round-trip']")
one_way_button =(By.XPATH,"//p[text()='One-way']")
multi_city_button = (By.XPATH,"//p[text()='Multi-city']")


from_city=(By.XPATH,"//span[text()='From']")
from_city_input=(By.XPATH,"//input[@type='text']")
select_city_list=(By.XPATH,"//span[text()='Bengaluru, India']")
to_city_input=(By.XPATH,"//input[@type='text']")


Departure = (By.XPATH,"//span[text()='Departure']")
calendar_date=(By.XPATH,"//div[contains(@aria-label ,'Sep 16')]")

Travellers_Class =(By.XPATH,"//span[text()='Travellers & Class']")
Adults=(By.XPATH,"//p[text()='Adults']//following::span[3]")
Children=(By.XPATH,"//p[text()='Children']//following::span[3]")
Infants=(By.XPATH,"//p[text()='Infants']//following::span[3]")
premium_economy=(By.XPATH,"//li[text()='premium economy']")
Done_button=(By.XPATH,"//a[text()='Done']")
SEARCH_FLIGHTS=(By.XPATH,"//span[text()='SEARCH FLIGHTS']")

from_city1="Bengaluru, India"
to_city1="Goa - Dabolim Airport, India"

date="Sep 16"

goibibo_url = "https://www.goibibo.com/flights/"
one_stop=(By.XPATH,"//span[text()='1 Stop']")