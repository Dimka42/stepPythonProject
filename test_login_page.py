from .pages.login_page import LoginPage


def test_form_and_url_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page2 = LoginPage(browser, link)
    page2.open()
    page2.should_be_login_page()
