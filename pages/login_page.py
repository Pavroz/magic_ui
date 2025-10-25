from pages.base_page import BasePage
from pages.locators import login_locators as loc
import allure

class LoginPage(BasePage):


    def login_form(self, username, password):
        with allure.step('Filling out the login form'):
            username_field = self.find(loc.username_field_loc)
            password_field = self.find(loc.password_field_loc)
            button = self.find(loc.button_loc)
            username_field.send_keys(username)
            password_field.send_keys(password)
            button.click()

    def check_error_alert(self, text_error):
        with allure.step('Check the error text'):
            error_alert = self.find(loc.error_alert_loc)
            assert error_alert.text == text_error