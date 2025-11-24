# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('link text','Men').click()
# time.sleep(2)
# driver.find_element('link text','Kids').click()
# time.sleep(2)
# driver.find_element('link text','Beauty').click()

################################################################################
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# #
# driver.get('https://www.amazon.in/')
# time.sleep(2)
#
# driver.find_element('link text','Sell').click()
# time.sleep(2)
#
# driver.find_element('link text','Bestsellers').click()
# time.sleep(2)
#
# driver.find_element('link text','Mobiles').click()
# time.sleep(2)

###################################################################################

import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)
# driver = webdriver.Firefox()
driver.get('https://demowebshop.tricentis.com/')

driver.find_element('link text','Register').click()
time.sleep(2)

driver.find_element('link text','Shopping cart').click()
time.sleep(2)

driver.find_element('link text','Log in').click()