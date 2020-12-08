import unittest

from selenium import webdriver

import config


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=config.executable)
        cls.driver.maximize_window()
        cls.driver.get(config.ip)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
