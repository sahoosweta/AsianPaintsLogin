from selenium.webdriver.common.by import By
from DataFiles import ExcelUtils
from Features.Utility.ConfigClass import ConfigClass
class LoginPageClass:

    def __init__(self, driver):

        self.driver = driver

        self.dataFilePath = ConfigClass.dataFilePath

        # Element locator
        self.closeButton = "(//a[@data-dismiss='modal'])[5]"

        self.mobileNumberTextBoxElement = "//*[@id='loginMobile']"

        self.submitButtonElement = "//button[@class='ctaText modal__variant-login--submit']"

        self.submitButtonElement1 = "//button[@class='ctaText validate-login  modal__variant-login--submit']"

        self.loggedinIcon = "//a[@class='iconLinks iconLinks__profile profile-js-handle isLoggedIn']"

        self.textElement="//span[@class='welcome-user-text__name']"

        self.signout= "//a[@class='logout-link']"

        self.invalidMsg= "//div[@class='form-global__field-message form-text-input__field-message']"


    def click_close_button(self):
        closeButtonClick = self.driver.find_element(By.XPATH,self.closeButton)
        closeButtonClick.click()

    def refresh_button(self):
        self.driver.refresh()

    def enter_mobileno_textbox(self,mob):
        mobileNumberTextBox = self.driver.find_element(By.XPATH, self.mobileNumberTextBoxElement)
        mobileNumberTextBox.send_keys(mob)

    def click_submit_button(self):
        submitButton = self.driver.find_element(By.XPATH, self.submitButtonElement)
        submitButton.click()

    def click_submit1_button(self):
        submitButton1=self.driver.find_element(By.XPATH,self.submitButtonElement1)
        submitButton1.click()

    def signedIn(self):
        loging=self.driver.find_element(By.XPATH,self.loggedinIcon)
        loging.click()

    def get_text(self):
        textValue = self.driver.find_element(By.XPATH, self.textElement)
        print(textValue.text)

    def click_sign_out(self):
        signOutLink = self.driver.find_element(By.XPATH,self.signout)
        signOutLink.click()

    def error_message(self):
        invalid = self.driver.find_element(By.XPATH, self.invalidMsg)
        print(invalid.text)


    # step defintion for excel sheet
    def mobiletextboxFirst_excel(self):
        ExcelUtils.get_row_count(self.dataFilePath,"Sheet1")
        mnum= ExcelUtils.read_data(self.dataFilePath, "Sheet1",2,1)
        mobileNumberTextBox = self.driver.find_element(By.XPATH, self.mobileNumberTextBoxElement)
        mobileNumberTextBox.send_keys(mnum)


    def mobiletextboxSecond_excel(self):
        ExcelUtils.get_row_count(self.dataFilePath,"Sheet1")
        mnum= ExcelUtils.read_data(self.dataFilePath, "Sheet1",3,1)
        mobileNumberTextBox = self.driver.find_element(By.XPATH, self.mobileNumberTextBoxElement)
        mobileNumberTextBox.send_keys(mnum)






