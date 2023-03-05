@functionaltests
Feature: Asian Paints Login

  Background:
     Given Chrome is opened and Asian Paints app is opened
      When  Customer clicks on login icon


  Scenario: Validate Customer's successful navigation onto Asian Paints landing page
    Then  It shows login page window

  Scenario: Validate Customer is able to click on close button on login page window
      Then  It shows login page window
      Then  Customer clicks on close button on login page window

  Scenario: Validate Customer is able to click on refresh button on Asian Paints web page
      Then  It shows login page window
      And   Customer clicks on refresh button
      Then  It shows Landing page of Asian Paints

  Scenario Outline: Validate Customer enters valid data
      Then  It shows login page window
      When  Customer enters <valid mobile number>
      And   Customer clicks on submit button
      And   Customer enters otp
      And   Customer clicks on submit(1) button
      Then  It shows a popup message of successful login and checks the user name
      And   Customer log out from the app

     Examples:
        | valid mobile number |
        | 8339915251    |
        | 7978616236    |

  Scenario Outline: Validate Customer enters invalid data
      Then  It shows login page window
      When  Customer enters <invalid mobile number>
      And   Customer clicks on submit button
      Then  It shows the error message in login page window
      Then  Customer clicks on close button on login page window

      Examples:
        | invalid mobile number |
        | 45846945784   |
        | 76454677874    |




