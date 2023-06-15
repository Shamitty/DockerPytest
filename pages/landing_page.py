from pages.base import BasePage
from selenium.webdriver.common.by import By

class LandingPage(BasePage):

    MACHINEBOOK_LANDING_TEXT = (By.ID, "MachineBook")

    def __init__(self, browser):
        self.browser = browser

    def get_machinebook_text(self):
        self.browser.find_element(*self.MACHINEBOOK_LANDING_TEXT)

