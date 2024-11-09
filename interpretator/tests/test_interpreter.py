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
    def test_spaces(self,interpreter):
        assert interpreter.eval("  2    - 2       ") == 0
    def test_int(self,interpreter):
        assert interpreter.eval("2222122-33") == 2222089
    def test_float(self,interpreter):
        assert interpreter.eval("22.2+33.3") == 55.5
    def test_term(self,interpreter):
        assert interpreter.eval("2+2-2") == 2
    def test_multiply(self,interpreter):
        assert interpreter.eval("2+2*2") == 6
    def test_parrens(self,interpreter):
        assert interpreter.eval("(2+2)*2") == 8
        assert interpreter.eval("3*(2-2)-2") == -2
        assert interpreter.eval("((((2))))") == 2
        assert interpreter.eval("2*(2+4/(2+2))") == 6
