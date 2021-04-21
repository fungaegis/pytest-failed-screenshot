import pytest
from selenium import webdriver

from backend import use_included_web_driver


@pytest.fixture()
def init_driver():
    driver = webdriver.Chrome(
        executable_path=use_included_web_driver('chromedriver'))
    yield driver
    driver.close()
    driver.quit()


def test_login_success(init_driver):
    init_driver.get("https://github.com/fungaegis/pytest-failed-screenshot")
    assert False
