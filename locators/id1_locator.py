'''id  :   id is an attribute which is also a locator.
        If we have id attribute, we can go for id locator
'''

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element('id','cookieChoiceDismiss').click()
time.sleep(2)

driver.find_element('id','name').send_keys('abc')
time.sleep(2)

driver.find_element('id','email').send_keys('abc@gmail.com')
time.sleep(2)

driver.find_element('id','phone').send_keys('0123456789')
time.sleep(2)

driver.find_element('id','textarea').send_keys('afasfsf')
time.sleep(2)

driver.find_element('id','female').click()
driver.find_element('id','monday').click()
