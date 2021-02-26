import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver


def pytest_addoption(parser):
    group = parser.getgroup("failed-screenshot", "Screenshot of test case failure")
    group.addoption("--switch",
                    action="store",
                    default="off",
                    choices=["on", "off"],
                    help="open failed screenshot")

    group.addoption("--address",
                    action="store",
                    default="off",
                    help="If the address is on, save the screenshot")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    if item.config.getvalue("switch") == "on":
        result = outcome.get_result()
        if result.when == "call" and result.failed:
            for value in item.funcargs.values():
                if "webdriver" in repr(value):
                    path = item.config.getvalue("address")
                    if path:  # if command passes in the address, it is saved
                        WebDriver(value).save_screenshot(path)
                        with open(path, "rb") as image:
                            allure.attach(body=image, name=item.name, attachment_type=allure.attachment_type.PNG)
                        break
                    else:  # Don't save, only attach allure
                        data = WebDriver(value).get_screenshot_as_png()
                        allure.attach(body=data, name=item.name, attachment_type=allure.attachment_type.PNG)
