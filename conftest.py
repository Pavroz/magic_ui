from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from time import sleep
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver

# Фикстуры для инициализации страниц
@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture()
def inventory_page(driver):
    return InventoryPage(driver)