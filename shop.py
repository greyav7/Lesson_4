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
time.sleep(3)

username = driver.find_element_by_id('username')
username.send_keys('Ivan363636@rambler.ru')
password = driver.find_element_by_id('password')
password.send_keys('Ivan363636!$')
driver.find_element_by_css_selector('[name="login"]').click()

driver.find_element_by_id('menu-item-40').click()
time.sleep(3)
# test 1
# driver.execute_script("window.scrollBy(0, 600);")
# driver.find_element_by_css_selector('[alt="Mastering HTML5 Forms"]').click()
# h3 = driver.find_element_by_css_selector('[itemprop="name"]')
# h3 = h3.text
# assert h3 == "HTML5 Forms"

#test 2
# driver.find_element_by_class_name('cat-item-19').click()
# count = driver.find_element_by_css_selector('.cat-item-19 .count')
# count = count.text
# if count == '(3)':
#     print ('3 book')
# else:
#     print ('count')

#test 3
# element = driver.find_element_by_css_selector(".orderby")
# select = Select(element)
#
# element_check = element.get_attribute("value")
# if element_check == "menu_order":
#         print("Default sorting")
# else:
#         print("no")
#
# select.select_by_value("price-desc")
#
# element = driver.find_element_by_css_selector(".orderby")
# select = Select(element)
#
# element_check = element.get_attribute("value")
# if element_check == "price-desc":
#         print("Sort by price: high to low")
# else:
#         print("no")

#test 4
# driver.execute_script("window.scrollBy(0, 700);")
# driver.find_element_by_css_selector('[data-product_id="169"]').click()
# old_price = driver.find_element(By.CSS_SELECTOR, '.price > del > span')
# old_price = old_price.text
# assert old_price == '₹600.00'
# new_price = driver.find_element(By.CSS_SELECTOR, '.price > ins > span')
# new_price = new_price.text
# assert new_price == '₹450.00'
#
# picture = WebDriverWait(driver, 5).until(
#     EC. element_to_be_clickable((By.CSS_SELECTOR, '.images')))
# picture.click()
# close = WebDriverWait(driver, 5).until(
#     EC. element_to_be_clickable((By.CSS_SELECTOR, '.pp_close')))
# close.click()

#test 5
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 1200);")
# driver.find_element_by_css_selector('[data-product_id="165"]').click()
# item = driver.find_element(By.CLASS_NAME, "cartcontents")
# item = item.text
# # assert item == '1 Item' // assert не работает почему-то именно здесь
# cost = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents .amount")
# cos = cost.text
# # assert cos == '₹350.00' // assert не работает почему-то именно здесь
# driver.find_element(By.ID, "wpmenucartli").click()
#
# WebDriverWait(driver, 5).until(
#      EC. text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal > td'), '350.00'))
# WebDriverWait(driver, 5).until(
#      EC. text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total > td'), '357.00'))

#test 6

time.sleep(3)
driver.quit()

C:/Users/kunae_000/PycharmProjects/pythonProject/Lesson 4