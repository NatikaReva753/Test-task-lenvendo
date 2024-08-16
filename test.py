from application import Application
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test(app):
    app.open_home_page()
    app.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[1]").click()
    app.find_element_by_xpath(
         u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[2]").click()
    app.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[3]").click()
    app.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[4]").click()
    app.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[5]").click()
    app.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[6]").click()
