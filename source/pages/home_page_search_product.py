import  time
from source.utilities.generic_methods import GenericMethods
from source.utilities import custom_logger as cl
import logging

class HomePageSearchProduct(GenericMethods):
    """
    searching product in amazon==>DocString
    """
    def __init__(self,driver):
        #we r inheriting GenericMethods for webdriver(driver)  using super()
        super().__init__(driver)
        self.driver=driver

        self.search_product_Name_id="twotabsearchtextbox"

    def searchBox(self,ProductName):
        self.sendKeys(ProductName,self.search_product_Name_id)
        time.sleep(3)

    def click_on_product(self):
        self.elementClick(locator="//span[text()='Apple iPhone XR (128GB) - Black']",locatorType="xpath")
        time.sleep(3)


