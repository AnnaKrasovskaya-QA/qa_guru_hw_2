import pytest
from selene import browser, be, have
from selenium import webdriver

driver_options = webdriver.ChromeOptions()
driver_options.page_load_strategy = 'eager'
browser.config.driver_options = driver_options

@pytest.fixture()
def open_window():
    driver = webdriver.Chrome()
    driver.set_window_size(1200, 800)


@pytest.fixture()
def before_search(open_window):
    browser.open('https://google.com')
    browser.config.timeout = 20
    print("Called before search test")


    yield
    browser.quit()
    print("Закрываем браузер!")


def test_search(before_search):
    browser.element('[name="q"]').should(be.blank).type('вокруг шум пусть так не кипишуй').press_enter()
    browser.element('[id="main"]').should(have.text('Вокруг шум'))
    print("Результат найден")


def test_no_search(before_search):
    browser.element('[name="q"]').should(be.blank).type('cuQ6b:npT2md;x123456789').press_enter()
    browser.element('[id="main"]').should(have.text('ничего не найдено'))
    print("Результат не найден")
