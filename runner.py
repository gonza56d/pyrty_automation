from unittest import TestLoader, TestSuite

from authentication.tests.authentication import AuthenticationTest
from pyunitreport import HTMLTestRunner


assertion_tests = TestLoader().loadTestsFromTestCase(AuthenticationTest)
smoke_test = TestSuite([assertion_tests,])

kwargs = {
    'output': 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
