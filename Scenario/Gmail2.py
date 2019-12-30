'''Scenario 2
1. Open any browser of your choice, say Mozilla Firefox
2. Navigate to https://www.gmail.com
3. Enter a valid Email Id or Phone Number
4. Click Next button
5. Enter Password and click “Sign in” button.
6. Verify that gmail is logged in successfully.
7. Click compose button and verify that a new mail window is opened.
8. Enter a Email Id
9. Enter some subject, say “Test Mail”
10. Enter some text in body 11. click send button. '''
from selenium import webdriver
import time
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://gmail.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_name("identifier").send_keys("selenium658@gmail.com")
driver.find_element_by_xpath("//span[text()='Next']").click()
driver.find_element_by_name("password").send_keys("deepu@0109")
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Next']").click()
#verify login page
ExpTitle=driver.title
print(ExpTitle)
ExpTitle=ExpTitle[0:5: ]
ActTitle="Inbox"
assert ActTitle==ExpTitle,"False"
print("Login is successfull----->Pass")
#click on compose and check the window
driver.find_element_by_xpath("//div[@class='aic']//div[text()='Compose']").click()
message=driver.find_element_by_xpath("//div[text()='New Message']")
Exp_msg="New Message"
Act_msg=message.text
assert Exp_msg==Act_msg,"False"
print("Compose window is verified--->Pass")
time.sleep(5)
#Enter email id
driver.find_element_by_xpath("//textarea[@aria-label='To']").send_keys("deepuravishancar@gmail.com")
driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys("Test Mail")
driver.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys("Test mail was requested")
driver.find_element_by_xpath("//div[text()='Send']").click()
print("Composing mail was successfull")
driver.quit()