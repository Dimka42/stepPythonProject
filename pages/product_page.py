from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_correct_name(self, link):
        expected_price = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        real_price = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CHECK)
        assert expected_price.text == real_price.text, f"Expected {expected_price.text}, real result {real_price.text} in {link}"

    def should_be_correct_price(self):
        expected_name = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        real_name = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CHECK)
        assert expected_name.text == real_name.text, f"Expected Плохой текст, real result {real_name.text}"