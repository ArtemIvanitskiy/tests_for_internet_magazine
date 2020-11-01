from .pages.product_page import ProductPage
import pytest
from .pages.locators import ProductPageLocators
import time


@pytest.mark.parametrize('promo_number', ["1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]) #если списком list(range(1, 9), то не получается пометить xfail для упавшего теста, так что пришлось список вручную печатать по-простому
def test_guest_can_add_product_to_basket(browser, promo_number):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_added_to_basket_product_name()
    page.check_cost_basket_with_cost_product()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/metasploit_193/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message_about_added_to_basket() #8.85s failed +
   
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/metasploit_193/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_about_added_to_basket() #passed
    
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/metasploit_193/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(1)
    page.should_disappeared_success_message_about_added_to_basket() #13.36s failed +
