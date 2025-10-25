from pages.base_page import BasePage
from pages.locators import inventory_locators as loc
import allure

class InventoryPage(BasePage):

    page_url = 'inventory.html'


    def check_name_page(self, text_title):
        name_page = self.find(loc.name_page_loc)
        with allure.step('Check name Page'):
            assert name_page.text == text_title