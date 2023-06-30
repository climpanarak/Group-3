'''Navigate to the Application Submission page, populate required fields, and confirm submission'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        driver = self.driver
        driver.maximize_window()
        user = "testaccount"
        pwd = "accounttester"
        driver.get("https://giese838.pythonanywhere.com/accounts/login/")
        time.sleep(2)
        elem = driver.find_element(By.ID,"id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID,"id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        # navigate to the Application Submission page
        driver.find_element(By.XPATH, "//a[contains(., 'Application Submission')]").click()
        time.sleep(2)
        # Populate the 3 required fields
        firstName = "Marge"
        emailAddress = "marge@home.com"

        elem = driver.find_element(By.ID, "id_name")
        elem.send_keys(firstName)
        elem = driver.find_element(By.ID, "id_email")
        elem.send_keys(emailAddress)

        propertyDropDown = Select(driver.find_element(By.ID, "id_property"));
        propertyDropDown.select_by_visible_text("The Simpsons House");
        time.sleep(3)
        elem.send_keys(Keys.RETURN)

        try:
            # get the page source to search if the submitted name is displayed on the applications page
            get_source = driver.page_source
            if firstName not in get_source:
                raise NoSuchElementException
            time.sleep(3)
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Login Failed - user may not exist")

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(warnings='ignore')

