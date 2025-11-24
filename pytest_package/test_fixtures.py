import pytest
# @pytest.fixture()
# def greet():
#     print('good morning')
#
# def test_login(greet):
#     print('login executing')
#
# def test_logout(greet):
#     print('logout executing')

#######################################################################################

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# def test_username():
#   driver.find_element('id','user-name').send_keys('standard_user')
#   time.sleep(2)
# def test_password():
#   driver.find_element('id','password').send_keys('secret_sauce')
#   time.sleep(2)
# def test_login():
#   driver.find_element('id','login-button').click()
#   time.sleep(2)
# def test_burger_button():
#   driver.find_element('id','react-burger-menu-btn').click()
#   time.sleep(2)
# def test_logout_button():
#   driver.find_element('id','logout_sidebar_link').click()

##################################################################################

# @pytest.fixture(scope='module')
# def setup():
#     print('good morning')
#     yield
#     print('good evening')
#
# def test_singup(setup):
#     print('signup executing')
#
# def test_logout():
#     print('logout executing')
#
# class TestSample:
#     def test_login(self,setup):
#         print('login executing')
#
#     def test_reg(self,setup):
#         print('reg executing')
# class TestSpam:
#     def test_gmail(self,setup):
#         print('gmail executing')


###########################################################################3
import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

@pytest.fixture(scope='class')
def setup():
    driver=webdriver.Chrome(opts)
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()
## setup --> driver = webdriver.Chrome(opts)

class TestRegister:
    def test_reg(self,setup):
        setup.find_element('xpath', '//a[text()="Register"]').click()
    def test_gender(self,setup):
        setup.find_element('xpath','//input[@value="F"]').click()
    def test_firstname(self,setup):
        setup.find_element('id','FirstName').send_keys('vibha')

    def test_lastname(self, setup):
        setup.find_element('id','LastName').send_keys('vibha')

    def test_email(self, setup):
        setup.find_element('id','Email').send_keys('vibha@gmail.com')

    def test_password(self, setup):
        setup.find_element('id','Password').send_keys('!1234567@')

    def test_confirmpassword(self, setup):
        setup.find_element('id','ConfirmPassword').send_keys('!1234567@')


class TestLogin:
    def test_login(self,setup):
        setup.find_element('xpath','//a[@class="ico-login"]').click()
    def test_email(self,setup):
        setup.find_element('id','Email').send_keys('vibha@.com')
    def test_password(self,setup):
        setup.find_element('id','Password').send_keys('!sdfsdf#')