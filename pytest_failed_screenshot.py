import os
import re
import shutil
import time
import uuid

import allure
import pytest
from helium import get_driver
from selenium.webdriver.remote.webdriver import WebDriver


def pytest_addoption(parser):
    group = parser.getgroup("failed-screenshot", "Screenshot of test case failure")
    group.addoption("--screenshot",
                    action="store",
                    default="off",
                    choices=["on", "off"],
                    help="open failed screenshot")

    group.addoption("--screenshot_path",
                    action="store",
                    default="off",
                    help="Default don't save screenshot, If the parameter is on, "
                         "it will be save in the 'screenshot' directory of program root directory "
                         "and the history file will be archived. "
                         "If the parameter is not on or off, it will be save in the specified path")


def pytest_configure(config):
    path = config.getvalue("screenshot_path")
    switch = config.getvalue("screenshot")
    if switch == "on" and path == "on":
        root_path = config.rootdir.strpath
        screenshot = os.path.join(root_path, "screenshot")
        archive_file(screenshot)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    instance = False
    if item.config.getvalue("screenshot") == "on" and result.when == "call" and result.failed:
        for value in item.funcargs.values():
            if isinstance(value, WebDriver):
                instance = True
                break
        else:
            driver = get_driver()
            if driver:
                instance = True
                value = driver

    if instance:
        path = item.config.getvalue("screenshot_path")
        if path not in ("off", "on"):  # if command passes in the path, it is saved
            capture_screenshot(path, item.name, value)
        elif path == "on":  # save project root path
            filename = item.config.rootdir.strpath  # Get project root path
            filename = os.path.join(filename, "screenshot", time.strftime("%Y-%m-%d"))
            capture_screenshot(filename, item.name, value)
        else:  # Don't save, only attach allure
            data = value.get_screenshot_as_png()
            allure.attach(body=data, name=item.name, attachment_type=allure.attachment_type.PNG)


def capture_screenshot(filedir, page_name, driver):
    try:
        if not os.path.exists(filedir):
            os.makedirs(filedir)
        img_path = os.path.join(filedir, page_name + "_" + str(uuid.uuid4()).replace("-", "")[:8] + ".png")
        res = driver.save_screenshot(img_path)
        if res:
            with open(img_path, "rb") as image:
                data = image.read()
                allure.attach(body=data, name=page_name, attachment_type=allure.attachment_type.PNG)
        else:
            print("screenshot failed!")
            img_path = None
        return img_path
    except (OSError, NameError) as e:
        print(e)


def archive_file(filepath, pattern=r"[\w\]\[]*\.png") -> None:
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    else:
        dirs_list = os.listdir(filepath)
        for dir_name in dirs_list:
            path = os.path.join(filepath, dir_name)
            if not os.path.isdir(path):
                continue
            dirs = ';'.join(os.listdir(path))
            mv_dirs = re.findall(pattern, dirs)
            if mv_dirs:
                history = os.path.join(filepath, "history", dir_name)
                if not os.path.exists(history):
                    os.makedirs(history)
                times = 1
                while True:
                    existing = os.path.join(history, str(times))
                    if not os.path.exists(existing):
                        os.makedirs(existing)
                        break
                    times += 1
                for i in mv_dirs:
                    shutil.move(os.path.join(path, i), existing)
                else:
                    try:
                        os.removedirs(path)
                    except OSError as e:
                        print(f"Delete directory path:{path} error! Track:{e}")
