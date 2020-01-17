Feature: Login into Female Daily application
  As a female daily user
  I want to login with my credentials
  So that, I can see female daily user page

  Background:
    Given I load the female daily web application

    Scenario: I can load female daily web application
      When I click login button
      Then I should be on the Login form page
      Then I should see the email text field
      Then I should see the password text field
      Then I should see login button
      Then I should be able to input my email address
      Then I should be able to input my password
      Then I click login button
      Then I should be see user home page
