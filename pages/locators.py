#локатор и селектор в данном контексте можно считать синонимами
from selenium.webdriver.common.by import By
from selenium import webdriver
import math

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")
    ALERT_SUCCESS_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert.alert-success.fade.in:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_MINI_ALL_PRICE = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    ALERT_BASKET_PRICE = (By.CSS_SELECTOR, ".alert.alert-noicon.alert-info strong")