from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config
import time


driver = webdriver.PhantomJS("d:/Code/Python/TelyChatbot/phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver.get("http://cms.amritanet.edu/gate-passes/apply")
elem = driver.find_element_by_name("username")
elem.send_keys(config.USERNAME)
elem = driver.find_element_by_name("password")
elem.send_keys(config.PASSWORD)
elem.send_keys(Keys.ENTER)
time.sleep(1)
passType = driver.find_elements_by_tag_name("option")
for option in passType:
    if option.text == 'Day Pass':
        option.click()
date = driver.find_element_by_id("from_date")
date.click()
datePicker = driver.find_element_by_class_name("datepicker-days")
datePicker = datePicker.find_element_by_class_name("table-condensed")
datePicker = datePicker.find_elements_by_tag_name("tbody")
for weeks in datePicker:
    days = weeks.find_elements_by_tag_name('td')
    try:
        for day in days:
            if day.text == '15':
                day.click()
    except:
        pass
timeArea = driver.find_element_by_name("from_time")
timeArea.click()
timeArea.clear()
timeArea.send_keys("12:30 pm")
applyingTo = driver.find_elements_by_tag_name("option")
for option in applyingTo:
    if option.text == 'Resident Warden':
        option.click()
occasion = driver.find_elements_by_tag_name('option')
for option in occasion:
    if option.text == "Regular Academic Semester":
        option.click()
reason = driver.find_element_by_tag_name("textarea")
reason.send_keys("Going home")
proceed = driver.find_element_by_id("proceed-btn")
proceed.click()
time.sleep(2)
applyPass = driver.find_elements_by_tag_name('button')
for buttons in applyPass:
    if buttons.text == "Apply Pass":
        buttons.click()
