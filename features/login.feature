# Feature File 
Feature: OTT Login Scenario

Scenario: User enters valid credentials and successfully logs in
    Given the user is on the OTT login page
    When the user enters valid username and password
    And clicks on the login button
    Then the user should be successfully logged in

Scenario: User enters invalid credentials and fails to log in
    Given the user is on the OTT login page
    When the user enters invalid username and password
    And clicks on the login button
    Then the user should see an error message indicating login failure

Scenario: User forgets password and requests a password reset
    Given the user is on the OTT login page
    When the user clicks on the "Forgot Password" link
    And enters their email address
    And clicks on the submit button
    Then the user should receive an email with instructions to reset their password

Scenario: User tries to login with an expired account
    Given the user is on the OTT login page
    And the user's account has expired
    When the user enters valid username and password
    And clicks on the login button
    Then the user should see an error message indicating their account has expired

Scenario: User tries to login with a locked account
    Given the user is on the OTT login page
    And the user's account is locked
    When the user enters valid username and password
    And clicks on the login button
    Then the user should see an error message indicating their account is locked