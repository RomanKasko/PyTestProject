link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_backet_button(browser):
    browser.get(link)
    assert browser.find_elements_by_css_selector("button.btn"), "There no backet button"