from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage():
    BASE_URL = "<Enter URL Here>"

    PAGE_URLS = {
        "home": BASE_URL + "/",
        "checkboxes": BASE_URL + "/checkboxes",
        "dropdown": BASE_URL + "/dropdown",
        "dynamic controls": BASE_URL + "/dynamic_controls",
        "form authentication": BASE_URL + "/login",
        "inputs": BASE_URL + "/inputs",
        "secure area": BASE_URL + "/secure"
    }

    def __int__(self, browser):
        self.browser = browser