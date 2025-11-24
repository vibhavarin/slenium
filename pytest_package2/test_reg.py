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
