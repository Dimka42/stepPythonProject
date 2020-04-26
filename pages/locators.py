from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")


class LoginPageLocators():
    SIGN_IN_INPUT_MAIL = (By.XPATH, "//input[@id='id_login-username']")
    SIGN_IN_INPUT_PASSWORD = (By.XPATH, "//input[@id='id_login-password']")
    SIGN_IN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTRATION_FORM = (By.XPATH, "//form[@id='register_form']")
    REGISTRATION_INPUT_MAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REGISTRATION_INPUT_PASSWORD = (By.XPATH, "//input[@id='id_registration-password1']")
    REGISTRATION_INPUT_REPEAT_PASSWORD = (By.XPATH, "//input[@id='id_registration-password2']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_NAME_CHECK = (By.XPATH, "//*[@id='messages']/div[1]//strong")
    PRODUCT_PRICE_CHECK = (By.XPATH, "//*[@id='messages']/div[3]//strong")
