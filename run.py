from utils import HTMLTestRunner
from utils import function
import unittest
import threading
from selenium import webdriver


if __name__=="__main__":
    
    suite=unittest.defaultTestLoader.discover("./testCase",pattern="loginTest.py")
    function.createHtmlReport("妖火网UI测试",suite)
    '''
    test=function.readExcel("data/modifyPwdTestData.xlsx")
    print(test)
    print(test[2][1]==None)
    '''
    
    
    
    
    