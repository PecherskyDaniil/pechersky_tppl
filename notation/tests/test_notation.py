import pytest
import numpy
from notation import separate,is_prefix,in_infix
@pytest.fixture
def estring():
    return "+ - 13 4 55"
class TestNotation:

    def test_separate(self,estring):
        ops,digs=separate(estring)
        assert (ops==["+","-"]).all()
        assert (digs==[13,4,55]).all()

        with pytest.raises(SyntaxError):
            separate("+ 3")
        with pytest.raises(SyntaxError):
            separate("+ 3 3 3")
        with pytest.raises(SyntaxError):
            separate("abc")

    @pytest.mark.parametrize(
        "string,isp",
        [("+ - 13 4 55",True),
         ("+ 2 * 2 - 2 1",True),
         ("2 3 -",False),
         ("- 2 - 3 4 5",False)]
    )
    def test_is_prefix(self,string,isp):      
        assert is_prefix(string)==isp
    @pytest.mark.parametrize(
        "prestring,instring",
        [("+ - 13 4 55","13 + 4 - 55"),
         ("+ 2 * 2 - 2 1","2 + 2 * 2 - 1"),
         ("/ + 3 10 * + 2 3 - 3 5","3 / 10 + 2 * 3 + 3 - 5")]
    )
    def test_in_infix(self,prestring,instring):
        assert in_infix(prestring)==instring
        
    def test_in_infix_error_many_opeartors(self):
        with pytest.raises(SyntaxError):
            in_infix("/ - 2 3")
    def test_in_infix_error_prefix(self):
        with pytest.raises(SyntaxError):
            in_infix("2 3 - -")
