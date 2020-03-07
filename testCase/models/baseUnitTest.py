from testCase.models.browserDriver import driver
import unittest

#定义一个单元测试基础类
class BaseUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver=driver()
        #设置等待超时
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
    def tearDown(self):
        #关闭浏览器
        self.driver.quit()