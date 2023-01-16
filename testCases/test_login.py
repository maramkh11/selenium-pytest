from utilities.customLogger import LogGenerator
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGenerator.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.logger.info("********** Home Page Title test is passed **********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Home Page Title test is failed **********")
            assert False

    # def test_login(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.setUserName(self.username)
    #     self.loginPage.setPassword(self.password)
    #     self.loginPage.clickLogin()
    #     actual_title = self.driver.title()
    #     if actual_title == "Dashboard / nopCommerce administration":
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
    #         self.driver.close()
    #         assert False
