from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):#В классе MainPage не осталось никаких методов, поэтому добавил заглушку:
     def __init__(self, *args, **kwargs) #__init__ вызывается при создании объекта
         super(MainPage, self).__init__(*args, **kwargs) #Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage


""" Перенесено в base_page.py:

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #Возможный второй способ перехода между страницами:
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
        
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
"""
            
