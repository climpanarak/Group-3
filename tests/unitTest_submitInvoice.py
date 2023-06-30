'''Navigate to the Invoice Submission page, populate required fields, and confirm submission'''

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
        # navigate to the Add Invoice page
        driver.get("https://giese838.pythonanywhere.com/invoice/create")
        time.sleep(2)
        # Populate the Owner field
        ownerDropDown = Select(driver.find_element(By.ID, "id_owner"));
        ownerDropDown.select_by_visible_text("HomerSimpson");
        time.sleep(1)
        # Upload an invoice document
        driver.find_element(By.ID, "id_invoice").send_keys("C:\\Users\\ace24\\Desktop\\Sample Invoice.docx")
        time.sleep(2)
        driver.find_element(By.ID, "id_invoice").submit()
        time.sleep(3)


        try:
            # verify the site navigates to the home page
            mgmtHome = "Management Home"
            get_source = driver.page_source
            if mgmtHome not in get_source:
                raise NoSuchElementException

            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("File upload failed")

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(warnings='ignore')

