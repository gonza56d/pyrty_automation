import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        cls.driver.maximize_window()
        cls.driver.get('localhost:8000')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
