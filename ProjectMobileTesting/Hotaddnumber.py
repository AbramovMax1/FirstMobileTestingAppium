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


class addcontacttest2(unittest.TestCase):
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

    def testaddcontect1(self):
        # creating contact with using phone number we get already from test 1
        hotnumber1 = self.HotInfo.hotnumber()
        # press on the plus button the create contact
        self.MobileEle.create_contact_button()
        # enter text on the contact list
        self.MobileEle.create_contact_info_companyname()
        self.MobileEle.create_contact_info_phone(hotnumber1)
        # saving the info about the contact
        self.MobileEle.save_create_contact_info()
        # closing the popup
        self.MobileEle.close_pop_up()
        # taking the name from text
        companyname1 = self.MobileEle.contact_name_large()
        # make sure that the name that I gave in sting the same like in the contact info
        self.assertEqual('HOT', companyname1)











