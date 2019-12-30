'''
Scenario 2
 1. Open any browser of your choice, say Mozilla Firefox
 2. Navigate to https://www.gmail.com
 3. Enter a valid Email Id or Phone Number
 4. Click Next button
 5. Enter Password and click “Sign in” button.
 6. Verify that gmail is logged in successfully.
 7. Click compose button and verify that a new mail window is opened.
 8. Enter a Email Id
 9. Enter some subject, say “Test Mail”
 10. Enter some text in body
 11. click send button.
'''
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("https://mail.google.com/mail/u/0/#inbox")
time.sleep(2)
driver.find_element_by_name("identifier").send_keys("seleniumoar1234")
driver.find_element_by_xpath("//span[text()='Next']").click()
driver.find_element_by_name("password").send_keys("Selenium1-2")
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Next']").click()
act_url=driver.current_url
#print(act_url)
expect_url="https://accounts.google.com/signin"
assert expect_url.find(act_url),"gmail does not logged successfully"
print("Gamil logged successfully")
driver.find_element_by_xpath("//div[text()='Compose']").click()
driver.find_element_by_name("to").send_keys("sujithak10@gmail.com")
driver.find_element_by_name("subjectbox").send_keys("This is test mail")
driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf tS-tW']").send_keys("Helo h ru i am fine thank you")
driver.find_element_by_xpath("//div[text()='Send']").click()
mesg=driver.find_element_by_xpath("//span[text()='Message sent.']").text
print(mesg,"sucessfully")
driver.close()