# -*- coding: utf-8 -*-

import selenium
import re
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# browser = webdriver.PhantomJS(executable_path="G:\Python projects\selenium\phantomjs.exe")

browser = webdriver.Firefox()
browser.get('https://www.americanairlines.cn/intl/cn/index.jsp?locale=zh_CN')
input = browser.find_element_by_id('reservationFlightSearchForm.originAirport')
input.send_keys('MEL')
input = browser.find_element_by_id('reservationFlightSearchForm.destinationAirport')
input.send_keys('SYD')
input.click(browser.find_element_by_id('bookingModule-submit'))
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
print(browser.current_url)
print(browser.get_cookie())
print(browser.page_source)


browser.close()


