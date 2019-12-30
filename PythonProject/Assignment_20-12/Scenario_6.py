from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.bluestone.com/")

# Move Cursor to Rings Menu
rings_tab = driver.find_element_by_xpath("//a[@title='Rings']")
act = ActionChains(driver)
act.move_to_element(rings_tab).perform()

# Select Diamond Rings and click on it
driver.find_element_by_xpath("//a[@title='Diamond Rings']").click()
act = ActionChains(driver)

# Get Price list By default
default_price = driver.find_elements_by_xpath("//span[@id='bst-discounted-price']")
for i in default_price:
    print(i.text)
print("==============")

# Get Price list price low to high
sort_by = driver.find_element_by_xpath("//span[text()=' Popular ']")
act.move_to_element(sort_by).perform()
driver.find_element_by_xpath("//a[text()='Price Low to High ']").click()

# Getting sorted price
sorted_price_lst =[]
sorted_price = driver.find_elements_by_xpath("//span[@id='bst-discounted-price']")
for i in sorted_price:
    sorted_price_lst.append(i.text)

