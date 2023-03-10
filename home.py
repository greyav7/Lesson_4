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
driver.execute_script("window.scrollBy(0, 600);")
read_more = driver.find_element_by_css_selector('[data-product_id="160"]')
read_more.click()
time.sleep(5) #Появляется реклама, закрытие вручную
driver.execute_script("window.scrollBy(0, 600);")
rew = driver.find_element_by_class_name('reviews_tab')
rew.click()
star = driver.find_element_by_class_name('star-5')
star.click()
comment = driver.find_element_by_id('comment')
comment.send_keys("Nice book!")
name = driver.find_element_by_id('author')
name.send_keys('Ivan')
email = driver.find_element_by_id('email')
email.send_keys('Ivan@rambler.ru')
submit = driver.find_element_by_id('submit')
submit.click()

time.sleep(3)
driver.quit()
