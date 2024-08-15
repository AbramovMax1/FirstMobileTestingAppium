import unittest
from selenium import webdriver as Swebdriver
from appium import webdriver as Awebdriver
from HOTWebClasses import hotinfo
from PhoneElements import mobileElements
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


appium_server_url_local = "http://localhost:4723/wd/hub"
capabilities = dict(
    platformName="Android",
    deviceName="Pixel7a",
    udid="emulator-5554",
    appActivity="com.google.android.apps.messaging.ui.ConversationListActivity",
    appPackage="com.google.android.apps.messaging",
    platformVersion="35"
)


class sendtexttest4(unittest.TestCase):
    def setUp(self):
        # Appium setup
        self.appDriver = Awebdriver.Remote(appium_server_url_local, capabilities)
        self.MobileEle = mobileElements(self.appDriver)

    def tearDown(self):
        if self.appDriver:
            self.appDriver.quit()

    def testsendsms(self):
        # skip the sign in
        self.MobileEle.text_info_skip_sign_in()
        # click on start chat
        self.MobileEle.text_info_start_chat_button()
        # click on contact
        self.MobileEle.text_info_click_on_contact()
        # send message in our station it's going to be 'Hey'
        self.MobileEle.text_info_send_message()
        # click on send sms
        self.MobileEle.text_info_send_sms_button()
        self.appDriver.back()
        self.appDriver.back()
        # close popup dialog
        self.MobileEle.text_info_close_dialog_popup()
        # check if there is conversion with hot
        self.assertIsInstance(self.MobileEle.text_info_con_with_account(), Awebdriver.WebElement)






