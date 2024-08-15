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
    appActivity="com.android.contacts.activities.PeopleActivity",
    appPackage="com.google.android.contacts",
    platformVersion="35"
)


class deletingaccounttest3(unittest.TestCase):
    def setUp(self):
        # Appium setup
        self.appDriver = Awebdriver.Remote(appium_server_url_local, capabilities)
        self.MobileEle = mobileElements(self.appDriver)

    def tearDown(self):
        if self.appDriver:
            self.appDriver.quit()

    def testdeletingcontact1(self):
        # choose the contact and get inside of it
        self.MobileEle.click_on_contact()
        # click on the 3 dots section
        self.MobileEle.three_dot()
        # click on deleting account
        self.MobileEle.delete_contect()
        # confirm deleting account
        self.MobileEle.confirm_delete()
        # taking the no contact text
        textcontact2 = self.MobileEle.no_contact_yet_text()
        # make sure that the contact name is not exsiting anymore in the contact app
        self.assertEqual('No contacts yet', textcontact2)
