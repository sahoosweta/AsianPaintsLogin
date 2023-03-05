Feature: Asian Paints Login
  Scenario: Validate Customer enters valid data
      Given Chrome is opened and Asian Paints app is opened
      When  User clicks on login icon for first dataset
      Then  It shows login page window for first dataset
      When  User enters mobile number for first dataset
      And   User clicks on submit button for first dataset
      And   User enters otp for first dataset
      And   User clicks on submit(1) button for first dataset
      Then  It shows a popup message of successful login for first data set and sign out from the app



  Scenario: Validate Customer enters invalid data
      Given Chrome is opened and Asian Paints app is opened
      When  User clicks on login icon for second dataset
      Then  It shows login page window for second dataset
      When  User enters mobile number for second dataset
      And   User clicks on submit button for second dataset
      Then  It shows the error message in login page window for second dataset
      Then  User clicks on close button on login page window for second dataset

