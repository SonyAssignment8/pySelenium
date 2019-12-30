'''Scenario 7
1. open Browser
2. Pass Url (bluestone)
3. Move the cursor All Jewellery
4. select Kadas and click on it
5. select any kada.
6. click on buy now
7. Capture whether error message is displayed or not(Not Displayed fail test case)
8. close browser'''
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
        win_list=self.driver.window_handles
        i=iter(win_list)
        parent_win=next(i)
        child_win=next(i)
        self.driver.switch_to.window(child_win)
        self.driver.find_element_by_xpath("//input[@value='Buy Now']").click()
        err_act=self.driver.find_element_by_xpath("//div[text()='* This field is required']").text
        err_exp="* This field is required"
        if err_act==err_exp:
            print("error msg dispalyed..TC Pass")
        else:
            print("err msg not-displayed TC fail")

b=BlueStone("chrome")
b.launchWebsite()

