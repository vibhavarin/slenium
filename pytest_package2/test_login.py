class TestLogin:
    def test_login(self,setup):
        setup.find_element('xpath','//a[@class="ico-login"]').click()
    def test_email(self,setup):
        setup.find_element('id','Email').send_keys('vibha@.com')
    def test_password(self,setup):
        setup.find_element('id','Password').send_keys('!sdfsdf#')