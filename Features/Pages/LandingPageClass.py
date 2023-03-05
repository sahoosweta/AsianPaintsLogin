from selenium.webdriver.common.by import By


class LandingPageClass:


    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
        self.loginIcon = "//span[@class='spriteIcon-Firstfold profileIcon']"

        self.loginText = "(//h2[@class='modal-title'])[4]"

        self.iframe = "//iframe[@class='__st_preview_frame_bpn']"

        self.allowButton = "//input[@name='continue']"

     # Creating Element Methods

    def click_login_icon(self):
        loginIconClick = self.driver.find_element(By.XPATH, self.loginIcon)
        loginIconClick.click()

    def check_login_text(self):
        validloginText = self.driver.find_element(By.XPATH, self.loginText)
        print(validloginText.text)
        return (validloginText.text)


    def iframehandle(self):
        iframe = self.driver.find_element(By.XPATH, self.iframe)
        self.driver.switch_to.frame(iframe)

    def click_allow(self):
        allow = self.driver.find_element(By.XPATH, self.allowButton)
        allow.click()




