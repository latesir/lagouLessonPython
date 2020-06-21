import pytest
import yaml


def func(x):
    return x + 1

@pytest.mark.parametrize(('a','b'),yaml.safe_load(open("./yamldemo.yaml")))
def test_answer(a,b):
    assert func(a) == b

@pytest.fixture()
def login():
    a='tom'
    print("fixTest")
    return a

if __name__ == "__main__":
    pytest.main(['test_scrips.py::TestDemo', '-v'])


class TestDemo:
    def test_a(self,login):
        print(f"a's out is {login}")

    def test_b(self):
        print("cpy")

    def test_c(self):
        print("c")
