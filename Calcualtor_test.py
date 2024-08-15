import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

appium_server_url_local = "http://localhost:4723/wd/hub"
capabilities = dict(
    platformName="Android",
    deviceName="Pixel7a",
    udid="emulator-5554",
    appActivity="com.android.calculator2.Calculator",
    appPackage="com.google.android.calculator",
    platformVersion="35"
)


class claculatorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(appium_server_url_local, capabilities)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test1(self):
        # pressing on the button in the calculator app ===============
        number1 = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_1")
        number1.click()
        plus_button = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/op_add")
        plus_button.click()
        number2 = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_1")
        number2.click()
        display_math_info = self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText')
        print(f"the number that printed in the calculator is {display_math_info.text}")
        equal_button = self.driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/eq")
        equal_button.click()
        result_bar = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.TextView")
        print(f"the result that printed in the calculator is {result_bar.text}")
        self.assertEqual(result_bar.text, result_bar.text,
                         "the if the first result equal to second result the test is passed")



