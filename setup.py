from setuptools import find_packages, setup

"""
author: fungaegis
github: https://github.com/fungaegis/pytest-failed-screenshot
"""
setup(
    name='pytest_failed_screenshot',
    url='https://github.com/fungaegis/pytest-failed-screenshot',
    version='1.1.0',
    author="fungaegis",
    author_email="fungaegis@gmail.com",
    description='Test case fails, take a screenshot, save it, attach it to the allure',
    python_requires='>=3',
    classifiers=[
        'Framework :: Pytest',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X'
    ],
    packages = find_packages(exclude=['tests', 'tests.*']),
    keywords=['pytest', 'allure', 'screenshot', 'selenium', 'appium'],
    install_requires=[
        'pytest',
        'selenium',
        'allure-pytest',
        'allure-python-commons',
        'helium'
    ],
    package_data={
        'backend.screenshot': ['webdrivers/**/*']
    },
    test_suite='tests'
)
