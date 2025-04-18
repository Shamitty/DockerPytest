# MkDocs Documentation for FGLife Selenium Test Framework

Based on your workspace, I'll create documentation on how to get started with this Selenium testing project.

## Project Structure

This project is a Selenium-based web testing framework designed to test the FGLife website. It uses:

- Selenium WebDriver for browser automation
- pytest and pytest-bdd for test execution
- Docker and Docker Compose for containerized execution
- Grid setup for parallel test execution

The key files in the workspace are:

- 

conftest.py

 - Core test configuration and fixtures
- 

docker-compose.yml

 - Docker services configuration
- 

fglife_landing_page.feature

 - BDD feature definitions
- 

test_fglife_landing_page_steps.py

 - BDD step implementations

## Getting Started

### Prerequisites

1. Install a code editor (VSCode or PyCharm)
   ```
   https://code.visualstudio.com/download
   ```

2. Install Python and ensure pip is available
   ```
   https://www.python.org/downloads/
   py -m ensurepip --upgrade
   ```

3. Install Docker and Docker Compose
   ```
   https://docs.docker.com/get-docker/
   ```

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Shamitty/DockerPytest.git
   cd DockerPytest
   ```

2. Install required packages
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

The framework can be configured through the 

config.json

 file:

```json
{
  "browser_config_name": "Remote",
  "implicit_wait": 10,
  "localization": false
}
```

- 

browser_config_name

: Choose between "Remote" (uses Selenium Grid) or "Local" (uses local WebDriver)
- `implicit_wait`: Default wait time in seconds
- `localization`: If true, uses localhost instead of selenium-hub

## Running Tests

### Local Execution

To run tests locally:

```bash
pytest step_defs/test_fglife_landing_page_steps.py --disable-warnings --html=reports/dockerpytest.html -k Regression
```

Add `-v -f` options for verbose mode and automatic re-run after file changes:

```bash
pytest step_defs/test_fglife_landing_page_steps.py --disable-warnings --html=reports/dockerpytest.html -k Regression -v -f
```

### Docker Execution

Run tests in Docker with specific tags:

```bash
docker-compose -f docker-compose.yml run -e TAGNAME=Regression --rm dockerpytest_regression && docker-compose rm -fsv
```

Or run multiple tagged tests:

```bash
TAGNAME="@Regression or @SecondScenario" docker-compose --no-cache -f docker-compose.yml run --rm dockerpytest_regression && docker-compose rm -fsv
```

## Test Structure

### Feature Files

BDD-style features are defined in the 

features

 directory. For example:

```gherkin
Feature: FGLife
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.
    @Regression
    Scenario: FGLife Url
        Given I have navigated to FGLife "https://www.fglife.com/"
        And I have verified that I have made it to the FGLife landing page
```

### Step Definitions

Step implementations are in 

test_fglife_landing_page_steps.py

:

```python
@pytest.mark.Regression
@given(parsers.parse('I have navigated to FGLife "{url}"'))
def test_fglife_url(browser):
    browser.get("https://www.fglife.com/")
    time.sleep(5)
```

### Page Objects

Page element definitions are in 

landing_page.py

 using the Page Object Model:

```python
class LandingPage(BasePage):
    FGLIFE_LANDING_TEXT = (By.ID, "logo")

    def __init__(self, browser):
        self.browser = browser

    def get_fglife_text(self):
        self.browser.find_element(*self.FGLIFE_LANDING_TEXT)
```

## Selenium Grid Setup

The project uses Selenium Grid to run tests across multiple browsers. The grid is configured in 

docker-compose.yml

 with:

- Chrome, Firefox and Edge browser nodes
- A central Selenium Hub
- Shared network configuration
- Volume mapping for test reports

## Reporting

Test reports are generated in HTML format in the `reports/` directory.

To view a report after test execution, open the generated HTML file:

```bash
reports/test_report.html
```

## Troubleshooting

- If the browser doesn't connect, check if Selenium Grid is running properly:
  ```bash
  curl http://selenium-hub:4444/grid/api/hub
  ```

- For issues with specific browsers, check docker logs:
  ```bash
  docker-compose logs chrome
  docker-compose logs firefox
  docker-compose logs edge
  ```