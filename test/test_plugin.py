import pytest


def test_help(testdir):
    testdir.makepyfile(
        """
        def test_01():
            a = "pytest"
            b = "py"
            assert a == b
        """
    )
    result = testdir.runpytest("--help")
    result.stdout.fnmatch_lines(["*--switch*"])
    result.stdout.fnmatch_lines(["*Custom grouping for pytest-xdist*"])


def test_without(testdir):
    testdir.makepyfile(
        """
        def test_01():
            a = "hello world"
            b = "hello world"
            assert a == b

        def test_02():
            a = "hello"
            b = "world"
            assert a == b
        """
    )
    result = testdir.runpytest()
    result.assert_outcomes(passed=1, failed=1)


def test_off(testdir):
    testdir.makepyfile(
        """
        def test_01():
            a = "hello world"
            b = "hello world"
            assert a == b

        def test_02():
            a = "hello"
            b = "world"
            assert a == b
        """
    )
    result = testdir.runpytest("--switch=off")
    result.assert_outcomes(passed=1, failed=1)


def test_xdist_on_switch_off(testdir):
    testdir.makepyfile(
        """
        def test_01():
            a = 5
            b = 10
            assert a + b == 15
        def test_02():
            a = 10
            b = 5
            assert a + b != 15
        """
    )
    result = testdir.runpytest("-n=3", "--switch=off")
    result.assert_outcomes(passed=1, failed=1)


def test_xidst_on_switch_on_none_param(testdir):
    testdir.makepyfile(
        """
        import pytest
        @pytest.mark.parametrize("group", ["group_1", "group_2", "group_3"], 
                                 ids=["group_1", "group_2}", "group_3"])
        def test_01(group):
            a = "hello world"
            b = "hello world"
            assert a == b

        def test_02():
            a = "hello"
            b = "world"
            assert a == b
            
        def test_03():
            a = "hello"
            b = "world"
            assert a == b
  
        @pytest.mark.parametrize("group", ["group_1", "group_2", "group_3"], 
                                 ids=["group_1", "group_2}", "group_3"])          
        def test_04(group):
            a = "hello"
            b = "world"
            assert a != b
            
        def test_05():
            a = "hello"
            b = "world"
            assert a != b
        """
    )
    result = testdir.runpytest("--switch=on", "-n=5")
    result.assert_outcomes(passed=7, failed=2)


def test_n_on_switch_on_have_param(testdir):
    testdir.makepyfile(
        """
        import pytest
        @pytest.mark.parametrize("group", 
                                 ["group_1", "group_2", "group_3", "group_4", "group_5", "group_6", 
                                  "group_7", "group_8", "group_9", "group_10", "group_11", "group_12"], 
                                 ids=["group_1${group_1}", "group_2${group_2}", "group_3${group_3}", 
                                      "group_4${group_4}", "group_5${group_5}", "group_6${group_6}", 
                                      "group_7${group_7}", "group_8${group_8}", "group_9${group_9}", 
                                      "group_10${group_10}", "group_11${group_11}", "group_12${group_12}"])
        def test_01(group):
            a = "hello world"
            b = "hello world"
            assert a == b
            
        @pytest.mark.parametrize("group", ["group_1", "group_2", "group_3"], 
                                 ids=["group_1${group_1}", "group_2${group_2}", "group_3${group_3}"])
        def test_02(group):
            a = "hello"
            b = "world"
            assert a == b
            
        @pytest.mark.parametrize("group", ["group_4", "group_5", "group_6"], 
                                 ids=["group_4${group_4}", "group_5${group_5}", "group_5${group_5}"])
        def test_03(group):
            a = "hello"
            b = "world"
            assert a == b
            
        @pytest.mark.parametrize("group", ["group_4", "group_5", "group_6"], 
                                 ids=["group_4${group_4}", "group_4${group_4}", "group_4${group_4}"])
        def test_04(group):
            a = "hello"
            b = "world"
            assert a == b
            
        @pytest.mark.parametrize("group", 
                                 ["group_4", "group_5", "group_6"], 
                                 ids=["group_4${group_5}", "group_5${group_5}", "group_6${group_5}"])
        def test_05(group):
            a = "hello"
            b = "world"
            assert a == b
        """
    )
    result = testdir.runpytest("-n=auto", "--switch=on")
    result.assert_outcomes(passed=12, failed=12)


def test_on_group_have_param(testdir):
    testdir.makepyfile(
        """
        import pytest
        @pytest.mark.parametrize("name", ["group_1", "group_2", "group_3"])
        def test_01(name):
            a = "hello world"
            b = "hello world"
            assert a == b

        @pytest.mark.parametrize("name", ["group_1", "group_2", "group_3"])
        def test_02(name):
            a = "hello"
            b = "world"
            assert a == b

        @pytest.mark.parametrize("name", ["group_1", "group_2", "group_3"])
        def test_03(name):
            a = "hello"
            b = "world"
            assert a == b

        @pytest.mark.parametrize("name", ["group_1", "group_2", "group_3"])
        def test_04(name):
            a = "hello"
            b = "world"
            assert a == b

        @pytest.mark.parametrize("name", ["group_1", "group_2", "group_3"])
        def test_05(name):
            a = "hello"
            b = "world"
            assert a == b
        """
    )
    result = testdir.runpytest("--switch=on", "-n=4")
    result.assert_outcomes(passed=3, failed=12)


if __name__ == '__main__':
    # pytest.main(["--concurrent=on"])
    # pytest.main(["-svv"])
    # pytest.main(["-sv", "-n=3", "--switch=on", "test_plugin.py::test_without"])
    pytest.main()
    # pytest.main(["-sv", "test_plugin.py::test_n_on_switch_on_have_param"])
