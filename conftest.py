import pytest
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def open_config():

    # Read config file
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config

def get_available_browsers():
    response = requests.get("http://localhost:4444/grid/api/hub")
    data = response.json()
    browsers = []
    for node in data['nodes']:
        for capability in node['capabilities']:
            browsers.append(capability['browserName'])
    return set(browsers)

def get_localization_execution(config):
    json_config = config['localization']
    if json_config:
        return "localhost"
    else:
        return "selenium-hub"

@pytest.fixture(params=["chrome", "firefox", "edge"])
def browser(request):
    browser_name = request.param
    json_config = open_config()
    browser_config_name = json_config['browser_config_name']
    execution_url = get_localization_execution(json_config)
    
    if browser_config_name == "Remote":
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')  # Run in headless mode if required
            options.add_argument('--no-sandbox')
            driver = webdriver.Remote(
                command_executor=f"http://{execution_url}:4444/wd/hub",
                options=options
            )
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            options.headless = True  # Enable headless mode
            driver = webdriver.Remote(
                command_executor=f"http://{execution_url}:4444/wd/hub",
                options=options
            )
        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
            driver = webdriver.Remote(
                command_executor=f"http://{execution_url}:4444/wd/hub",
                options=options
            )

    elif browser_config_name == "Local":      
    # Configure browser-specific options
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            # options.add_argument('--headless')  # Run in headless mode if required
            options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()), options=options
            )
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument('--no-sandbox')
            # options.headless = True  # Enable headless mode
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()), options=options
            )
        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()), options=options
            )
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # Configure implicit wait and maximize window
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver

    # Quit the browser after the test
    driver.quit()
    
