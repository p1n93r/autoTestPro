from pageObjects.models import basePage
from selenium.webdriver.common.by import By
from pageObjects import loginPage

class Logout(basePage.Base):
    '''
    Description:妖火网的页面的PageObject
    '''
    
    #用于定位的数据由于易变，放在类变量易于管理
    url="waplogout.aspx?siteid=1000"
    logoutBtnLocation=(By.CSS_SELECTOR, ".bt1 > a:nth-child(1)")
    
    #统一的登出入口
    def logoutSystem(self):
        self.openLogoutPage()
        self.clickLogout()
    
    #登录妖火网
    def login(self):
        #调用loginPage的统一登录入口
        return loginPage.Login(self.driver).loginSystem()
        
    #打开登出界面
    def openLogoutPage(self):
        self.open(Logout.url)
       
    #点击登出按钮
    def clickLogout(self):
        self.findElement(*Logout.logoutBtnLocation).click()
        