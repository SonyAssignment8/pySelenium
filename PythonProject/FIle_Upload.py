# Import statements
import autoit
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

# Creating Driver object
driver = webdriver.Chrome("./chromedriver.exe")

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

autoit.win_wait("[CLASS:#32770]", 3)
autoit.control_send("[CLASS:#32770]", "Edit1", "Java Interview Questions.pdf")
autoit.control_click("[CLASS:#32770]", "Button1")
