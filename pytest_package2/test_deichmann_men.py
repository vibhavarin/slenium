class TestAccount:
    def test_account(self, setup):
        setup.find_element('xpath', '(//font[text()="Men"])[2]').click()
