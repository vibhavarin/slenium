'''
class name  :   If we are having "class" attribute, then we can go for "class name" locator


    DRAWBACKS
    *   class name is not unique
        Incase of multiple occurances, class name will always consider the first occurance
    *   It cannot locate spaces
        Whenever we have space in the value of the class attribute, we should replace the space with dot(.)

'''

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
#
# driver.find_element('class name','ico-register').click()
# time.sleep(2)
# driver.find_element('class name','ico-login').click()
# time.sleep(2)
# driver.find_element('class name','ico-cart').click()


###########################################################################################

# 2 example
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Veetrag\PycharmProjects\selenium training\files\css_selector.html')
# time.sleep(2)
#
# driver.find_element('class name','first_row').send_keys('asd')
# time.sleep(2)
# driver.find_element('class name','first_row').send_keys('gfhg')
# time.sleep(2)
# driver.find_element('class name','first_row').send_keys('ahj')
# time.sleep(2)
#

#########################################################################################

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('class name','inputtext _58mg _5dba _2ph-').send_keys('vibha')
## error because class name locator does not recognize the space
########################################################################################
## to overcome this drawback we replace space with dot(.)

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)
# driver.find_element('xpath','(//span[text()="Allow all cookies"])[2]').click()
driver.find_element('class name','x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft').click()
time.sleep(2)
driver.find_element('class name','inputtext._58mg._5dba._2ph-').send_keys('vibha')

## when I am using class name locator to locate the all cookie message its giving me error but when

## I am using dot in between spas then it is executing, but it is not clicking the all cookie button and executing without error




