from .token import TokenType,Token
from .ast import BinOp,Number,UnaryOp,Variable
from .parser import Parser
class NodeVisitor:
    def visit(self):
        pass

class Interpreter(NodeVisitor):
    
    def __init__(self):
        self._parser=Parser()
        self._vars={}

        
    def visit(self,node):
        if isinstance(node,Number):
            return self._visit_number(node)
        elif isinstance(node,BinOp):
            return self._visit_binop(node)
        elif isinstance(node,UnaryOp):
            return self._visit_unaryop(node)
        elif isinstance(node,Variable):
            return self._visit_var(node)
    def _visit_number(self,node:Number)->float:
        return float(node.token.value)
    def _visit_var(self,node:Variable):
        if node.id.value in self._vars:
            return float(self._vars[node.id.value])
        else:
            raise RuntimeError("variable isnt defined before")
    def _visit_unaryop(self,node:UnaryOp)->float:
        match node.op.value:
            case "+":
                return +self.visit(node.expr)
            case "-":
                return -self.visit(node.expr)
            case _:
                raise RuntimeError("invalid operator")
    def _visit_binop(self,node:BinOp)->float:
        match node.op.value:
            case "+":
                return self.visit(node.left)+self.visit(node.right)
            case "-":
                return self.visit(node.left)-self.visit(node.right)
            case "*":
                return self.visit(node.left)*self.visit(node.right)
            case "/":
                return self.visit(node.left)/self.visit(node.right)
            case _:
                raise RuntimeError("invalid operator")
    def eval(self,code:str)->float:
        trees=self._parser.program(code)
        for tree in trees:
            self._vars[tree.id.value]=self.visit(tree.expr)
        return self._vars