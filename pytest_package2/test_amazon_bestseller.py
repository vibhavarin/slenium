class TestBestseller:
    def test_bestseller(self,setup):
        setup.find_element('link text','Bestsellers').click()