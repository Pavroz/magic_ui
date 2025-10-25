import allure

@allure.feature('Authorization')
@allure.story('Incorrect authorization')
def test_incorrect_login(login_page):
    login_page.open_page()
    with allure.step('Enter incorrect username and password'):
        login_page.login_form('qwewqe', 'wqewqe')
    login_page.check_error_alert('Eqpic sadface: Username and password do not match any user in this service')

@allure.feature('Authorization')
@allure.story('Incorrect authorization')
def test_correct_username_with_incorrect_password(login_page):
    login_page.open_page()
    with allure.step('Incorrect password'):
        login_page.login_form('standard_user', 'wqewqe')
    login_page.check_error_alert('Epic sadface: Username and password do not match any user in this service')

@allure.feature('Authorization')
@allure.story('Correct authorization')
def test_correct_login(login_page):
    login_page.open_page()
    with allure.step('Enter correct username and password'):
        login_page.login_form('standard_user', 'secret_sauce')
