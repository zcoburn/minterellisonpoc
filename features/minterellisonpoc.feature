Feature: Automated smoke testing - Sydney Metro (live)
Scenario: Primary Navigation
      Given Go to Test URL
      When  Homepage is displayed
      Then  Validate homepage
      Then  Perform a search
      Then  Validate search result
