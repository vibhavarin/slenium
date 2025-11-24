

class TestLogin:

     def test_login(self,setup):
         setup.find_element('id','user-name').send_keys('standard_user')
         # time.sleep(2)

         setup.find_element('id','password').send_keys('secret_sauce')
         # time.sleep(2)

         setup.find_element('id','login-button').click()

