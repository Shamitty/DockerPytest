from pages.base import BasePage
from selenium.webdriver.common.by import By

class LandingPage(BasePage):

    FGLIFE_LANDING_TEXT = (By.ID, "logo")

    def __init__(self, browser):
        self.browser = browser

    def get_fglife_text(self):
        self.browser.find_element(*self.FGLIFE_LANDING_TEXT)

