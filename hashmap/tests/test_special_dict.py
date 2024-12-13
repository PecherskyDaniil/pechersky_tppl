import pytest
from specialdict import SpecialDict
from specialdict import Token,TokenType
@pytest.fixture(scope="function")
def specialdict():
    a=SpecialDict()
    a["value1"]=-1
    a["value2"]=-2
    a["(1,2)"]=12
    a["(2,3)"]=23
    a["(3,3)"]=33
    a["(4,1)"]=41
    a["(1,1)"]=11
    a["(5,2)"]=52
    a["(1)"]=1
    a["-1"]=-1
    a["2"]=2
    a["3"]=3
    a["(1,2,3)"]=123
    a["(3,3,3)"]=333
    a["(3,2,3)"]=323
    a["(3,2,1)"]=321
    a["4,4,4"]=444
    a["(10,4,7)"]=1047
    return a
class TestSpecialDict:
    def test_token_str(self):
        assert str(Token(TokenType.NUMBER,"2"))=="Token: TokenType.NUMBER, 2"
    def test_set_get(self):
        a=SpecialDict()
        a["1"]=1
        a["2"]=2
        assert a["1"] == 1
        assert a["2"] == 2
    def test_del(self):
        a=SpecialDict()
        a["1"]=1
        a["2"]=2
        del a["1"]
        assert a.keys()==["2"]
        assert a.items()==[('2', 2)]
        assert str(a)=="SpecialDict: {'2': 2}"
    def test_iloc(self,specialdict):
        assert specialdict.iloc(0) == 1
        assert specialdict.iloc(16) == -1
    @pytest.mark.parametrize(
        "cond,results",
         [(">2",[("3",3)]),
         ("<=3,   >=3",[("(2,3)",23),("(3,3)",33)]),
         (">1,   =2,",[("(3,2,3)",323),("(3,2,1)",321)]),
         (",,",[("(3,2,3)",323),("(3,2,1)",321),("(3,3,3)",333),("(1,2,3)",123),("(10,4,7)",1047),("4,4,4",444)]),
         ("<>2",[("(1)",1),("3",3)]),
         ("",[("(1)",1),("3",3),("2",2),("-1",-1)]),
         (",<2",[("(1,1)",11),("(4,1)",41)])]
    )
    def test_ploc(self,specialdict,cond,results):
        b=specialdict.ploc(cond)
        for res in results:
            assert b[res[0]]==res[1]
    def test_ploc_error(self,specialdict):
        with pytest.raises(SyntaxError):
            b=specialdict.ploc(">>2")
        with pytest.raises(SyntaxError):
            b=specialdict.ploc(">2 2")
        with pytest.raises(SyntaxError):
            b=specialdict.ploc("> >2")
        with pytest.raises(SyntaxError):
            b=SpecialDict()
            b[">2"]=2
            b.ploc("=1")
