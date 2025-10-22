

def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('qwewqe', 'wqewqe')
    login_page.check_error_alert('Epic sadface: Username and password do not match any user in this service')

def test_correct_username_with_incorrect_password(login_page):
    login_page.open_page()
    login_page.fill_login_form('standard_user', 'wqewqe')
    login_page.check_error_alert('Epic sadface: Username and password do not match any user in this service')

def test_correct_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('standard_user', 'secret_sauce')
