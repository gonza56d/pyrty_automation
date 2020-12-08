import config

class SignupPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = config.ip

    def open(self):
        self.driver.get(self.url)

    def signup(self, username, email, password):
        self.username_field.clear()
        self.username_field.send_keys(username)
        self.email_field.clear()
        self.email_field.send_keys(email)
        self.password_field.clear()
        self.password_field.send_keys(password)
        self.signup_button.click()

    @property
    def account_registered_displayed(self):
        return self.driver.find_element_by_xpath(
            "//div[contains(@class, 'alert-dismissible') and contains(text(), 'Account registered successfully.')]"
        ).is_displayed()

    @property
    def username_taken_displayed(self):
        return self.driver.find_element_by_xpath(
            "//li[contains(text(), 'username already exists.')]"
        ).is_displayed()

    @property
    def email_taken_displayed(self):
        return self.driver.find_element_by_xpath(
            "//li[contains(text(), 'email is already taken')]"
        ).is_displayed()

    @property
    def username_field(self):
        return self.driver.find_element_by_id('id_username')

    @property
    def email_field(self):
        return self.driver.find_element_by_id('id_email')

    @property
    def password_field(self):
        return self.driver.find_element_by_id('id_password')

    @property
    def signup_button(self):
        return self.driver.find_element_by_xpath(
            "//button[contains(text(),'Sign up') and contains(@class, 'btn-block')]")
