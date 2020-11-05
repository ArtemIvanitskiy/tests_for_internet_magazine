#локатор и селектор в данном контексте можно считать синонимами
from selenium.webdriver.common.by import By
from selenium import webdriver
import math

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
 
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_IMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")
    PRODUCT_IN_ALERT_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert.alert-success.fade.in:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_MINI_ALL_PRICE = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    ALERT_BASKET_PRICE = (By.CSS_SELECTOR, ".alert.alert-noicon.alert-info strong")
    SUCCESS_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert.alert-success.fade.in:nth-child(1)")
    
class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")