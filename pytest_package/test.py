# import time
# import pytest
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
#
# @pytest.fixture(scope='class',params=['chrome','firefox','internet explorer'])
# def setup(request):
#     parameter= request.param
#
#     if parameter == 'chrome':
#        driver = webdriver.Chrome(opts)
#     elif parameter == 'firefox':
#         driver = webdriver.Firefox()
#     elif parameter == 'internet explorer':
#         driver = webdriver.ie()
#
#     driver.get('https://www.saucedemo.com/')
#     time.sleep(2)
#     yield driver
#
#
# class TestSample:
#    def test_username(self,setup):
#        setup.find_element('css selector','input[id="user-name"]').send_keys('standard_user')
#        time.sleep(2)
#
#    def test_password(self,setup):
#        setup.find_element('css selector','input[id="password"]').send_keys('secret_sauce')
#        time.sleep(2)
#
#    def test_login(self,setup):
#       setup.find_element('css selector','input[id="login-button"]').click()



#######################################################################################################

import time
import pytest
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

@pytest.fixture(scope='class',params=['chrome','firefox','edge'])
def setup(request):
    parameter= request.param

    if parameter == 'chrome':
       driver=webdriver.Chrome(opts)
    elif parameter == 'firefox':
        driver = webdriver.Firefox()
    elif parameter == 'edge':
        driver = webdriver.Edge()

        driver.get('https://demoapps.qspiders.com/ui')
        # driver.find_element('xpath','//p[text()="UI Testing Concepts"]').click()
        yield driver
        time.sleep(2)

class TestSample:

     def test_name(self,setup):
         setup.find_element('id','name').send_keys('abc')
         time.sleep(2)

     def test_email(self,setup):
         setup.find_element('css selector','input[placeholder="Enter Your Email"]').send_keys('abc@gmail.com')
         time.sleep(2)

     def test_password(self,setup):
         setup.find_element('name','password').send_keys('!abc1a')
         time.sleep(2)

     def test_reg(self,setup):
         setup.find_element('xpath','//button[text()="Register"]').click()


# driver.find_element('css selector','input[placeholder="Enter your email"]').send_keys('abc@gmail.com')
# time.sleep(2)
#
# driver.find_element('id','password').send_keys('!abc1a')
# time.sleep(2)
#
# # driver.find_element('xpath','//button[text()="Login"]').click()



