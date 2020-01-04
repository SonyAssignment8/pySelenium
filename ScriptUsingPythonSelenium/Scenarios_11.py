'''Scenario 11
1. Open browser
2. Enter URL(bluestone)
3. click on offers
4. Select 0% off Making charge and click on it
5. Verify the products list display with 0% charging
6. close Browser'''
from selenium import webdriver
from selenium.webdriver import ActionChains


class BlueStone:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Safari()

    def launchWebsite(self):
        self.driver.get("https://www.bluestone.com/")
        self.offers()

    def offers(self):
        self.driver.find_element_by_xpath("//a[text()='Offers ']").click()
        self.makingCharges()

    def makingCharges(self):
        product_offer=self.driver.find_elements_by_xpath("//span[@class='offer']")
        p_lst=[]
        for i in product_offer:
            p_lst.append(i.text)
        flag=False
        for i in p_lst:
            if i.__contains__("20% OFF ON DIAMOND PRICE"):
                flag=True

        assert flag==True,"list does not contains 20% off product list"
        print("list contains 20% off product list ")
        self.driver.close()

b=BlueStone("chrome")
b.launchWebsite()




