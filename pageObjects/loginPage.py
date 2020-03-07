from pageObjects.models import basePage
from pageObjects import logoutPage
from selenium.webdriver.common.by import By
from utils import function
from time import sleep

class Login(basePage.Base):
    '''
    Description:妖火网的登录页面的PageObject
    '''
    
    #由于定位的数据由于易变，放在类变量易于管理
    url="blog/Login.html"
    userIdLocation=(By.CSS_SELECTOR, "#logname")
    userPwdLocation=(By.CSS_SELECTOR, "#password")
    loginBtn=(By.CSS_SELECTOR, ".btn")
    loginTipsLocation=(By.CSS_SELECTOR, "b")
    gotoMainPageLocation=(By.CSS_SELECTOR, ".bt1 > a:nth-child(1)")
    rememberLocation=(By.CSS_SELECTOR,"#remember")
    
    #统一登录入口的用户名和密码
    rows=function.readExcel("data/loginTestData.xlsx")
    username=rows[1][0]
    pwd=rows[1][1]
    
    #打开登录页面
    def openLoginPage(self):
        self.open(Login.url)
        
    #定义一个统一的登录入口
    def loginSystem(self):
        #如果cookies文件为空
        if len(open("data/cookies.json").read()<0):
            self.openLoginPage()
            self.inputUserId(Login.username)
            self.inputUserPwd(Login.pwd)
            self.clickRemember()
            self.clickLoginBtn()
            #去主页的一个按钮
            elements = self.findElements(*Login.gotoMainPageLocation)
            info=""
            if len(elements)>0:
                info=self.getTips()
                elements[0].click() 
            #保存登录成功的cookies的策略
            if info==Login.rows[1][2]:
                #将cookies信息保存到data/cookies.json
                cookies=self.driver.get_cookies()
                cookiesFile = open('data/cookies.json', 'w')
                cookiesFile.write(json.dumps(cookies))
                cookiesFile.close
            return info
        #如果cookies文件不为空
        else:
            #登录前清楚所有cookie
            driver.delete_all_cookies()
            driver.get(logurl)
            f1 = open('vcyber.json')
            cookie = f1.read()
            cookie = json.loads(cookie)
            for c in cookie:
                driver.add_cookie(c)
            # # 刷新页面
            driver.refresh()
    
    
    
    

            
        
        
    def logout(self):
        #调用logoutPage的统一登出入口
        logoutPage.Logout(self.driver).logoutSystem()
    
    #填写用户id
    def inputUserId(self,userId):
        self.findElement(*Login.userIdLocation).send_keys(userId)
        
    #填写用户密码
    def inputUserPwd(self,pwd):
        self.findElement(*Login.userPwdLocation).send_keys(pwd)
        
    #点击登录按钮
    def clickLoginBtn(self):
        self.findElement(*Login.loginBtn).click()
        
    def clickRemember(self):
        self.findElement(*Login.rememberLocation).click()
        
    #获取网页的错误提示信息
    def getTips(self):
        return self.findElement(*Login.loginTipsLocation).text
 