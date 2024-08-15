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


class editaccounttest5(unittest.TestCase):
    def setUp(self):
        # Appium setup
        self.appDriver = Awebdriver.Remote(appium_server_url_local, capabilities)
        self.MobileEle = mobileElements(self.appDriver)

    def tearDown(self):
        if self.appDriver:
            self.appDriver.quit()

    def testedit1(self):
        # choose and click on the  contact we want to edit
        self.MobileEle.click_on_contact()
        # close popup
        self.MobileEle.close_pop_up()
        # click on the pencil to edit out contact
        self.MobileEle.click_contact_edit_button()
        # edit the contact company name from HOT to hot with small latter's
        self.MobileEle.delete_contact_info_companyname()
        self.MobileEle.edit_contact_info_companyname().click()
        self.MobileEle.edit_contact_info_companyname().send_keys('hot')
        # press save
        self.MobileEle.save_create_contact_info()
        # give us the name in the large text under the image of the contact
        name1 = self.MobileEle.contact_name_large()
        # check if the name 'HOT' changed with the name we gave in our situation is 'hot'
        self.assertEqual('hot', name1)
        # go back one page
        self.appDriver.back()
        sleep(3)
        # check if the contact is there and not was deleted by accident
        self.assertIsInstance(self.MobileEle.contact(), Awebdriver.WebElement)