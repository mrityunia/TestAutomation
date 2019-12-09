Feature: Web Smoke Test cases

  Background:
    Given The user opens application
     Then application is opened
  @Chrome
  @Smoke
  @UI
  Scenario: verify the user is able to login
    Given  the user clicks on sign in
     When the user enters user id and password
      | UserId      | Password |
      | xyz@abc.com | xyzas124 |
      And  clicks on SignIn
     Then the user is getting success message

