from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
driver.get("https://www.bluestone.com/")
mousehover=driver.find_element_by_xpath("//a[text()='Offers ']")
a=ActionChains(driver)
a.move_to_element(mousehover).perform()
time.sleep(3)
driver.find_element_by_xpath("//span[text()='20% off on making charge']").click()

def product():
    prod=driver.find_elements_by_xpath("//img[@class='hc img-responsive center-block']")
    for i in prod:
        print(i.text)
product()









