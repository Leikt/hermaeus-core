from src.hermaeus import hello_world


def test_hello_world():
    res = hello_world('Hermaeus')
    assert res == 'Hello, Hermaeus!'