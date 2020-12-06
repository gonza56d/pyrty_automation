from users.pom import SignupPage


class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.url = 'localhost:8000'

    def open(self):
        self.driver.get(self.url)

    @property
    def username_field(self):
        return self.driver.find_element_by_id('id_username')

    @property
    def password_field(self):
        return self.driver.find_element_by_id('id_password')

    @property
    def login_button(self):
        return self.driver.find_element_by_xpath("//i [contains(@class, 'fa-rocket')]/ancestor::button")

    @property
    def signup_button(self):
        return self.driver.find_element_by_xpath("//a[contains(@href, 'signup')]")

    def login(self, username, password):
        self.username_field.clear()
        self.username_field.send_keys(username)
        self.password_field.clear()
        self.password_field.send_keys(password)
        self.login_button.click()

    def get_signup(self):
        self.signup_button.click()
        return SignupPage()

    @property
    def wrong_password_displayed(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Wrong username/password.')]").is_displayed()

    @property
    def login_success_displayed(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Log in success.')]").is_displayed()
