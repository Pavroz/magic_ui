import allure


@allure.feature('Inventory')
@allure.story('Correct authorization')
def test_correct_login(login_page):
    login_page.open_page()
    with allure.step('Enter correct username and password'):
        login_page.login_form('standard_user', 'secret_sauce')

@allure.feature('Inventory')
@allure.story('Test name page')
def test_name_page(login_page, inventory_page):
    test_correct_login(login_page)
    inventory_page.check_name_page('Products')