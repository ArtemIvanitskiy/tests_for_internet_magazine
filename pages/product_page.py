from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        button_atb = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_atb.click()
    #метод проверки соответствия названия товара,
    #добавленного в корзину с тем, который действительно добавили
    def check_added_to_basket_product_name(self):
        name_of_the_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        text_name_of_the_product = name_of_the_product.text
        
        actually_added_product = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_ADDED_TO_BASKET)
        text_actually_added_product = actually_added_product.text
        
        assert text_name_of_the_product == text_actually_added_product, "The name of the product added to the basket and which was actually added are not equal"
    #метод проверки совпадения стоимости корзины с ценой товара
    def check_cost_basket_with_cost_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        text_product_price = product_price.text
        
        alert_basket_price = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_PRICE)
        text_alert_basket_price = alert_basket_price.text
        
        #дополнительная проверка равенства цены товара появившейся цене в мини-корзине
        text = self.browser.find_element(*ProductPageLocators.BASKET_MINI_ALL_PRICE).text
        #убираем из всего текста текст "Basket total:", получая текст после ":"
        piece_of_text = text.split(":")[-1].strip()
        #убираем текст "View basket" и добавляем £
        text_mini_basket_price = piece_of_text.split("£")[-2].strip() + " £"
        
        assert text_product_price == text_alert_basket_price == text_mini_basket_price, "The price of a product or basket is not equal"
    
    #отрицательная проверка
    def should_not_be_success_message_about_added_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_TO_BASKET), \
       "Success message is presented, but should not be"
       
    def should_disappeared_success_message_about_added_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADDED_TO_BASKET), \
       "Success message is presenting, but should disappeared"