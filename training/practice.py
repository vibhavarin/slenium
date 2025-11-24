# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(opts)
#
# driver.implicitly_wait(20)

# driver.get('https://www.saucedemo.com/')
#
# driver.find_element('id','user-name').send_keys('standard_user')
# driver.find_element('id','password').send_keys('secret_sauce')
# driver.find_element('id','login-button').click()
#
# driver.find_element('id','react-burger-menu-btn').click()
# driver.find_element('id','logout_sidebar_link').click()



################################################################################################

# driver.get('https://testautomationpractice.blogspot.com/')
# driver.find_element('id','cookieChoiceDismiss').click()
# driver.find_element('id','name').send_keys('vibha')
# driver.find_element('id','email').send_keys('vibha@gmail.com')
# driver.find_element('id','phone').send_keys('0123456789')
# driver.find_element('id','textarea').send_keys('abc roadno.11')
# driver.find_element('id','female').click()
# driver.find_element('id','monday').click()
# data = driver.find_element('id','country')
# ssd = Select(data)
# ssd.select_by_value('germany')
# data = driver.find_element('id','colors')
# ssd = Select(data)
# ssd.select_by_value('yellow')
# data = driver.find_element('xpath','//select[@name="animals"]')
# ssd.select_by_value('cat')

#################################################################################

# driver.get('https://demowebshop.tricentis.com/')
# driver.find_element('class name','ico-register').click()
# driver.find_element('class name','ico-login').click()
# driver.find_element('class name','cart-label').click()
##############################################################################
# driver.get('https://demowebshop.tricentis.com/')
# driver.find_element('xpath','//a[text()="Register"]').click()
#
# driver.find_element('xpath','//input[@value="F"]').click()
# driver.find_element('id','FirstName').send_keys('vibha')
# driver.find_element('id','LastName').send_keys('vibha')
# driver.find_element('id','Email').send_keys('vibha@gmail.com')
# driver.find_element('id','Password').send_keys('!1234567@')
# driver.find_element('id','ConfirmPassword').send_keys('!1234567@')

###############################################################################
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# driver.find_element('class name','inputtext._58mg._5dba._2ph-').send_keys('vibha')
# driver.find_element('class name','inputtext._58mg._5dba._2ph-').send_keys('vibha')
################################################################################

# driver.get('https://www.facebook.com/r.php?entry_point=login')
# driver.find_element('tag name','input').send_keys('vibha')
# driver.find_element('tag name','input').send_keys('vibha')



######################################################################################3
import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)

driver.implicitly_wait(20)

driver.get('https://urlaub.check24.de/vergleich/2005-6-6-0/Ferien%20buchen?wpset=google_reisen&gcamid=14061061848&tid=nonpof&gad_source=1&gad_campaignid=14061061848&gbraid=0AAAAADsjqrU8NW7ym5Uh2SuvARK9l-Y45&gclid=CjwKCAiA_orJBhBNEiwABkdmjDAlwfpMWfxh-WP0yEWN0BVD4v5PsLrw2Ncxo8LnsuTtwHG41xpOBxoCipQQAvD_BwE')

driver.find_element('xpath','//input[@id="c24-travel-destination-element"]').send_keys('mallorca')

driver.find_element('xpath','//label[@for="c24-travel-ac-airport-list-item0-1"]').send_keys('stuttgart')

driver.find_element('xpath','//div[@id="c24-travel-ac-airport-button"]').click()




