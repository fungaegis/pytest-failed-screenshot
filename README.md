pytest-custom-scheduling: pytest plugin
==============

Rewrite pytest-xdist pytest_xdist_make_scheduler function, Modify load scheduling.

Support custom grouping.

install
=====

`pip install pytest-custom-scheduling`

Usage
=====

command line:`pytest --switch={on:off} -n=auto`

tip: pytest-xdist must be turned on

- switch: Used to open plugin, default "off"

Use `${...}` as a marker custom grouping.

Demo
=====

```python
import pytest


@pytest.mark.parametrize("group", 
                         ["group_1", "group_2", "group_3", "group_4", "group_5", "group_6", 
                          "group_7", "group_8", "group_9", "group_10", "group_11", "group_12"], 
                         ids=["group_1${group_1}", "group_2${group_2}", "group_3${group_3}", 
                              "group_4${group_4}", "group_5${group_5}", "group_6${group_6}", 
                              "group_7${group_7}", "group_8${group_8}", "group_9${group_9}", 
                              "group_10${group_10}", "group_11${group_11}", "group_12${group_12}"])

@pytest.mark.parametrize("group", ["group_4", "group_5", "group_6"], 
                         ids=["group_4${group_5}", "group_5${group_5}", "group_6${group_5}"])
def test_05(group):
    a = "hello"
    b = "world"
    assert a == b
```

cmd line: `pytest --switch=on -n=auto`
