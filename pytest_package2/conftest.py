# import time
# import pytest
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
#
# @pytest.fixture(scope='class')
# def setup():
#     driver=webdriver.Chrome(opts)
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(2)
#     yield driver
#     driver.close()

#######################################################################################

# import time
# import pytest
# from selenium import webdriver
# @pytest.fixture(scope='class')
# def setup():
#     driver = webdriver.Firefox()
#     driver.get('https://www.saucedemo.com/')
#     time.sleep(2)
#     yield driver
#     driver.close()

#######################################################################################

# import time
# import pytest
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
#
#
# @pytest.fixture(scope='class')
# def setup():
#     driver=webdriver.Chrome(opts)
#
#     driver.get('https://www.amazon.in/')
#     time.sleep(2)
#     yield driver
#     driver.close()
####################################################################################

import time
import pytest
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)


@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome(opts)

    driver.get('https://www.deichmann.com/de-de/')
    time.sleep(2)
    yield driver
    driver.close()