'''Scenario 1
 1. Open a browser of your choice say Mozilla Firefox using Gecko Driver
 2. Navigate to Gmail (https://www.gmail.com)
 3. Login to your Gmail with correct credentials
 4. Verify that by default “Primary” section is selected.
 5. If not click on the Primary tab.
 6. Get the count of the total number of emails in the Primary tab.
 7. Get the name of the sender and subject of Nth Email of your inbox.
 8. Write a method to get the name of the sender and subject of email of your inbox.'''
from selenium import webdriver
import time
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://accounts.google.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_name("identifier").send_keys("selenium658@gmail.com")
driver.find_element_by_xpath("//span[text()='Next']").click()
driver.find_element_by_name("password").send_keys("deepu@0109")
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Next']").click()
ExpTab="Primary"
time.sleep(4)
primary=driver.find_element_by_xpath("//div[text()='Primary']")
ActTab=primary.text
if ExpTab==ActTab:
    print("Primary Tab is selected")
    primary.click()
else:
    print("Primary Tab is not selected")
result=driver.find_element_by_xpath("//div[@class='J-J5-Ji amH J-JN-I']")
count=result.text
countnum=count[8: :]
print("Total number of mails :",countnum)
list_items=driver.find_elements_by_xpath("//tr//td//div//span")
for i in list_items:
    lst_mail=i.text
    time.sleep(6)

    # exp=driver.find_element_by_xpath("//tr[@class='zA yO x7 byw']")
    # exp.click()
    # if lst_mail==exp:
    #     lst_mail.click()
    #     print(lst_mail.text)