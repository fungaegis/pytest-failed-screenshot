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
    result.stdout.fnmatch_lines(["*--screenshot*"])
    result.stdout.fnmatch_lines(["*--screenshot_path*"])
