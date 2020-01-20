import pytest
import time
from source.utilities import excel
from test_scripts.test_cases.test_amazon import HomeSearchProduct


@pytest.mark.usefixtures("OneTimeSetup")
class Test_AmazonProj():

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.hs=HomeSearchProduct(self.driver)

    def test_tc_001_add_product_and_verify(self):
        self.hs.searchProduct(excel.get_value("Cart","TC_002","ProductName"))
        self.hs.addToCart()


