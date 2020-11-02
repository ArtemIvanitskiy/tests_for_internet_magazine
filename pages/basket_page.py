from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Product in basket, but should not be"
        
    def should_be_element_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Missing an item indicating that the cart is empty"