from ScriptUsingPythonSelenium.BaseClass import*
#launch the browser
driver.get("http://localhost:8888/")
#Enter the manditory details and login to the application
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("user_password").send_keys("manager")
driver.find_element_by_id("submitButton").click()

#click on contact link
driver.find_element_by_xpath("//a[text()='Contacts']").click()

#click on "+" symbol to create contact
driver.find_element_by_xpath("//img[@alt='Create Contact...']").click()

#enter the manditary details click on save button
driver.find_element_by_name("lastname").send_keys("krishna")
driver.find_element_by_xpath("//input[@title='Save [Alt+S]']").click()
#click on contact button to go back to contacts page
driver.find_element_by_xpath("//table[@class='small']/tbody/tr/td/a[text()='Contacts']").click()
lst=driver.find_elements_by_xpath("//span[@vtfieldname='lastname']/..")
print(lst)
for i in lst:
    if i.text=="krishna":
        print("contact is created successfully..")

driver.close()

