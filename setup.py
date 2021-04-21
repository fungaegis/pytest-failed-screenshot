from setuptools import setup

setup(
    name='pytest_failed_screenshot',
    url='https://github.com/fungaegis/pytest-failed-screenshot',
    version='1.1.0',
    author="fungaegis",
    author_email="fungaegis@gmail.com",
    description='Test case fails, take a screenshot, save it, attach it to the allure',
    python_requires='>=3',
    license='MIT License',
    classifiers=[
        'Framework :: Pytest',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X'
    ],
    py_modules=['screenshot'],
    keywords=[
        'pytest', 'allure', 'screenshot', 'selenium', 'appium', 'helium'
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
            'failed_screenshot = screenshot',
        ]
    }
)
