''''
tag name    :   We can locate the web-elements using their tagname.
                But tagname will always consider the first occurance

'''

# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Veetrag\PycharmProjects\selenium training\files\css_selector.html')
#
# driver.find_element('tag name','input').send_keys('vibha')
# time.sleep(2)
#
# driver.find_element('tag name','input').send_keys('abc')


################################################################################

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('tag name','input').send_keys('vibha')
time.sleep(2)

# driver.find_element('tag name','input').send_keys('abc')

