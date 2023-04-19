import pytest
from selene import browser

@pytest.fixture()
def browser_open(scope='function'):
    browser.driver.set_window_size(1920, 1080)
    browser.config.base_url = 'https://demoqa.com'
    yield browser
    browser.quit()