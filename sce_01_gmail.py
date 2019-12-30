'''
Scenario 1
1. Open a browser of your choice say Mozilla Firefox using Gecko Driver
2. Navigate to Gmail (https://www.gmail.com)
3. Login to your Gmail with correct credentials.
4. Verify that by default “Primary” section is selected.
5. If not click on the Primary tab.
6. Get the count of the total number of emails in the Primary tab.
7. Get the name of the sender and subject of Nth Email of your inbox.
8. Write a method to get the name of the sender and subject of email of your inbox.
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
import time
time.sleep(4)
primary_btn=driver.find_element_by_xpath("//div[@aria-label='Primary']")
assert primary_btn.is_enabled(),"Failed the test case"
primary_btn.click()
total_count=driver.find_element_by_xpath("//div[@aria-label='Show more messages']").text
print("Total count of the emails present in the inbox",total_count[7:])
def inbox():
    sender_lst = []
    subject_lst = []
    subject_mail = driver.find_elements_by_xpath("//tr//td//span[@class='bog']")
    for i in subject_mail:
        data = i.text
        subject_lst.append(data)
    sender_mail = driver.find_elements_by_xpath("//tr//td//span[@class='bA4']")
    for i in sender_mail:
        data = i.text
        sender_lst.append(data)
    print("name of the senders", sender_lst)
    print("===============================================")
    print("Subject of the mails", subject_lst)

inbox()
driver.close()