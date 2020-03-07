from pageObjects.models import basePage
from selenium.webdriver.common.by import By
from pageObjects import loginPage,logoutPage
from utils import function

class ModifyPwd(basePage.Base):
    '''
    Description:妖火网的页面的PageObject
    '''
    
    #用于定位的数据由于易变，放在类变量易于管理
    url="bbs/ModifyPW.aspx?siteid=1000"
    #这是修改前的身份验证所需的定位元素
    originalPwdLocation=(By.CSS_SELECTOR, ".txt")
    confirmBtnLocation=(By.CSS_SELECTOR, ".btn")
    
    #这是真正修改页面的定位元素
    originalPwdLocation1=(By.CSS_SELECTOR,"input.txt:nth-child(6)")
    newPwdLocation=(By.CSS_SELECTOR,"input.txt:nth-child(9)")
    confirmPwdLocation=(By.CSS_SELECTOR,"input.txt:nth-child(12)")
    modifyBtnLocation=(By.CSS_SELECTOR,"#submit")
    tipsLocation=(By.CSS_SELECTOR,".tip > b:nth-child(1)")
    
    #密码（不给PageObject传递参数时的默认参数）
    rows=function.readExcel("data/loginTestData.xlsx")
    pwd=rows[1][1]
    
    
    #登录妖火网
    def login(self):
        #调用loginPage的统一登录入口
        return loginPage.Login(self.driver).loginSystem()
        
    def logout(self):
        #调用logoutPage的统一登出入口
        logoutPage.Logout(self.driver).logoutSystem()
        
    #打开修改密码界面
    def openModifyPage(self):
        self.open(ModifyPwd.url)
        #修改信息之前网站有个密码验证，所以先验证下
        elements=self.findElements(*ModifyPwd.originalPwdLocation)
        if len(elements)>0:
            elements[0].send_keys(ModifyPwd.pwd)
            self.findElement(*ModifyPwd.confirmBtnLocation).click()
        
    #填写原密码
    def inputOriginalPwd(self,pwd):
        if pwd!=None:
            self.findElement(*ModifyPwd.originalPwdLocation1).send_keys(pwd)
      
    #填写新密码
    def inputNewPwd(self,pwd):
        if pwd!=None:
            self.findElement(*ModifyPwd.newPwdLocation).send_keys(pwd)
    
    #填写确认密码
    def inputConfirmPwd(self,pwd):
        if pwd!=None:
            self.findElement(*ModifyPwd.confirmPwdLocation).send_keys(pwd)
        
    #点击修改按钮
    def clickModifyBtn(self):
        self.findElement(*ModifyPwd.modifyBtnLocation).click()
        
    #获取提示信息
    def getTips(self):
        return self.findElement(*ModifyPwd.tipsLocation).text