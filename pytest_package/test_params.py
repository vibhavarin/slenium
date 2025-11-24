import time
import pytest
from selenium import webdriver

opts = webdriver.ChromeOptions()
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