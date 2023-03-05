import time
from behave import *
from Features.Pages.LandingPageClass import LandingPageClass
from Features.Pages.LoginPageClass import LoginPageClass
from DataFiles import ExcelUtils
from Features.Utility.ConfigClass import ConfigClass


# Scenario 1 for ecxel
@when(u'User clicks on login icon for first dataset')
def step_impl(context):
    time.sleep(2)

    landingPage = LandingPageClass(context.driver)
    landingPage.click_login_icon()


@then(u'It shows login page window for first dataset')
def step_impl(context):
    time.sleep(2)

    loginPageWindow = LandingPageClass(context.driver)
    loginPageWindow.check_login_text()

@when(u'User enters mobile number for first dataset')
def step_impl(context):
    time.sleep(3)
    mnumber= LoginPageClass(context.driver)
    mnumber.mobiletextboxFirst_excel()


@when(u'User clicks on submit button for first dataset')
def step_impl(context):
    time.sleep(5)
    submit = LoginPageClass(context.driver)
    submit.click_submit_button()

@when(u'User enters otp for first dataset')
def step_impl(context):
    time.sleep(30)


@when(u'User clicks on submit(1) button for first dataset')
def step_impl(context):
    time.sleep(5)
    submitOTP = LoginPageClass(context.driver)
    submitOTP.click_submit1_button()


@then(u'It shows a popup message of successful login for first data set and sign out from the app')
def step_impl(context):

    time.sleep(3)
    loggedIn = LoginPageClass(context.driver)
    loggedIn.signedIn()

    time.sleep(2)
    textElement = LoginPageClass(context.driver)
    textElement.get_text()

    time.sleep(2)
    loggedIn = LoginPageClass(context.driver)
    loggedIn.signedIn()

    time.sleep(2)
    signOutLink = LoginPageClass(context.driver)
    signOutLink.click_sign_out()

    time.sleep(7)

    expectedTitle = "Trusted Wall Painting, Home Painting & Waterproofing in India - Asian Paints"
    actualTitle = context.driver.title
    try:
        if (expectedTitle == actualTitle):
            assert True
            print("Test is passed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 3, "Passed")
        else:
            print("Test is failed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 3, "Failed")
            assert False
    finally:
        print("page title is" + actualTitle)
        time.sleep(1)


# Scenario 2 for excel file

@when(u'User clicks on login icon for second dataset')
def step_impl(context):
    time.sleep(2)
    landingPage = LandingPageClass(context.driver)
    landingPage.click_login_icon()


@then(u'It shows login page window for second dataset')
def step_impl(context):
    time.sleep(2)
    loginPageWindow = LandingPageClass(context.driver)
    loginPageWindow.check_login_text()

@when(u'User enters mobile number for second dataset')
def step_impl(context):
   time.sleep(5)
   mobilenumber=LoginPageClass(context.driver)
   mobilenumber.mobiletextboxSecond_excel()


@when(u'User clicks on submit button for second dataset')
def step_impl(context):
    time.sleep(5)
    submit = LoginPageClass(context.driver)
    submit.click_submit_button()


@then(u'It shows the error message in login page window for second dataset')
def step_impl(context):
    time.sleep(2)
    errorMessage = LoginPageClass(context.driver)
    errorMessage.error_message()


@then(u'User clicks on close button on login page window for second dataset')
def step_impl(context):
    time.sleep(1)
    clickCloseButton = LoginPageClass(context.driver)
    clickCloseButton.click_close_button()
    time.sleep(2)
    expectedTitle = "Trusted Wall Painting, Home Painting & Waterproofing in India - Asian Paints"
    actualTitle = context.driver.title
    try:
        if (expectedTitle == actualTitle):
            assert True
            print("Test is passed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 3, "Passed")
        else:
            print("Test is failed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 3, "Failed")
            assert False
    finally:
        print("page title is" + actualTitle)
        time.sleep(1)



