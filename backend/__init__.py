from os import X_OK, access
from os.path import dirname, join

from backend.os_ import make_executable
from backend.system_ import *


def use_included_web_driver(driver_name):
    if is_windows():
        driver_name += '.exe'
    driver_path = join(
        dirname(__file__), 'webdrivers', get_os_name(),
        driver_name
    )
    if not access(driver_path, X_OK):
        try:
            make_executable(driver_path)
        except Exception:
            raise RuntimeError(
                "The driver located at %s is not executable." % driver_path
            ) from None
    return driver_path
