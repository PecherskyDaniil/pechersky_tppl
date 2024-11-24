import pytest
from interpreter import Interpreter
from interpreter import Token,TokenType
from interpreter import ast
@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()
class TestInterpreter:
    @pytest.mark.parametrize(
        "string,result",
        [("BEGIN x:=2+2; END.",{"x":4.0}),
         ("BEGIN x:=2+2; y :=3+3 END.",{"x":4.0,"y":6}),
         ("BEGIN x:=2+2; y:=x+3; END.",{"x":4.0,"y":7}),
         ("BEGIN x:=2+2; x : =x+3 END.",{"x":7.0}),
         ("BEGIN x:=2+2; BEGIN y:=x+3; z:=y+3 END; z:=z-x END.",{"x":4.0,"y":7.0,"z":6.0}),
         ("BEGIN x:=2*2; y:=(x+6)/2; END.",{"x":4.0,"y":5.0}),
         ("BEGIN x:=-4; y:=(x+6)/2; END.",{"x":-4.0,"y":1.0}),
         ("BEGIN x:=+4; y:=(x+6)/2; END.",{"x":4.0,"y":5.0})]
    )
    def test_constrcutions(self,string,result,interpreter):
        assert interpreter.eval(string) == result
    
    def test_begin_end_error(self,interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN x:=3;.")
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN x:=3; END END.")
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN x:=3; BEGIN END.")
        with pytest.raises(SyntaxError):
            interpreter.eval("x:=3; END.")

    def test_no_dot_error(self,interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN x:=3; END")
    def test_semi_error(self,interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN x:=3 y:=x END.")
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN x:=3;; END.")
    def test_wrong_expr(self,interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN x :=/3; y:=x END.")
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN x:=3/*2; y:=x END.")
        with pytest.raises(RuntimeError):
            interpreter.eval("BEGIN x:=3-z; y:=x END.")
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN $ x:=3-3 y:=x END.")
    def test_bad_assign(self,interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN x:s=3; y:=x END.")
    def test_node_print(self):
        n1=ast.Number(Token(TokenType.NUMBER,"2"))
        n2=ast.Number(Token(TokenType.NUMBER,"3"))
        assert str(n1)=="Number Token: TokenType.NUMBER, 2"
        assert str(ast.BinOp(n1,Token(TokenType.OPERATOR,"+"),n2))=="BinOp +(Number Token: TokenType.NUMBER, 2, Number Token: TokenType.NUMBER, 3)"
        assert str(ast.UnaryOp(Token(TokenType.OPERATOR,"-"),n2))=="UnaryOp -(Number Token: TokenType.NUMBER, 3))"
        assert str(ast.Variable(Token(TokenType.ID,"n"),n1))=="Variable Token: TokenType.ID, n = Number Token: TokenType.NUMBER, 2"
    
