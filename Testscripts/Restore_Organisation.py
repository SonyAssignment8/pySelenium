#Verify organisation Name which is restored from the recycle Bin
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost:8888/")
#login to the application
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("user_password").send_keys("manager")
driver.find_element_by_id("submitButton").click()
#Navigate to Organisation
driver.find_element_by_xpath("//a[text()='Organizations']").click()
#select the Organisation to be deleted
driver.find_element_by_xpath("//tr/td/a[text()='t3M Invest A/S']").click()
#Delete the Organisation
driver.find_element_by_xpath("//input[@name='Delete']").click()
alt=driver.switch_to_alert()
alt.accept()
#Navigate to Recycling Bin
driver.find_element_by_xpath("//a[text()='More']").click()
driver.find_element_by_xpath("//a[text()='Recycle Bin']").click()
#select the Organisation to be restored
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("//input[@value='Restore']").click()
#Handle the Alert popup
alt1=driver.switch_to_alert()
alt1.accept()
#get the organisation names
driver.find_element_by_xpath("//a[text()='Organizations']").click()
l=driver.find_elements_by_xpath("//tr[@class='lvtColData']/td[3]")
#Validate the organisation name
ExpResult='t3M Invest A/S'
flag=False
for i in l:
    i.text==ExpResult
    flag=True
assert flag==True,"False"
print("Organisation is restored")