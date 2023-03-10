import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.implicitly_wait(10)
driver.find_element_by_link_text('My Account').click()
time.sleep(5)
# reg_email = driver.find_element_by_id('reg_email')
# reg_email.send_keys('Ivan363636@rambler.ru')
# reg_password = driver.find_element_by_id('reg_password')
# reg_password.send_keys('Ivan363636!$')
# driver.find_element_by_css_selector('[value="Register"]').click()

# driver.get("https://practice.automationtesting.in")
# driver.implicitly_wait(10)
# driver.find_element_by_link_text('My Account').click()
# time.sleep(5)
#
username = driver.find_element_by_id('username')
username.send_keys('Ivan363636@rambler.ru')
password = driver.find_element_by_id('password')
password.send_keys('Ivan363636!$')
driver.find_element_by_css_selector('[name="login"]').click()

time.sleep(3)
driver.quit()
