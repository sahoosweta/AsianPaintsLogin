import time

from hamcrest import *
from behave import *
from Features.Pages.LoginPageClass import LoginPageClass


# Scenario 2
@then(u'Customer clicks on close button on login page window')
def step_impl(context):
    time.sleep(3)
    clickCloseButton = LoginPageClass(context.driver)
    clickCloseButton.click_close_button()


# Scenario 3
@then(u'Customer clicks on refresh button')
def step_impl(context):
    time.sleep(2)
    refresh=LoginPageClass(context.driver)
    refresh.refresh_button()

@then(u'It shows Landing page of Asian Paints')
def step_impl(context):
    time.sleep(3)
    expectedTitle = "Trusted Wall Painting, Home Painting & Waterproofing in India - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


# Scenario 4 & 5
@when(u'Customer enters {mobilenumber}')
def step_impl(context, mobilenumber):
    time.sleep(3)
    mobilenumberTextBox=LoginPageClass(context.driver)
    mobilenumberTextBox.enter_mobileno_textbox(mobilenumber)

# Scenario 4 & 5 sm process
@when(u'Customer clicks on submit button')
def step_impl(context):
    time.sleep(7)
    submit=LoginPageClass(context.driver)
    submit.click_submit_button()


@then(u'Customer enters otp')
def step_impl(context):
   time.sleep(30)

@step("Customer clicks on submit(1) button")
def step_impl(context):
    time.sleep(25)
    submitOTP=LoginPageClass(context.driver)
    submitOTP.click_submit1_button()


# Scenario 4 valid number
@then(u'It shows a popup message of successful login and checks the user name')
def step_impl(context):
    time.sleep(5)
    loggedinicon = LoginPageClass(context.driver)
    loggedinicon.signedIn()

    time.sleep(5)
    textElement = LoginPageClass(context.driver)
    textElement.get_text()



@step("Customer log out from the app")
def step_impl(context):
    time.sleep(5)
    signOutLink = LoginPageClass(context.driver)
    signOutLink.click_sign_out()


#Scenario 5


@then(u'It shows the error message in login page window')
def step_impl(context):

    time.sleep(3)
    errorMessage = LoginPageClass(context.driver)
    errorMessage.error_message()


