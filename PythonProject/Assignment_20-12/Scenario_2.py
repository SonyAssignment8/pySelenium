# Import statements
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

# Creating Driver object
driver = webdriver.Chrome()

# Navigate to URL
driver.implicitly_wait(20)
driver.get("https://www.gmail.com")
driver.maximize_window()

# Login to application
driver.find_element_by_name('identifier').send_keys('jyoti08.sahu')
driver.find_element_by_xpath('//span[text()="Next"]').click()
driver.find_element_by_name('password').send_keys("jyoti@0802")
count = 5
while count <= 5:
    try:
        driver.find_element_by_xpath('//span[text()="Next"]').click()
        count += 1
        break
    except:
        print("Handled")

# Verify that gmail is logged in successfully
exp_Title = 'Inbox - jyoti08.sahu@gmail.com - Gmail'
time.sleep(2)
act_Title = driver.title
if act_Title.__contains__(exp_Title):
    print("PASS--Logged in to Gmail successfully")
else:
    print("PASS--Login not successful")

# Click compose button
driver.find_element_by_xpath("//div[text()='Compose']").click()
driver.find_element_by_xpath("//img[@aria-label='Full-screen (Shift for pop-out)']").click()

# verify that a new mail window is opened
exp_txt = 'New Message'
act_txt = driver.find_element_by_xpath("//div[text()='New Message']").text
if act_txt == exp_txt:
    print(" A new mail window is opened ")
else:
    print(" A new mail window is not opened ")

# Enter email-ID, subject and body
time.sleep(2)
driver.find_element_by_xpath("//textarea[@aria-label='To']").send_keys("jyoti.s@testyantra.in")
driver.find_element_by_xpath("//input[@name='subjectbox']").send_keys("Test Mail")
driver.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys('''Hi,
This is a test mail''')

# click on 'Send' button
driver.find_element_by_xpath("//div[@aria-label='Send ‪(Ctrl-Enter)‬']").click()
print("Mail sent successfully")

# Logout from the application
driver.find_element_by_xpath("//span[@class='gb_Ia gbii']").click()
driver.find_element_by_xpath("//a[text()='Sign out']").click()
print("Success")
