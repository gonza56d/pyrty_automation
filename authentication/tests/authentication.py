import unittest
from pyunitreport import HTMLTestRunner

from selenium.common.exceptions import NoSuchElementException
from authentication.pom import LoginPage
from authentication.tests import BaseTest
from utils.randoms import Random


class AuthenticationTest(BaseTest):

    def test_fake_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login('jaskdjak', 'alkwdjawkljdl')
        self.assertTrue(login_page.wrong_password_displayed)

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login('gonza56d', 'abc123abc123')
        self.assertTrue(login_page.login_success_displayed)

    def test_fake_signup(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        signup_page = login_page.get_signup()
        signup_page.signup('demo', 'demo@demo.com', 'demodemo')
        self.assertTrue(signup_page.username_taken_displayed)
        self.assertTrue(signup_page.email_taken_displayed)

    def test_signup(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        signup_page = login_page.get_signup()
        signup_page.signup(Random.get_username(), Random.get_email(), Random.get_password())
        try:
            self.assertTrue(signup_page.account_registered_displayed)
        except NoSuchElementException:
            self.test_signup()


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='reports', report_name='login'))
