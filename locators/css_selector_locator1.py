'''
css selector    :   To locate the web-elements using any attribute
                    SYNTAX  :   tagname[attr_name="attr_value"]

                    DRAWBACKS
                    *   Indexing is not possible in css selector.
                        If we have multiple occurances, css selector will always consider the first occurance
                    *   Cannot locate text using css selector

'''

# import time
# #EG1
#
# from selenium import webdriver
# # opts = webdriver.ChromeOptions()
# # opts.add_experimental_option('detach',True)
# # driver = webdriver.Chrome(opts)
# driver = webdriver.Firefox()
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('css selector','input[id="user-name"]').send_keys('standard_user')
# time.sleep(2)
#
# driver.find_element('css selector','input[id="password"]').send_keys('secret_sauce')
# time.sleep(2)
#
# driver.find_element('css selector','input[id="login-button"]').click()

###########################################################################################################


# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(20)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
#
# driver.find_element('css selector','input[name="firstname"]').send_keys('abc')
#
# driver.find_element('css selector','input[name="lastname"]').send_keys('def')
#
# driver.find_element('css selector','input[value="1"]').click()
#
# driver.find_element('css selector','input[name="reg_email__"]').send_keys('abc@gmail.com')
#
# driver.find_element('css selector','input[name="reg_passwd__"]').send_keys('1!bvnbv@')


##############################################################################################################

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver= webdriver.Chrome(opts)
# driver.implicitly_wait(20)
#
# driver.get('https://www.myntra.com/')
#
# driver.find_element('css selector','a[data-group="men"]').click()
# time.sleep(2)
# driver.find_element('css selector','a[data-group="women"]').click()
#
# driver.find_element('css selector','a[data-group="kids"]').click()
#
# driver.find_element('css selector','a[data-group="home"]').click()

##########################################################################################################

######## The data will be filled in the same textbox
import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('css selector','input[type="text"]').send_keys('abc')
time.sleep(2)

driver.find_element('css selector','input[type="text"]').send_keys('bcd')