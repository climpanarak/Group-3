'''Search for images on the Property Details page'''

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
        # navigate to the Property List page
        driver.find_element(By.XPATH, "//a[contains(., 'Property List')]").click()
        time.sleep(2)
        # Click a particular property link
        driver.find_element(By.XPATH, "//a[contains(., 'The Simpsons House')]").click()
        time.sleep(3)

        try:
            # Find an image element to verify its existence
            findImage = driver.find_elements(By.XPATH,"//img")
            findImageCount = len(findImage)
            print(findImageCount)
            # evaluate if there is at least one image on the page
            if findImageCount < 1:
                raise NoSuchElementException
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Edit Author button does not navigate to the update page")

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()