from selenium import webdriver
from selenium.webdriver.common.by import By


class hotinfo:
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def hotnumber(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[href='https://bit.ly/3UNguhE']").text.replace("-", "-")




