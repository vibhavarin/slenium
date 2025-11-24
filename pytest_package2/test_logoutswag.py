

class test_logout:
    def test_logout(self, setup):
        setup.find_element('id', 'react-burger-menu-btn').click()

        setup.find_element('id', 'logout_sidebar_link').click()