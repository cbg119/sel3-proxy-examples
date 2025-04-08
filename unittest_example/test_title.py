import os
import unittest
from selenium import webdriver

class SauceDemo(unittest.TestCase):
    def test_title(self):
        #Use HTTP endpoint to validate resolve_ip workaround
        SAUCE_URL = "http://ondemand.us-west-1.saucelabs.com:80/wd/hub"

        capabilities = {
            "browserName": "chrome",
            "browserVersion": "latest",
            "platformName": "Windows 11",
            "sauce:options": {
                "name": "Unittest Proxy Example",
                "username": os.environ["SAUCE_USERNAME"],
                "accessKey": os.environ["SAUCE_ACCESS_KEY"]
            }
        }

        driver = webdriver.Remote(command_executor=SAUCE_URL, desired_capabilities=capabilities)

        driver.get("https://saucedemo.com")
        title = driver.title
        titleIsCorrect = "Swag Labs" in title
        jobStatus = "passed" if titleIsCorrect else "failed"

        driver.execute_script("sauce:job-result=" + jobStatus)
        driver.quit()
        self.assertTrue(titleIsCorrect)

if __name__ == "__main__":
    unittest.main()