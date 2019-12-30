import time

from selenium import webdriver
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to the page
driver.get("https://www.netmeds.com/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.switch_to_frame("webklipper-publisher-widget-container-notification-frame")
#Handle the popup
driver.find_element_by_xpath("//span[text()='No Thanks']").click()
driver.switch_to_default_content()
#Navigate to the Family care tab
driver.find_element_by_xpath("//a[text()='Family Care']").click()
time.sleep(12)
# #Select the price range
# driver.find_element_by_xpath("//button[text()='High to Low']").click()
# time.sleep(8)
#Select a particular product

driver.find_element_by_xpath("//span[@class='clsgetname']").click()

driver.find_element_by_xpath("//button[@title='ADD TO CART']").click()
#Navigate to the add to cart page
driver.find_element_by_xpath("//span[@class='counter-number']").click()
#Validation
Exp_Product="Women's Horlicks No Added Sugar Powder - Chocolate Flavour 400 gm (Refill Pack)"
Act_Product=driver.find_element_by_xpath("//div[@class='product-item-name col pl-0']").text
assert Exp_Product==Act_Product,"False"
print("The selected product is added to the cart-------->verified")
