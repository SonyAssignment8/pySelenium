def get_Name_subject():
    # Get the number of email which user and subject details need to be printed
    email_no = int(input("Enter a number in range 1 to ", size))

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

# Checking 'Primary Tab' is selected or not
primary_tab = driver.find_element_by_xpath("//div[@aria-label='Primary']")
time.sleep(4)
exp_txt = 'Primary'
assert primary_tab.text == exp_txt, primary_tab.click()
print("Primary is selected by default")

# Get the message count
msg_count = driver.find_elements_by_xpath("//span[@class='ts']")
print('Total number of mails:',msg_count[2].text)

# Go to mails count and perform mouse over
mouse_over = driver.find_element_by_xpath("//div[@class='J-J5-Ji amH J-JN-I']")
act = ActionChains(driver)
act.move_to_element(mouse_over).perform()

# Click on 'Oldest'
driver.find_element_by_xpath("//div[text()='Oldest']").click()

# Get all the list of mails
mail_list = driver.find_elements_by_xpath("//span[@class='yP']")
size = len(mail_list)

get_Name_subject()

#if 1>= email_no < 50:

# Logout from the application
driver.find_element_by_xpath("//span[@class='gb_Ia gbii']").click()
driver.find_element_by_xpath("//a[text()='Sign out']").click()
print("Success")

