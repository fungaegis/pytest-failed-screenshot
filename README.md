pytest-failed-screenshot: pytest plugin
==============

For UI automation test cases using selenium and appium, screenshots are saved when they fail, and are attached to the report when allure is used

用于使用了Selenium和Appium的UI自动化测试用例在失败时进行截图保存并且在开启allure的时候会将截图附加到报告上

Support helium, the webdriver process cannot be killed within a use case 

支持helium失败截图, 但必须保证webdriver实例在用例内不被关闭.

install
=====

`pip install pytest-failed-screenshot`

Usage
=====

command line:`pytest --screenshot={on:off} --screenshot_path={on:off:absolute path}`

options:
- screenshot: Used to open plugin, default "off"
- screenshot_path: 
    - off: The default is 'off'. The screenshot will not be saved and will only be attached to the allure report.
    - on: The screenshots will be saved to the "./screenshot/%Y-%m-%d/" directory in the root path of the project. 
      If the directory has historical screenshots, the historical screenshots will be archived, moved to the "./screenshot/history/%Y-%m-%d/{times}" directory, 
      and attached to the allure report
    - Absolute path: The screenshot will be saved in that path and attached to the report.

选项:
- screenshot: 用于开启该插件,默认为"off"关闭状态
- screenshot_path:
    - off: 默认为"off"关闭状态,截图不进行保存,只附加到allure报告上
    - on: 截图将保存到项目根路径的"./screenshot/%Y-%m-%d/"目录,
      若该目录已有历史截图则将历史截图进行归档, 移动至"./screenshot/history/%Y-%m-%d/次数/"目录中,
      并且附加到allure报告上
    - 绝对路径: 截图将保存在指定的路径上,并且附加到allure报告上
    
Demo
======
The driver instances of selenium and appium must be transferred by a fixture.

selenium和appium的驱动实例必须通过fixture函数的方式前置传入

```python
import pytest
from selenium import webdriver
from helium import start_chrome, kill_browser


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
```

command: `pytest --screenshot=on --screenshot_path=on`

tip:
- Support the use of pytest-xdist together

小贴士:
- 支持与pytest-xdist一起使用

![archive](./images/archive.png)

![allure](./images/attach.png)

## log
### v1.0.1
Support helium for screenshots , solve the problem https://github.com/fungaegis/pytest-failed-screenshot/issues/1

更新支持helium进行截图,解决https://github.com/fungaegis/pytest-failed-screenshot/issues/1的问题
### v1.0.2
Update the readme and add demo

更新readme文档,增加使用示例
