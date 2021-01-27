Feature: Minter Ellison POC Automated Testing
Scenario: Homepage & Search
      Given Go to Test URL
      When  Homepage is displayed
      Then  Validate homepage
      Then  Perform a search
      Then  Validate search result
