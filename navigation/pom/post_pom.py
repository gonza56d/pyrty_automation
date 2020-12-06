
class PostPage:

    def __init__(self, driver, post_id):
        self.driver = driver
        self.url = f'http://localhost:8000/posts/{post_id}'

    def open(self):
        self.driver.get(self.url)

    @property
    def post_score(self):
        return int(self.driver.find_element_by_xpath("//div[contains(@class, 'post-score')]").text())

    @property
    def positive_vote_button(self):
        return self.driver.find_element_by_id('btn-post-positive-vote')

    @property
    def negative_vote_button(self):
        return self.driver.find_element_by_id('btn-post-negative-vote')

    @property
    def has_voted_positive(self):
        return self.driver.find_element_by_id('btn-post-positive-vote')\
            .get_attribute('class').contains('btn-warning')

    @property
    def has_voted_negative(self):
        return self.driver.find_element_by_id('btn-post-negative-vote') \
            .get_attribute('class').contains('btn-warning')

    @property
    def comment_box(self):
        return self.driver.find_element_by_xpath("//div[contains(@class, 'ql-editor')]/child::p")
