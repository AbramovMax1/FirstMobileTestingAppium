from appium import webdriver as appDriver
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class mobileElements:
    def __init__(self, driver: appDriver.Remote):
        self.appDriver = driver

    # calling process def's =======================================================================================
    def open_call_section(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID, value="com.google.android.dialer:id/dialpad_fab").click()

    def dial_number(self, hotnumber):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.CLASS_NAME,
                                    value="android.widget.EditText").send_keys(hotnumber)

    def click_make_call(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID,
                                    value="com.google.android.dialer:id/dialpad_voice_call_button").click()

    def click_hangup_call(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID, value="com.google.android.dialer:id/incall_end_call").click()

    def the_number_on_the_phone(self):
        sleep(5)
        return self.appDriver.find_element(by=AppiumBy.ID, value="com.google.android.dialer:id/digits").text

    def click_recents_calls(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID,
                                    value='com.google.android.dialer:id/tab_call_history').click()
    def last_call(self):
        sleep(5)
        return self.appDriver.find_element(by=AppiumBy.XPATH,
                                           value='//androidx.cardview.widget.CardView[@content-desc="HOT, Mobile, outgoing call, Just now."]/android.view.ViewGroup')
    # creating contact phone number ================================================================================
    def create_contact_button(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID,
                                    value="com.google.android.contacts:id/floating_action_button").click()

    def create_contact_info_companyname(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.EditText[@text="Company"]').send_keys('HOT')

    def delete_contact_info_companyname(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.XPATH,
                                    value='(//android.widget.ImageView[@content-desc="delete"])[1]').click()

    def edit_contact_info_companyname(self):
        sleep(5)
        return self.appDriver.find_element(by=AppiumBy.XPATH,
                                           value='//android.widget.EditText[@text="Company"]')

    def create_contact_info_phone(self, hotnumber):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.EditText[@text="Phone"]').send_keys(hotnumber)

    def save_create_contact_info(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID, value='com.google.android.contacts:id/toolbar_button').click()

    def contact_name_large(self):
        wait = WebDriverWait(self.appDriver, 10)
        wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.google.android.contacts:id/large_title')))
        return self.appDriver.find_element(by=AppiumBy.ID,
                                           value='com.google.android.contacts:id/large_title').text

    def close_pop_up(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID, value='android:id/closeButton').click()

    def click_on_contact(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.ListView[@resource-id="android:id/list"]/android.view.ViewGroup/android.widget.ImageView').click()

    def contact(self):
        sleep(5)
        return self.appDriver.find_element(by=AppiumBy.XPATH,
                                           value='//android.widget.ListView[@resource-id="android:id/list"]/android.view.ViewGroup/android.widget.ImageView')

    def three_dot(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID,
                                    value='com.google.android.contacts:id/action_bar_overflow_menu').click()

    def delete_contect(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.TextView[@resource-id="com.google.android.contacts:id/title" and @text="Delete"]').click()

    def confirm_delete(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID, value='android:id/button1').click()

    def contact_name_list(self):
        sleep(5)
        return self.appDriver.find_element(by=AppiumBy.XPATH,
                                           value='//android.widget.TextView[@content-desc="H"]').text

    def no_contact_yet_text(self):
        sleep(5)
        wait = WebDriverWait(self.appDriver, 10)
        wait.until(EC.presence_of_element_located((AppiumBy.ID, 'android:id/text1')))
        return self.appDriver.find_element(by=AppiumBy.ID, value='android:id/text1').text

    def click_contact_edit_button(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID,
                                    value='com.google.android.contacts:id/menu_insert_or_edit').click()

    # texting to contact process =====================================================================================
    def text_info_skip_sign_in(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID,
                                    value='com.google.android.apps.messaging:id/secondary_action_button').click()

    def text_info_start_chat_button(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID,
                                    value='com.google.android.apps.messaging:id/start_chat_fab').click()

    def text_info_enter_number(self, hotnumber):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID,
                                    value='ContactSearchBar').send_keys(hotnumber)

    def text_info_click_on_contact(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.XPATH,
                                    value='//android.view.View[@resource-id="contact_row_test_prefix_31"]/android.view.View/android.view.View[1]').click()

    def text_info_send_message(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID,
                                    value='com.google.android.apps.messaging:id/compose_message_text').send_keys("Hey")

    def text_info_send_sms_button(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID,
                                    value='com.google.android.apps.messaging:id/send_message_button_icon').click()

    def text_info_con_with_account(self):
        sleep(5)
        return self.appDriver.find_element(by=AppiumBy.ID,
                                           value='com.google.android.apps.messaging:id/swipeableContainer')

    def text_info_close_dialog_popup(self):
        sleep(5)
        self.appDriver.find_element(by=AppiumBy.ID,
                                    value='com.google.android.apps.messaging:id/legal_fyi_close_btn').click()


