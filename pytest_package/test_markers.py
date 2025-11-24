'''
To group the testcases, we use markers
There are 2 types
    *   custom markers
    *   inbuilt markers
'''


import pytest

# @pytest.mark.vibha
# def test_login():
#     print('login execution')
#
# def test_signup():
#     print('signup execution')
#
# @pytest.mark.vibha
# @pytest.mark.piku
# def test_reg():
#     print('reg execution')
#
# def test_logout():
#     print('logout execution')


###########################################################################################

# @pytest.mark.sanity
# def test_login():
#     print('login execution')
#
# @pytest.mark.smoke
# def test_signup():
#     print('signup execution')
#
# @pytest.mark.smoke
# def test_reg():
#     print('reg execution')
#
# @pytest.mark.regression
# def test_logout():
#     print('logout execution')

###############################################################################################

# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print('login execution')
#
# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_signup():
#     print('signup execution')
# @pytest.mark.regression
# @pytest.mark.sanity
# def test_reg():
#     print('reg execution')
#
# @pytest.mark.regression
# @pytest.mark.sanity
# def test_logout():
#     print('logout execution')
#
###################################################################################################

# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print('login execution')
#
#     def test_signup(self):
#         print('signup execution')
#
#     def test_reg(self):
#         print('reg execution')
#
#     def test_logout(self):
#         print('logout execution')

### all test will pass

##################################################################################################

# @pytest.mark.regression
# class TestSample:
#
#     @pytest.mark.sanity
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.smoke
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
#
# #### if I gave regression test then pass all the tests,but if i gave only smoke test then it will pass only
# #smoke test.


###########################################################################################################

import time
import pytest
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)

@pytest.mark.parametrize('username,pwd',[('standard_user','secret_sauce'),('secret','ewe'),('standard','12333')])

def test_login(username,pwd):
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)
    driver.find_element('css selector','input[id="user-name"]').send_keys(username)
    time.sleep(2)


    driver.find_element('css selector','input[id="password"]').send_keys(pwd)
    time.sleep(2)


    driver.find_element('css selector','input[id="login-button"]').click()

    if 'inventory' in driver.current_url:
        print('successful')

    else:
        print('unsuccesful')