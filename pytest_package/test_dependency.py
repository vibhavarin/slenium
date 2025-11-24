import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
#
# driver = webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver,10)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# @pytest.mark.dependency()
# def test_login():
#
#     driver.find_element('css selector','input[id="user-name"]').send_keys('standard_user')
#     time.sleep(2)
#     driver.find_element('css selector','input[id="password"]').send_keys('secret_sauceee')
#     time.sleep(2)
#     driver.find_element('css selector','input[id="login-button"]').click()
#     wait_.until(expected_conditions.visibility_of_element_located(('xpath','//span[text()="Products"]')))
#
# @pytest.mark.dependency(depends=['test_login'])
# def test_logout():
#     driver.find_element('id','react-burger-menu-btn').click()
#     time.sleep(2)
#     driver.find_element('id','logout_sidebar_link').click()

############################################################################################
# @pytest.mark.dependency()
# def test_login():
#     print("login execution")
# @pytest.mark.dependency(depends=['test_login','test_reg'])
# def test_logout():
#     print("logout execution")
# @pytest.mark.dependency()
# def test_reg():
#     print("reg execution")

#############################################################################################

# class TestSample:
#
#    @pytest.mark.dependency()
#    def test_login(self):
#       print("login execution")
#
#    @pytest.mark.dependency(depends=['TestSample::test_login,test_reg'])
#    def test_logout(self):
#       print("logout execution")
#
#    @pytest.mark.dependency()
#    def test_reg(self):
#       print("reg execution")

#############################################################################################