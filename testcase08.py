'''Scenario 8
1. open Browser
2. Pass Url (bluestone)
3. Move the cursor All Jewellery
4. select Kadas and click on it
5. select any kada.
6. Select Bangle size
7. click on buy now
8. capture the size of item in cart page and Compare with selectd size
9. close browser'''
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
        self.Alljwellary()

    def Alljwellary(self):
        jwells_element=self.driver.find_element_by_xpath("//a[text()='All Jewellery ']")
        act=ActionChains(self.driver)
        act.move_to_element(jwells_element).perform()
        self.driver.find_element_by_xpath("//span[text()='Kadas']").click()
        self.selectOneProduct()
    def selectOneProduct(self):
        self.driver.find_element_by_xpath("(//img[@class='hc img-responsive center-block'])[1]").click()
        win_list=self.driver.window_handles[1]
        self.driver.switch_to.window(win_list)

        self.driver.execute_script("window.scrollBy(0,250)")
        self.driver.find_element_by_xpath("//span[text()=' Select Size ']").click()
        self.driver.find_element_by_xpath("(//span[@class='size'])[1]").click()
        self.driver.find_element_by_xpath("//input[@value='Buy Now']").click()
        self.driver.find_element_by_xpath("//span[@class='icon-ion-android-arrow-dropdown']").click()
        size_list=self.driver.find_elements_by_xpath("//span[@class='size']")
        for i in size_list:
            if i.contains("2-2(2 2/16"):
                print("TC_Pass")
            else:
                print("TC_Fail")

b=BlueStone("chrome")
b.launchWebsite()
