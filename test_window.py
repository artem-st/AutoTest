import pytest
import time
from selenium import webdriver
from definitions import *


class TestClass:

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        self.driver = webdriver.Firefox(ROOT_DIR)
        yield
        self.driver.quit()

    def test_comment(self):
        self.driver.get(APP_URL)

        for x in range(0, 50):
            window_button = self.driver.find_elements_by_xpath("//*[contains(@class, 'NPS__button n')]")
            if len(window_button) == 0:
                self.driver.delete_all_cookies()
                self.driver.refresh()
                self.driver.get(APP_URL)
                time.sleep(1)
            else:
                break

        window_button.__getitem__(0).click()
        message = self.driver.find_element_by_xpath("//*[contains(@id, 'feedbackTextarea')]")
        message.send_keys("test")
        self.driver.find_element_by_xpath("//*[contains(@class, 'NPS__feedback-send')]").click()
        time.sleep(1)
        assert self.driver.find_element_by_xpath("//*[contains(@class, 'NPS__feedback-send')]").is_displayed() == False


    def test_rate(self):
            self.driver.get(APP_URL)
            for x in range(0, 50):
                window_button = self.driver.find_elements_by_xpath("//*[contains(@class, 'NPS__button n')]")
                if len(window_button) == 0:
                    self.driver.delete_all_cookies()
                    self.driver.refresh()
                    self.driver.get(APP_URL)
                    time.sleep(1)
                else:
                    break
            window_button.__getitem__(9).click()
            time.sleep(1)
            assert self.driver.find_element_by_xpath("//*[contains(@class, 'NPS__button n')]").is_displayed() == False
