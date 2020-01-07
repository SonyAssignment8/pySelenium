'''Scenario 11
1.Open browser
2. Enter URL(bluestone)
3. click on offers
4. Select 0% off Making charge and click on it
5. Verify the products list display with 0% charging
6. close Browse'''
import time

from selenium import webdriver
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to bluestone page
driver.get("https://www.bluestone.com/")
driver.find_element_by_xpath("//a[text()='Offers ']").click()
time.sleep(4)
act=driver.find_elements_by_xpath("//span[contains(text(),'making charge')]")
exp="making charge"
for i in act:
    actual=print(i.text)
    assert actual == exp, "False"
    print("The discount price is verified")
driver.close()