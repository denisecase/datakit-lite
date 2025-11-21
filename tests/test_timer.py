from datakit_lite import log_duration, timeit


def test_timeit_decorator_runs():
    @timeit
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5


def test_log_duration_runs(capsys):
    with log_duration("block"):
        x = 1 + 1
        assert x == 2

    # Any printed output is fine
    output = capsys.readouterr().out
    assert "block" in output
