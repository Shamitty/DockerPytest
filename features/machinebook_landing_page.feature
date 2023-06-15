Feature: MachineBook
    As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

    Background: MachineBook Url
        Given I have navigated to MachineBook "<Enter URL Here>"
        And I have verified that I have made it to the MachineBook landing page

    @MachineBookLandingPage @Regression
    Scenario: Navigate to the landing page
        When I have clicked the Book Equipment tab on the MachineBook landing page
        And I have clicked the Acknowledgement button on the Equipment Reservations page
        And I have clicked today on the current reservations tab for the MachineBook landing page
        And I have clicked all equipment tab on the MachineBook landing page
        And I have entered "5055D" in the filtered entries textbox on the All Equipment page
        And I have clicked the Admin tab on the MachineBook landing page
        And I have clicked the FAQ tab on the MachineBook landing page
        Then I verified "Frequently Asked Questions" on the FAQ page