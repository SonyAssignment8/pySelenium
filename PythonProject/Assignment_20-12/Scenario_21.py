# Import Statements
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

# 1. Open browser
driver = webdriver.Chrome()
driver.implicitly_wait(20)

# 2. Enter URL(bluestone)
driver.get("https://www.bluestone.com/")
driver.maximize_window()

# 3. go to search and search for rings
driver.find_element_by_name("search_query").send_keys("Rings")
driver.find_element_by_xpath("//input[@value='Search']").click()

# 4. move the cursor to price
act = ActionChains(driver)
wb_price = driver.find_element_by_xpath("//span[text()='Price']")
wb_below = driver.find_element_by_xpath("//span[@data-displayname='below rs 10000']")
act.move_to_element(wb_price).click(wb_below).perform()

# 5. get the count of below 10000 Rs
sleep(5)
prdct_count=driver.find_element_by_xpath("//span[@class='total-designs']").text
print("the count of products below 10000 Rs is:",prdct_count[0:2:])

# 6. close Browser
driver.close()