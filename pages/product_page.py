from .base_page import BasePage
from .locators import ProductPageLocators
import time, re

class ProductPage(BasePage):
    def add_to_basket(self):
        button_atb = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_atb.click()
        
    #метод проверки соответствия названия товара,
    #добавленного в корзину с тем, который действительно добавили
    def check_added_to_basket_product_name(self):
        text_name_of_the_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text        
        text_actually_added_product = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_ALERT_ADDED_TO_BASKET).text
        assert text_name_of_the_product == text_actually_added_product, "The name of the product added to the basket and which was actually added are not equal"

    #метод проверки совпадения стоимости одного товара в корзине с ценой товара
    def check_cost_basket_with_cost_product(self): 
        text_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cost_product = re.findall(r'\d+\.\d+', text_product)
       
        text_alert = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_PRICE).text
        cost_alert_basket = re.findall(r'\d+\.\d+', text_alert)
        
        text_mini = self.browser.find_element(*ProductPageLocators.BASKET_MINI_ALL_PRICE).text
        cost_mini_basket = re.findall(r'\d+\.\d+', text_mini)
        assert cost_product == cost_alert_basket == cost_mini_basket, "The price of a product or basket is not equal"
    
    #отрицательные проверки
    def should_not_be_success_message_about_added_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_TO_BASKET), \
       "Success message is presented, but should not be"
       
    def should_disappeared_success_message_about_added_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADDED_TO_BASKET), \
       "Success message is presenting, but should disappeared"