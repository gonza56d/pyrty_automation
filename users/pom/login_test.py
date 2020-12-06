import unittest

from pyunitreport import HTMLTestRunner
from users.pom.login_pom import LoginPage
from users.pom.base_test import BaseTest


class LoginTest(BaseTest):

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

    def test_signup(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        signup_page = login_page.get_signup()
        # TODO test the sign up


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='reports', report_name='login'))
