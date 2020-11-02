from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():    
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес    
        page = BasePage(browser, link)
        page.open()   
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
 
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()    


    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_product()
    page.should_be_element_cart_is_empty()
  
