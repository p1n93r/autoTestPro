from selenium import webdriver
from utils.function import printScreen

#定义浏览器驱动
def driver():
    driver=webdriver.Firefox()
    return driver