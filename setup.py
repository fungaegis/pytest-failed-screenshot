from setuptools import setup

"""
author: fungaegis
github: https://github.com/fungaegis/pytest-failed-screenshot
"""

setup(
    name='pytest_failed_screenshot',
    url='https://github.com/fungaegis/pytest-failed-screenshot',
    version='0.1',
    author="fungaegis",
    author_email="fungaegis@gmail.com",
    description='Test case fails,take a screenshot,save it,attach it to the allure',
    long_description='After the test case fails, take a screenshot in time, '
                     'save the screenshot in the specified address and attach it to the allure;'
                     '\nUsage: cmd line or main function --switch={on:off} --address=image path, default is off',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.7',
    ],
    license='MIT License',
    py_modules=['pytest_failed_screenshot'],
    keywords=[
        'pytest', 'py.test', 'pytest_failed_screenshot', 'allure', 'screenshot'
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
