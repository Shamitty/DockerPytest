from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time


# scenarios('../features/fglife_landing_page.feature', 'test_DockerPytest_landing_page_steps.py')
scenarios('../features/fglife_landing_page.feature')

@pytest.mark.Regression
@given(parsers.parse('I have navigated to FGLife "{url}"'))
def test_fglife_url(browser):
    browser.get("https://www.fglife.com/")
    time.sleep(5)

@pytest.mark.SecondScenario
@given(parsers.parse('I have navigated to FGLife Second "{url}"'))
def test_fglife_url_second(browser):
    browser.get("https://www.fglife.com/")
    time.sleep(5)

@given("I have verified that I have made it to the FGLife landing page")
def verify_landing_page(browser):
    h2_elements = browser.find_elements("tag name", "h2")
    
    # Filter for elements containing the desired text
    desired_text = "Who is F&G?"  # Replace with the text you're looking for
    matching_element = next((el for el in h2_elements if desired_text in el.text), None)

    # Assert that the element was found
    assert matching_element is not None, f"No <h2> element found containing text: {desired_text}"
   
    # assert "DockerPytest" in browser.find_element(By.XPATH, "//h2[contains(.,'Who is F&G?')]").text


# @when("I have clicked the Book Equipment tab on the DockerPytest landing page")
# def book_equip_tab(browser):
#     try:
#         browser.find_element(By.XPATH, "//span[contains(.,'Book Equipment')]").click()
#     except:
#         raise NotImplementedError(u'STEP: When I have clicked the Book Equipment tab on the DockerPytest landing page')


# @when("I have clicked the Acknowledgement button on the Equipment Reservations page")
# def step_impl(browser):
#     try:
#         wait = WebDriverWait(browser, 10)
#         wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Acknowledge and Accept')]")))
#         browser.find_element(By.XPATH, "//button[contains(.,'Acknowledge and Accept')]").click()
#     except:
#         raise NotImplementedError(
#             u'STEP: And I have clicked the Acknowledgement button on the Equipment Reservations page')


# @when("I have clicked today on the current reservations tab for the DockerPytest landing page")
# def step_impl(browser):
#     try:
#         ActionChains(browser).move_to_element(
#             browser.find_element(By.ID, "webNavbarDropdown10")).perform()
#         browser.find_elements(By.ID, "selected_day")[0].click()
#         assert "Current Reservations for Today" in browser.find_element(By.XPATH,
#                                                                                "//h1[contains(.,'Current Reservations')]").text
#     except:
#         raise NotImplementedError(
#             u'STEP: And I have clicked today on the current reservations tab for the DockerPytest landing page')


# @when("I have clicked all equipment tab on the DockerPytest landing page")
# def step_impl(browser):
#     try:
#         browser.find_element(By.XPATH, "//span[contains(.,'All Equipment')]").click()
#     except:
#         raise NotImplementedError(u'STEP: And I have clicked all equipment tab on the DockerPytest landing page')


# @when(parsers.parse('I have entered "{equipment}" in the filtered entries textbox on the All Equipment page'))
# def step_impl(browser, equipment):
#     try:
#         browser.find_element(By.CSS_SELECTOR, "input[aria-label*='Filter entries']").send_keys(equipment)
#     except:
#         raise NotImplementedError(
#             u'STEP: And I have entered "5055D" in the filtered entries textbox on the All Equipment page')


# @when("I have clicked the Admin tab on the DockerPytest landing page")
# def step_impl(browser):
#     try:
#         browser.find_element(By.XPATH, "//span[contains(.,'Admin')]").click()
#         assert "Enter Password to Access Admin Features" in browser.find_element(By.XPATH,
#                                                                                         "//h5[contains(.,'Enter Password to Access Admin Features')]").text
#     except:
#         raise NotImplementedError(u'STEP: And I have clicked the Admin tab on the DockerPytest landing page')


# @when("I have clicked the FAQ tab on the DockerPytest landing page")
# def step_impl(browser):
#     try:
#         browser.find_element(By.XPATH, "//span[contains(.,'FAQ')]").click()
#     except:
#         raise NotImplementedError(u'STEP: And I have clicked the FAQ tab on the DockerPytest landing page')


# @then(parsers.parse('I verified "{text}" on the FAQ page'))
# def step_impl(browser, text):
#     try:
#         assert text in browser.find_element(By.XPATH, "//h1[contains(.,'Frequently Asked Questions')]").text
#         done_text = browser.find_element(By.XPATH, "//h1[contains(.,'Frequently Asked Questions')]").text
#         print(f"Done mf asdfasdfasdf {done_text}")
#     except:
#         raise NotImplementedError(u'STEP: Then I verified "Frequently Asked Questions" on the FAQ page')
