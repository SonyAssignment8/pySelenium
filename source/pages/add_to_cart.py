from datetime import time

from source.pages.home_page_search_product import HomePageSearchProduct
from source.utilities.generic_methods import GenericMethods


class AddToCart(GenericMethods):

    def __init__(self,driver):
        self.driver=driver
        HomePageSearchProduct(driver)


    def add_to_cart(self):
        self.switch_to_child_window(self.driver)
        self.timesleep()
        self.elementClick(locator="add-to-cart-button")
