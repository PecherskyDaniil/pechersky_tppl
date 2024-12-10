from .token import Token,TokenType
from .lexer import Lexer
from .ast import Number,BinOp,UnaryOp,Variable

class Parser:

    def __init__(self):
        self._lexer=Lexer()
        self._current_token=None
        self._vars=[]
    def __check_token(self,type_: TokenType) -> None:
        if self._current_token.type_ == type_:
            self._current_token=self._lexer.next()
        else:
            raise SyntaxError("invalid token order")
    def __factor(self):
        token = self._current_token
        if token.value=="+":
            self.__check_token(TokenType.OPERATOR)
            return UnaryOp(token,self.__factor())
        if token.value=="-":
            self.__check_token(TokenType.OPERATOR)
            return UnaryOp(token,self.__factor())
        if token.type_==TokenType.NUMBER:
            self.__check_token(TokenType.NUMBER)
            return Number(token)
        if token.type_==TokenType.ID:
            self.__check_token(TokenType.ID)
            return Variable(token,Number(None))
        if token.type_==TokenType.LPAREN:
            self.__check_token(TokenType.LPAREN)
            result=self.__expr()
            self.__check_token(TokenType.RPAREN)
            return result
        
        raise SyntaxError("invalid token order")
    def __term(self):
        result=self.__factor()
        while self._current_token and (self._current_token.type_==TokenType.OPERATOR):
            if self._current_token.value not in ['*','/']:
                break
            token = self._current_token
            self.__check_token(TokenType.OPERATOR)
            result=BinOp(result,token,self.__factor())
        return result
    def __expr(self)->BinOp:
        result=self.__term()
        while self._current_token and (self._current_token.type_==TokenType.OPERATOR):
            if self._current_token.value not in ['+','-']:
                break
            token=self._current_token
            self.__check_token(TokenType.OPERATOR)
            result= BinOp(result,token,self.__term())
        return result
    
    def __assignment(self):
        token=self._current_token
        if token.type_==TokenType.ID:
            self.__check_token(TokenType.ID)
            self.__check_token(TokenType.ASSIGN)
            result=Variable(token,self.__expr())
            return result
    
    def __statement(self):
        token=self._current_token
        if token.type_==TokenType.ID:
            result=self.__assignment()
            self._vars.append(result)
        elif token.type_==TokenType.BEGIN:
            self.__complex_statement()
            return
        else:
            raise SyntaxError("Invalid statement")
    def __statement_list(self):
        token=self._current_token
        if token.type_==TokenType.END:
            return 
        self.__statement()
        token=self._current_token
        if token.type_==TokenType.SEMI:
            self.__check_token(TokenType.SEMI)
            self.__statement_list()
            return
        elif token.type_==TokenType.END:
            return 
        else:
            raise SyntaxError("Wrong end of statement")
    def __complex_statement(self):
        token = self._current_token
        if token.type_==TokenType.BEGIN:
            self.__check_token(TokenType.BEGIN)
            self.__statement_list()
            self.__check_token(TokenType.END)
            return
        else:
            raise SyntaxError("BEGIN END problem")
    def program(self,s:str):
        self._lexer.init(s)
        self._current_token=self._lexer.next()
        self.__complex_statement()
        self.__check_token(TokenType.EOL)
        return self._vars
    
    