
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Jyoti\AppData\Local\Programs\Python\Python35\Scripts\chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://www.gmail.com")
driver.find_element_by_name('identifier').send_keys('jyoti08.sahu')
driver.find_element_by_xpath('//span[text()="Next"]').click()
driver.find_element_by_name('password').send_keys("jyoti@0802")
count = 5
while count<=5:
    try:
        driver.find_element_by_xpath('//span[text()="Next"]').click()
        count +=1
        break
    except Exception:
        print("Handled")
driver.find_element_by_xpath("//span[@class='gb_Ia gbii']").click()
driver.find_element_by_xpath("//a[text()='Sign out']").click()
print("Success")
