from utils import function
from testCase.models import baseUnitTest
from pageObjects import loginPage


class LoginTest(baseUnitTest.BaseUnitTest):
    '''妖火网登录测试'''
    
    #获取当前页面的所有测试数据
    rows=function.readExcel("data/loginTestData.xlsx")
    
    def commomBase(self,whichRow,picName):
        #获取测试数据
        row=LoginTest.rows[whichRow]
        
        loginPageObj=loginPage.Login(self.driver)
        loginPageObj.openLoginPage()
        loginPageObj.inputUserId(row[0])
        loginPageObj.inputUserPwd(row[1])
        loginPageObj.clickRemember()
        loginPageObj.clickLoginBtn()
        self.assertEqual(loginPageObj.getTips(),row[2])
        #截图
        function.printScreen(self.driver,picName)
        #只有成功登录了系统才能登出
        if whichRow==1:
            loginPageObj.logout()
       
    def testLogin(self):
        '''正确的用户名和密码'''
        self.commomBase(1,"登录成功")
        
    def testLoginWithWrongPwd(self):
        '''正确的用户名和错误的密码'''
        self.commomBase(2,"密码错误")
        
    def testLoginWithWrongId(self):
        '''不存在的用户名'''
        self.commomBase(3,"用户名不存在")
        