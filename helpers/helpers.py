from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By


def wait_for_asdf(self, xpath):
    self._driver_wait.until(EC.element_to_be_clickable((By.XPATH, f"{xpath}")))
    return self._driver.find_element(By.XPATH, xpath)