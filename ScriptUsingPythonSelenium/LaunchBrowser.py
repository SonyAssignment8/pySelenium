from ScriptUsingPythonSelenium.BaseClass import*
driver.implicitly_wait(20)
driver.get("http://www.gmail.com")
driver.find_element_by_id("identifierId").send_keys("htkrishnakumara")
driver.find_element_by_xpath("//span[text()='Next']").click()
driver.find_element_by_name("password").send_keys("Krishna@123")
count=0
while count<=10:
    try:
        driver.find_element_by_xpath("//span[text()='Next']").click()
        break
    except Exception:
        count+=1



