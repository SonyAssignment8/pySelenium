from selenium import webdriver

count = 0
count1 = 0
driver = webdriver.Chrome('C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python35\\Scripts\\chromedriver.exe')
driver.get('http://gmail.com')
driver.implicitly_wait(8)

driver.find_element_by_name('identifier').send_keys('selenium658')
while count < 10:
    try:
        driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
        count += 1
        break
    except Exception:
        print('exception handled')
driver.find_element_by_name('password').send_keys('selenium123')
while count1 < 10:
    try:
        driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
        count1 += 1
        break
    except Exception:
        print('exception handled')


