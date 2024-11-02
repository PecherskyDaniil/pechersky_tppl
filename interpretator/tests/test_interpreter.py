import pytest
from interpreter import Interpreter

@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()
class TestInterpreter:

    def test_add(self,interpreter):
        assert interpreter.eval("2+2") == 4
        assert interpreter.eval("2+3") == 5
    def test_sub(self,interpreter):
        assert interpreter.eval("2-2") == 0
        assert interpreter.eval("2-3") == -1
