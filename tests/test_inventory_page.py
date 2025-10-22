
def test_correct_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('standard_user', 'secret_sauce')

def test_name_page(login_page, inventory_page):
    test_correct_login(login_page)
    inventory_page.check_name_page('Products')