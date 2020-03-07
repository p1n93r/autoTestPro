from utils import function
from testCase.models import baseUnitTest
from pageObjects import modifyPwdPage


class ModifyPwdTest(baseUnitTest.BaseUnitTest):
    '''妖火网修改密码测试'''   
    
    #表格的内容可能会在测试过程中变化，所以每执行一个test，就重新加载一次表格
    def initData(self):
        self.successInfo=function.readExcel("data/loginTestData.xlsx")[1][2]
        self.rows=function.readExcel("data/modifyPwdTestData.xlsx")
    
    def commonBase(self,modifyPagePicName,whichRow):
        self.initData()
        ModifyPageObject=modifyPwdPage.ModifyPwd(self.driver)
        info=ModifyPageObject.login()
        self.assertEqual(info,self.successInfo)
        ModifyPageObject.openModifyPage()
        ModifyPageObject.inputOriginalPwd(self.rows[whichRow][0])
        ModifyPageObject.inputNewPwd(self.rows[whichRow][1])
        ModifyPageObject.inputConfirmPwd(self.rows[whichRow][2])
        ModifyPageObject.clickModifyBtn()
        function.printScreen(self.driver,"点击修改密码按钮_"+modifyPagePicName)
        #断言是否修改成功,成功后需要修改相应excel里的数据，防止不能正常登录
        self.assertEqual(ModifyPageObject.getTips(),self.rows[whichRow][3])
        #登出
        ModifyPageObject.logout()
    def testModifyPwd(self):
        '''正常修改密码'''
        self.commonBase("正常修改密码",1)
        #修改相应的excel
        newPwd=self.rows[1][1]
        function.writeExcel("data/loginTestData.xlsx",*(1,1,newPwd))
        for i in range(1,6):
            function.writeExcel("data/modifyPwdTestData.xlsx",*(i,0,newPwd))
         
    def testModifyPwd1(self):
        '''仅新密码为空'''
        self.commonBase("仅新密码为空",2)
        
    def testModifyPwd2(self):
        '''仅确认密码为空'''
        self.commonBase("仅确认密码为空",3)
        
    def testModifyPwd3(self):
        '''仅新密码和确认密码为空'''
        self.commonBase("仅新密码和确认密码为空",4)
        
    def testModifyPwd4(self):
        '''仅新密码和确认密码不一致'''
        self.commonBase("仅新密码和确认密码不一致",5)
        
    def testModifyPwd5(self):
        '''仅原密码错误'''
        self.commonBase("仅原密码错误",6)
        
    def testModifyPwd6(self):
        '''原密码错误的同时新旧密码不一致'''
        self.commonBase("原密码错误的同时新旧密码不一致",7)
        