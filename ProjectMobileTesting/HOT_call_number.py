from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
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
    appActivity="com.google.android.dialer.extensions.GoogleDialtactsActivity",
    appPackage="com.google.android.dialer",
    platformVersion="35"
)


class callelaltest1(unittest.TestCase):
    def setUp(self):
        # Appium setup
        self.appDriver = Awebdriver.Remote(appium_server_url_local, capabilities)
        self.MobileEle = mobileElements(self.appDriver)

        # selenium setup
        self.webDriver = Swebdriver.Firefox()
        self.webDriver.get("https://www.hotmobile.co.il/HOTmobile_en/Pages/Contact-Us.aspx")
        self.webDriver.maximize_window()
        self.webDriver.implicitly_wait(10)
        self.HotInfo = hotinfo(self.webDriver)

    def tearDown(self):
        if self.appDriver:
            self.appDriver.quit()

        if self.webDriver:
            self.webDriver.quit()

    def testdailing1(self):
        # dailing to the number
        hotnumber1 = self.HotInfo.hotnumber()
        # open the number section
        self.MobileEle.open_call_section()
        # put the number from the site
        self.MobileEle.dial_number(hotnumber1)
        hotnumber2 = self.MobileEle.the_number_on_the_phone()
        # press on call to the number
        self.assertEqual(hotnumber1, hotnumber2)
        self.MobileEle.click_make_call()
        # press on the stop call
        self.MobileEle.click_hangup_call()
        # go to call history
        self.MobileEle.click_recents_calls()
        # check if there is last call
        self.assertIsInstance(self.MobileEle.last_call(), Awebdriver.WebElement)




