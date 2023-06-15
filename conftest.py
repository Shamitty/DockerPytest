import pytest
import selenium.webdriver
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pytest_bdd import given, then, parsers
from pages.base import BasePage
import urllib3
import backoff


#@backoff.on_exception(
   # backoff.expo,
   # urllib3.exceptions.MaxRetryError,
  #  jitter=backoff.full_jitter,
 #   max_time=600
#)

#def pytest_addoption(parser):
#    parser.addoption("--browser", action="store")

@pytest.fixture()
def config(request, scope='session'):

    # Read config file
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config


@pytest.fixture()
def browser(config):

    # Initialize the WebDriver instance
    if config['browser'] == 'Remote':
        opts = webdriver.ChromeOptions()
        if config['headless']:
            opts.add_argument('headless')
            b = webdriver.Remote(
                command_executor='http://selenium-hub:4444/wd/hub',
                options=opts
            )
    elif config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        if config['headless']:
            print("should be headless. Need to uncomment")
            opts.add_argument('headless')
            opts.add_argument('no-sandbox')    
        b = webdriver.Chrome(options=opts)
    elif config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        if config['headless']:
            opts.headless = True
        b = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make call wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])
    b.maximize_window()
    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the teardown
    b.quit()




