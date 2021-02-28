pytest-failed-screenshot: pytest plugin
=======================================

For UI automation test cases using selenium and appium, screenshots are
saved when they fail, and are attached to the report when allure is used

install
=======

``pip install pytest-failed-screenshot``

Usage
=====

command line:``pytest --screenshot={on:off} --screenshot_path={on:off:absolute path}``


* - options:
  - screenshot: Used to open plugin, default "off"
  - screenshot_path:
     - off: The default is 'off'.The screenshot will not be saved and will only be attached to the allure report.
     - on: The screenshots will be saved to the "./screenshot/%Y-%m-%d/" directory in the root path of the project.
       If the directory has historical screenshots, the historical screenshots will be archived, moved to the
       "./screenshot/history/%Y-%m-%d/{times}" directory, and attached to the allure report
     - Absolute path: The screenshot will be saved in that path and attached to the report.


Demo
====

The driver instances of selenium and appium must be transferred by a
fixture.


.. code-block:: python

    import pytest
    from selenium import webdriver


    @pytest.fixture()
    def init_driver():
        driver = webdriver.Chrome()
        yield driver
        driver.close()
        driver.quit()


    def test_login_success(init_driver):
        init_driver.get("https://github.com/fungaegis/pytest-failed-screenshot")
        assert False


command: ``pytest --screenshot=on --screenshot_path=on``

tip: Support the use of pytest-xdist together


