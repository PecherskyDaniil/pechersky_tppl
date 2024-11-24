from interpreter import Parser
from interpreter import Token,TokenType
from interpreter import Interpreter
with open('./tests/file.txt','r') as f:
    text=f.read()
print(text)
parser=Interpreter()
print(parser.eval("BEGIN x:=3/-2; y:=x END."))
