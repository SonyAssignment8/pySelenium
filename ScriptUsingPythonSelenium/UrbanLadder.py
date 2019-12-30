from ScriptUsingPythonSelenium.BaseClass import*
driver.get("https://www.urbanladder.com/")
lst=driver.find_elements_by_xpath("//div[@id='topnav_wrapper']/ul/li")
for j in lst:
    if j.text=="Living":
        j.click()

lst1=driver.find_elements_by_xpath("//div[@class='subnavlist_wrapper clearfix']")
for i in lst1:
    print(i.text)



