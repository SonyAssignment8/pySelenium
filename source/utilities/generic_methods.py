import logging
import os
import time
from selenium import webdriver
from traceback import print_stack

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import source.utilities.custom_logger as cl
import selenium.webdriver.support.expected_conditions as EC


class GenericMethods():
    log=cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver
    def screenShot(self,resultMessage):
        """
        Takes screenshot of the current open web page

        """
        fileName=resultMessage+"."+str(round(time.time()*1000))+".png"
        screenshotDirectory="../screenshots/"
        relativeFileName=screenshotDirectory+fileName
        currentDirectory=os.path.dirname(__file__)
        destinationFile=os.path.join(currentDirectory,relativeFileName)
        destinationDirectory=os.path.join(currentDirectory,screenshotDirectory)

        try:
            if not os.path.exists((destinationDirectory)):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("screenshot save to directory:"+destinationFile)
        except:
            self.log.error("### Exception occurred")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self,locatorType):
        locatorType=locatorType.lower()
        if locatorType=="id":
            return By.ID
        elif locatorType=="name":
            return By.NAME
        elif locatorType=="xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator_Type"+locatorType+"not_correct/supported")
        return False

    def getElement(self,locator,locatorType="id"):
        element=None
        try:
            locatorType=locatorType.lower()
            byType=self.getByType(locatorType)
            element=self.driver.find_element(byType,locator)
            self.log.info("Element found with locator:"+locator+"and locator Type"+locatorType)
        except:
            self.log.info("element not found with locator"+locator+"and locator Type"+locatorType)
        return element

    def clearText(self, locator, locatorType="id"):
        try:
            self.getElement(locator,locatorType).clear()
            self.log.info("The text field is cleared with locator:" + locator + "and locator Type" + locatorType)
        except:
            self.log.error("not able to clear")
            print_stack()

    def elementClick(self,locator,locatorType="id"):
        try:
            element=self.getElement(locator,locatorType)
            element.click()
            self.log.info("clicked on element with locator:"+locator+"locatorType:"+locatorType)
        except:
            self.log.info("cannot click on the element with locator:"+locator+"locatorType:"+locatorType)
            print_stack()

    def isElementPresent(self,locator,locatorType="id"):
        try:
            element=self.getElement(locator,locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self,locator,byType):
        try:
            elementList=self.driver.find_elements(byType,locator)
            if len(elementList)>0:
                self.log.info("Element Found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self,locator,locatorType="id",
                       timeout=10,pollFrequency=0.5):
        element=None
        try:
            byType=self.getByType(locatorType)
            self.log.info("waiting for maximum::"+str(time)+
                          "::seconds for element to be clickable")
            wait=WebDriverWait(self.driver,timeout,poll_frequency=pollFrequency,
                               ignored_exceptions=[NoSuchElementException,
                                                   ElementNotVisibleException])
            element=wait.until(EC.element_to_be_clickable((byType,locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element


    def sendKeys(self,data,locator,locatorType="id"):
        try:
            element=self.getElement(locator,locatorType)
            element.send_keys(data)
            self.log.info("sent data on element with locator:"+locator+"locatorType:"+locatorType)
        except:
            self.log.info("cant send data on the element with locator:"+locator+"locatorType:"+locatorType)


    def isElementPresent1(self,locator,locatorType="id"):
        try:
            element=self.getElement(locator,locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")

        except:
            self.log.info("Element not found")
            print_stack()


    def switch_to_child_window(self,driver):
        child_window=None
        parent_window=driver.current_window_handle
        window_ids=driver.window_handles
        try:
            for window_id in window_ids:
                if window_id!=parent_window:
                    child_window=window_id
                    break
            driver.switch_to.window(child_window)
        except Exception:
            self.log.info("unable to change the focus to the child window")
            print_stack()

    def timesleep(self):
        time.sleep(3)