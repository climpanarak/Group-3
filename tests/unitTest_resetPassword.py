'''When “Forgot password” link is clicked, the page should display message that a link was sent to reset password.'''

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
        # open the login page
        driver.get("https://giese838.pythonanywhere.com/accounts/login/")
        time.sleep(3)
        # click the Forgot password link
        driver.find_element(By.XPATH, "//a[contains(., 'Forgot password?')]").click()
        time.sleep(3)
        address = "duffydavis@unomaha.edu"
        elem = driver.find_element(By.ID, "id_email")
        elem.send_keys(address)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        try:
            # verify the page after entering an email address instructs the user of link sent
            # note that the user hasn't logged in
            instructions = "We've emailed you instructions for setting your password"
            get_source = driver.page_source
            if instructions not in get_source:
                raise NoSuchElementException
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("User isn't prompted to login")

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()