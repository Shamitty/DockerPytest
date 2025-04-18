Feature: FGLife
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

    @Regression
    Scenario: FGLife Url
        Given I have navigated to FGLife "https://www.fglife.com/"
        And I have verified that I have made it to the FGLife landing page

    @SecondScenario
    Scenario: FGLife Url Second
        Given I have navigated to FGLife Second "https://www.fglife.com/"
        And I have verified that I have made it to the FGLife landing page
