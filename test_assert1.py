import pytest

def f():
    return 3


def test_function():
    assert f() == 4, "value was odd, should be even"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
        assert 'maximum recursion' in excinfo.value


def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r'.*1234.*'):
        myfunc()