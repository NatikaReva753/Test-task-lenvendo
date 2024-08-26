from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_button_activation(app):
    app.session.login()
    app.open_home_page()

    # Находим кнопку с номиналом 500
    button_xpath = u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[1]"
    button = app.find_element_by_xpath(button_xpath)
    button.click()
    assert "par-options__button--active" in button.get_attribute("class"), "Button did not activate"

    # Находим кнопку с номиналом 1000
    button_xpath = u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[2]"
    button = app.find_element_by_xpath(button_xpath)
    button.click()
    assert "par-options__button--active" in button.get_attribute("class"), "Button did not activate"

    # Находим кнопку с номиналом 2000
    button_xpath = u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[3]"
    button = app.find_element_by_xpath(button_xpath)
    button.click()
    assert "par-options__button--active" in button.get_attribute("class"), "Button did not activate"

    # Находим кнопку с номиналом 3000
    button_xpath = u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[4]"
    button = app.find_element_by_xpath(button_xpath)
    button.click()
    assert "par-options__button--active" in button.get_attribute("class"), "Button did not activate"

    # Находим кнопку с номиналом 5000
    button_xpath = u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[5]"
    button = app.find_element_by_xpath(button_xpath)
    button.click()
    assert "par-options__button--active" in button.get_attribute("class"), "Button did not activate"

    # Находим кнопку с номиналом 10000
    button_xpath = u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::button[6]"
    button = app.find_element_by_xpath(button_xpath)
    button.click()
    assert "par-options__button--active" in button.get_attribute("class"), "Button did not activate"