from source.pages.add_to_cart import AddToCart
from source.pages.home_page_search_product import HomePageSearchProduct
from source.utilities.webdriver_factory import WebDriverFactory
#from source.utilities.webdriver_factory import WebDriverFactory

class HomeSearchProduct():
    def __init__(self,driver):
        #super().__init__(driver)
        self.driver=driver

    def searchProduct(self,name):
        HomePageSearchProduct(self.driver).searchBox(name)
        HomePageSearchProduct(self.driver).elementClick("//input[@value='Go']","xpath")
        HomePageSearchProduct(self.driver).click_on_product()
       # HomePageSearchProduct(self.driver).add_to_list()

    def addToCart(self):
        AddToCart(self.driver).add_to_cart()

