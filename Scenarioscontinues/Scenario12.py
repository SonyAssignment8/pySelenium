'''Scenario 12
1. Open browser
2. Enter URL(bluestone)
3. click on offers
4. Select 75% off Making charge and click on it
5. Verify the products list display with 75% charging
6. close Browser Scenario '''
from selenium import webdriver
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to bluestone page
driver.get("https://www.bluestone.com/")
driver.find_element_by_xpath("//a[text()='Offers ']").click()
driver.close()
