import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.bluestone.com/")
driver.maximize_window()

# Move the cursor All Jewellery
all_jewel = driver.find_element_by_xpath("//a[@title='Jewellery']")
act = ActionChains(driver)
act.move_to_element(all_jewel).perform()

# select Kadas and click on it
driver.find_element_by_xpath("//span[text()='Kadas']").click()

# select any kada.
driver.find_element_by_xpath("//img[@alt='The Alok Kada For Him']").click()

# Select Bangle size
child_win = driver.window_handles[1]
driver.switch_to.window(child_win)
driver.find_element_by_xpath("//span[@class='size-box-overlay']").click()
driver.find_element_by_xpath('''//span[text()='2-10(2 10/16")']''').click()
selected_size = driver.find_element_by_xpath('''//span[text()='2-10(2 10/16")']''').text

# click on 'buy now'
driver.find_element_by_xpath("//input[@value='Buy Now']").click()
size_cart_page = driver.find_element_by_xpath('''//span[text()='2-10(2 10/16")']''').text

# Compare both the sizes
assert selected_size == size_cart_page, "The size of item in cart page and selected size is not same"
print("The size of item in cart page and selected size is same")

# Close the browser
driver.close()
