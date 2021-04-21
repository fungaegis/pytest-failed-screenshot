import helium
import pytest


@pytest.fixture()
def init_helium():
    yield None
    helium.kill_browser()


def test_helium_demo(init_helium):
    helium.start_chrome("https://github.com/fungaegis/pytest-failed-screenshot")
    assert False
