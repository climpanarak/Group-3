'''Check for a data element for a profile role'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        # open the home page
        driver.get("https://giese838.pythonanywhere.com")
        time.sleep(3)
        # find 'Sign Up' link and click it
        driver.find_element(By.LINK_TEXT, "Sign Up").click()
        time.sleep(3)

        try:
            # search for the 'role' field
            driver.find_element(By.ID, "id_role")
            driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Login was allowed for an invalid user")

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()