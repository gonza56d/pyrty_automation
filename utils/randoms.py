import random, string


class Random:

    @staticmethod
    def get_username():
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(11))

    @staticmethod
    def get_email():
        email = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(11))
        domain = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))
        return email+'@'+domain+'.com'

    @staticmethod
    def get_password():
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))
