'''Scenario 10
1. Open browser
2. Pass url bluestone
3. Goto chat our experts and maximize
4. Maxmize chat our experts
5. Enter the details and click on start chat
6. Enter some message.
7. And print reply in output'''
from selenium import webdriver
class BlueStone:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Safari()

    def launchWebsite(self):
        self.driver.get("https://www.bluestone.com/")
        self.chat()
    def chat(self):
        import time
        self.driver.maximize_window()
        time.sleep(7)
        self.driver.switch_to_frame(self.driver.find_element_by_id("chat-widget"))
        count=0
        while count<=150:
            try:

                self.driver.find_element_by_xpath("//div/p[contains(text(),'CHAT with our experts !')]").click()
                break
            except Exception:
                count+=1

b=BlueStone("chrome")
b.launchWebsite()