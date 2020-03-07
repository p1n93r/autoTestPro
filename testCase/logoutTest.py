from utils import function
from testCase.models import baseUnitTest
from pageObjects import logoutPage


class LogoutTest(baseUnitTest.BaseUnitTest):
    '''妖火网登登出测试'''   
    
    successInfo=function.readExcel("data/loginTestData.xlsx")[1][2]
    
    def testLogout(self):
        '''成功登录后的登出'''
        logoutPageObject=logoutPage.Logout(self.driver)
        info=logoutPageObject.login()
        self.assertEqual(info,LogoutTest.successInfo)
        logoutPageObject.openLogoutPage()
        logoutPageObject.clickLogout()
        #截图
        function.printScreen(self.driver,"登出成功")
        
        
        