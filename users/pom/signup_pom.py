
class SignupPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'localhost:8000'

    def open(self):
        self.driver.get(self.url)

    # TODO
