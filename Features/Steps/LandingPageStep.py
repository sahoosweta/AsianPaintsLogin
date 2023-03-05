import time

from hamcrest import *
from behave import *
from Features.Pages.LandingPageClass import LandingPageClass


@given(u'Chrome is opened and Asian Paints app is opened')
def step_impl(context):
    time.sleep(3)
    handleiframe = LandingPageClass(context.driver)
    handleiframe.iframehandle()

    time.sleep(2)
    allowButton = LandingPageClass(context.driver)
    allowButton.click_allow()

    time.sleep(1)
    expectedTitle = "Trusted Wall Painting, Home Painting & Waterproofing in India - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@when(u'Customer clicks on login icon')
def step_impl(context):
    time.sleep(2)
    landingPage = LandingPageClass(context.driver)
    landingPage.click_login_icon()


@then(u'It shows login page window')
def step_impl(context):
    time.sleep(2)
    loginPageWindow = LandingPageClass(context.driver)
    expectedText = "Login"
    actualText = loginPageWindow.check_login_text()
    assert expectedText, actualText




