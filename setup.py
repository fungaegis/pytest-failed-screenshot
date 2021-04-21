from setuptools import setup

"""
author: fungaegis
github: https://github.com/fungaegis/pytest-failed-screenshot
"""

setup(
    name='pytest_failed_screenshot',
    url='https://github.com/fungaegis/pytest-failed-screenshot',
    version='1.0.2',
    author="fungaegis",
    author_email="fungaegis@gmail.com",
    description='Test case fails, take a screenshot, save it, attach it to the allure',
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
        'allure-python-commons',
        'helium'
    ],
    entry_points={
        'pytest11': [
            'failed_screenshot = pytest_failed_screenshot',
        ]
    }
)
