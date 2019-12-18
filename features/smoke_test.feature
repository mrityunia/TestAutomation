Feature: Web Smoke Test cases

  In order to perform Smoke Testing as an end user on GAM
I want to run the automated features of GAM

  Background:
    Given the user has navigated to the page "GAM dashboard"
     Then the user sees the page url contains "GAM"
     Then the user sees the "GAM" in the PageSource

  @chrome
  Scenario: Exported CSV file should have the same number of rows as the Now Showing message
    Given the user has captured the now showing xxxx items number on the GAM home screen
     When the user has exports the CSV file from GAM
     Then the user sees that the number of rows in the CSV is equal to the "Now showing xxxx items" plus one
      And the user deletes the CSV file