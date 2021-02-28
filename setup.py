from setuptools import setup

"""
author: fungaegis
github: https://github.com/fungaegis/pytest-failed-screenshot
"""

setup(
    name='pytest_failed_screenshot',
    url='https://github.com/fungaegis/pytest-failed-screenshot',
    version='1.0.0',
    author="fungaegis",
    author_email="fungaegis@gmail.com",
    description='Test case fails,take a screenshot,save it,attach it to the allure',
    long_description=r'''After the test case fails, take a screenshot in time,
                     save the screenshot in the specified address and attach it to the allure;
                     Usage: cmd line or main function 
                     "--screenshot={on:off}": Used to open plugin, default "off";
                     "--screenshot_path=file path",
                        - off: The default is 'off'. The screenshot will not be saved and will only be attached to the allure report.
                        - on: The screenshots will be saved to the "./screenshot/%Y-%m-%d/" directory in the root path of the project. 
                        If the directory has historical screenshots, the historical screenshots will be archived, moved to the "./screenshot/history/%Y-%m-%d/{times}" directory, 
                        and attached to the allure report
                        - Absolute path: The screenshot will be saved in that path and attached to the report.
                     ''',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.7',
    ],
    license='MIT License',
    py_modules=['pytest_failed_screenshot'],
    keywords=[
        'pytest', 'py.test', 'pytest_failed_screenshot', 'allure', 'screenshot', 'selenium', 'appium'
    ],

    install_requires=[
        'pytest',
        'selenium',
        'allure-pytest',
        'allure-python-commons'
    ],
    entry_points={
        'pytest11': [
            'failed_screenshot = pytest_failed_screenshot',
        ]
    }
)
