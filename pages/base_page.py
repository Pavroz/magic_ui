from selenium.webdriver.remote.webdriver import WebDriver
import allure


class BasePage:

    base_url = 'https://www.saucedemo.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        with allure.step('Open the Page'):
            if self.page_url:
                self.driver.get(f'{self.base_url}{self.page_url}')
            else:
                self.driver.get(f'{self.base_url}')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self,locator: tuple):
        return self.driver.find_elements(*locator)