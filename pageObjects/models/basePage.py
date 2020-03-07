#一个页面基础类，用于所有的Page Object继承
class Base():
    '''
    Description:封装了selenium的一些方法,主要是元素查找相关
    '''
    
    #被测项目的域名(basePath)
    rootUrl="https://yaohuo.me/"
    
    def __init__(self,driver,baseUrl=rootUrl):
        self.driver=driver
        self.baseUrl=baseUrl
        
    def open(self,url):
        self.driver.get(self.baseUrl+url)
        #断言是否打开了本页面
        assert self.driver.current_url==(self.baseUrl+url),'未找到页面：%s' %url
        
    def findElement(self,*location):
        return self.driver.find_element(*location)
        
    def findElements(self,*location):
        return self.driver.find_elements(*location)
        
    def doScript(self,src):
        return self.driver.execute_script(src)