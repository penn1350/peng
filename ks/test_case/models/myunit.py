from selenium import webdriver
from .driver import browser
import unittest
import os

class MyTest(unittest.TestCase):
    """自定义测试框架类,前后装饰器"""
    def setUp(self) -> None:
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()
