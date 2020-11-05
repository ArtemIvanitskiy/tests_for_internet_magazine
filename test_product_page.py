from .pages.product_page import ProductPage
import pytest
from .pages.locators import ProductPageLocators
import time
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


#список в parametrize создан вручную, а не программно: list(range(1, 9), чтобы получилось пометить xfail для упавшего теста
@pytest.mark.need_review
@pytest.mark.parametrize('promo_number', ["1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_number):    
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_added_to_basket_product_name()
    page.check_cost_basket_with_cost_product()

    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()    

    
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/metasploit_193/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message_about_added_to_basket()
   
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/metasploit_193/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_about_added_to_basket()
    
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/metasploit_193/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappeared_success_message_about_added_to_basket()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/metasploit_193/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_product()
    page.should_be_element_cart_is_empty()
    

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_user()
        page.should_be_authorized_user()               
        
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/metasploit_193/"
        page = ProductPage(browser, link)
        page.open()       
        page.should_not_be_success_message_about_added_to_basket()       
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):        
        link = "http://selenium1py.pythonanywhere.com/catalogue/metasploit_193/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()        
        page.check_added_to_basket_product_name()
        page.check_cost_basket_with_cost_product()
       