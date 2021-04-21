pytest-failed-screenshot: pytest plugin
=======================================

For UI automation test cases using selenium and appium, screenshots are
saved when they fail, and are attached to the report when allure is used

Support helium, the webdriver process cannot be killed within a use case

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


    # helium demo
    @pytest.fixture()
    def init_helium():
        yield None
        kill_browser()


    @pytest.mark.usefixtures("init_helium")
    def test_helium_demo():
        start_chrome("https://github.com/fungaegis/pytest-failed-screenshot")
        # The webdriver process cannot be killed within a use case
        assert False


command: ``pytest --screenshot=on --screenshot_path=on``

tip: Support the use of pytest-xdist together

log
===
v1.0.1

Support helium for screenshots , solve the problem https://github.com/fungaegis/pytest-failed-screenshot/issues/1

v1.0.2

Update the readme and add demo

