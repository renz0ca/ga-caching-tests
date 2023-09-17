from test_project_2 import is_odd


def test_is_odd():
    assert is_odd(1)
    assert not is_odd(2)
    assert is_odd(141)
    assert not is_odd(3432)
