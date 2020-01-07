from selenium import webdriver
import time
#1 Open browser
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
#2 Enter URL(bluestone)
driver.get("https://www.bluestone.com/")
driver.maximize_window()
driver.implicitly_wait(12)

#3 click on offers
act = ActionChains(driver)
wb_offers = driver.find_element_by_xpath("//a[@title='Offers']")
#4 Select 0% off Making charge and click on it
wb_twntyoffer = driver.find_element_by_xpath("//span[@data-p='offers-20peroff,m']")
act.move_to_element(wb_offers).click(wb_twntyoffer).perform()
# 5Verify the products list display with 0% charging
wb_lst_of_offers = driver.find_elements_by_xpath("//span[@class='offer']")
emptylst = []
#append the product list
for i in wb_lst_of_offers:
    emptylst.append(i.text)
    print(emptylst)

