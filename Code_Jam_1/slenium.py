from selenium import *
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://pclub.search.in')

blood_grp = driver.find_element_by_id('mat-input-1')

blood_grp.click()

#for option in blood_grp.find_elements_by_tag_name('option'):
 #   if option.text == s:
  #      option.click() # select() in earlier versions of webdriver
   #     break
blood_grp.click()
blood_grp.send_keys('Amitesh')


