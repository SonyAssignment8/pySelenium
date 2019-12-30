from Netmeds.commonlib import commonlibrary
from Netmeds.jsonnetmeds_read import GenericLib
import time

class NetMeds:
    def Read_data(self):
        self.b = GenericLib()
        self.driver = self.b.choose_browser()
        self.base_url = self.b.read_property('login','url')
        self.sign_in = self.b.read_property('login','sign_in')
        self.Frame_id=self.b.read_property('login',"frame_id")
        self.click_frame=self.b.read_property('login',"click_frame")
        self.mobile_id=self.b.read_property('login',"mobile_id")
        self.mobile_num=self.b.read_property('login',"mobile_num")
        self.password_click=self.b.read_property('login',"password_click")
        self.psw_id=self.b.read_property('login',"psw_id")
        self.password_send=self.b.read_property('login',"password_send")
        self.signin_click=self.b.read_property('login',"signin_click")
        self.PersonalCare=self.b.read_property('PersonalCare','Personal_Care')
        self.click_product=self.b.read_property('PersonalCare','click_product')
        self.AddToCart=self.b.read_property('PersonalCare','AddToCart')
        self.verify_cart=self.b.read_property('PersonalCare','verify_cart')
        self.uploadprescription=self.b.read_property('uploadprescription','uploadprescription_id')
        self.click_uploadprescription=self.b.read_property('uploadprescription','click_uploadprescription')
        self.click_gallery=self.b.read_property('uploadprescription','click_gallery')


    def Login(self):
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        time.sleep(10)
        self.driver.switch_to_frame(self.Frame_id)
        self.driver.find_element_by_id(self.click_frame).click()
        self.driver.find_element_by_xpath(self.sign_in ).click()
        self.driver.find_element_by_id(self.mobile_id).send_keys(self.mobile_num)
        self.driver.find_element_by_xpath(self.password_click).click()
        self.driver.find_element_by_id(self.psw_id).send_keys(self.password_send)
        self.driver.find_element_by_xpath(self.signin_click).click()


    # def personalcare(self):
    #     self.driver.find_element_by_xpath(self.PersonalCare).click()
    #     self.driver.find_element_by_xpath(self.click_product).click()
    #     self.driver.find_element_by_xpath(self.AddToCart).click()
    #
    #     act_msg=self.driver.current_url
    #     exp_msg='https://www.netmeds.com/checkout/cart'
    #     assert act_msg in exp_msg,print("fail")
    #     print("pass")
    
    def upload_prescription(self):
        self.driver.find_element_by_id(self.uploadprescription).click()
        self.driver.find_element_by_xpath(self.click_uploadprescription).click()
        self.driver.find_element_by_xpath(self.click_gallery).click()

n=NetMeds()
n.Read_data()
n.Login()
#n.personalcare()
n.upload_prescription()