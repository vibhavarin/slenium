'''
name    :   name is an attribute which is also a locator.
            So if we have name attribute, then we can go for name locator

            DRAWBACKS
            *   name is not unique
            *   Incase of multiple occurances, name will always consider the first occurance

'''


# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('name','user-name').send_keys('standard_user')
# time.sleep(2)
#
# driver.find_element('name','password').send_keys('secret_sauce')
# time.sleep(2)
#
# driver.find_element('name','login-button').click()


import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Veetrag\PycharmProjects\selenium training\files\css_selector.html')
time.sleep(2)

driver.find_element('name','fname').send_keys('abc')
time.sleep(2)
driver.find_element('name','fname').send_keys('hdgjhsgd')
time.sleep(2)
driver.find_element('name','fname').send_keys('vbvv')