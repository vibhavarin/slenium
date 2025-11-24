'''
xpath   :   It is a locator used to locate any element on the application uniquely
            We can locate the elements using attributes, we can locate elements using text, indexing is possible,
            can locate dynamically changing elements
            We can locate any element on the web-application using xpath

There are 2 types of xpath
*   absolute xpath  :   Starts from the root of html
*   relative xpath

'''

# import time
#
# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Veetrag\PycharmProjects\selenium training\files\css_selector_dup1.html')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/input[1]').send_keys('Vibha')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/input[2]').send_keys('vibha@12345')

################################################################################################


import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)

# driver.get('https://www.saucedemo.com/')
#
# driver.find_element('xpath','html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(2)
#
# driver.find_element('xpath','html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
# time.sleep(2)
#
# driver.find_element('xpath','html/body/div/div/div[2]/div[1]/div/div/form/input').click()
# time.sleep(2)
#
# driver.find_element('xpath','html/body/div/div/div/div/div/div[2]').click()
# time.sleep(2)
#
# # driver.find_element('xpath','').click()

#############################################################################################################

''' with attribute name and value : tag_name[@attribute name ="attribute value"]

'''

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element('xpath','//a[@class="ico-register"]').click()
time.sleep(2)

driver.find_element('xpath','//input[@value="F"]').click()
time.sleep(2)

driver.find_element('xpath','//input[@id="FirstName"]').send_keys('abc')
driver.find_element('xpath','//input[@id="LastName"]').send_keys('pqr')
driver.find_element('xpath','//input[@id="Email"]').send_keys('abc@gmail.com')
driver.find_element('xpath','//input[@id="Password"]').send_keys('abc')
driver.find_element('xpath','//input[@id="ConfirmPassword"]').send_keys('abc')
############################################################################################################



