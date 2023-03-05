
from Features.Utility.UtilityClass import UtilityClass


def before_scenario(context, driver):
    UtilityClass.launch_browser(context)
    #time.sleep(1)
    context.driver.implicitly_wait(1)

    UtilityClass.maximize_window(context)
    #time.sleep(1)
    context.driver.implicitly_wait(1)

    UtilityClass.launch_app(context)
    #time.sleep(1)
    context.driver.implicitly_wait(2)

def after_scenario(context, driver):
    context.driver.implicitly_wait(3)
    #time.sleep(1)
    UtilityClass.close_browser(context)

