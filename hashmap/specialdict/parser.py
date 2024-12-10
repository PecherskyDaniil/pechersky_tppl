from .lexer import Lexer
from .token import Token,TokenType

class CondParser:
    def __init__(self):
        self._lexer=Lexer()
        self._current_token=None
        self._ops=[[]]
    def __check_token(self,type_: TokenType) -> None:
        if self._current_token.type_ == type_:
            self._current_token=self._lexer.next()
        #else:
            #raise SyntaxError("invalid token order")
    def __factor(self):
        token = self._current_token
        if token.type_==TokenType.DELIMETR:
            self._ops.append([])
            self.__check_token(TokenType.DELIMETR)
            return self.__factor()
        if token.type_==TokenType.OPERATOR:
            if len(self._ops[-1])!=1:
                self._ops[-1].append(token.value)
                self.__check_token(TokenType.OPERATOR)
                return self.__factor()
            else:
                raise SyntaxError("invalid token order")
        if token.type_==TokenType.NUMBER:
            if len(self._ops)==0 or len(self._ops[-1])!=1:
                raise SyntaxError("invalid token order")
            else:
                self._ops[-1].append(token.value)
                self.__check_token(TokenType.NUMBER)
                return self.__factor()
        if token.type_==TokenType.EOL:
            return self._ops
        #raise SyntaxError("invalid token order")
    def eval(self,s:str):
        if len(s)==0:
            return [[]]
        self._lexer.init(s)
        self._current_token=self._lexer.next()
        self._ops=[[]]
        return self.__factor()

class KeyParser:
    def __init__(self):
        self._lexer=Lexer()
        self._current_token=None
        self._numbers=[]
    def __check_token(self,type_: TokenType) -> None:
        if self._current_token.type_ == type_:
            self._current_token=self._lexer.next()
        #else:
        #    raise SyntaxError("invalid token order")
    def __factor(self):
        token = self._current_token
        if token.type_==TokenType.DELIMETR:
            self.__check_token(TokenType.DELIMETR)
            return self.__factor()
        if token.type_==TokenType.NUMBER:
            self._numbers.append(token.value)
            self.__check_token(TokenType.NUMBER)
            return self.__factor()
        if token.type_==TokenType.EOL:
            return self._numbers
        raise SyntaxError("invalid token order")
    def eval(self,s:str):
        self._lexer.init(s)
        self._current_token=self._lexer.next()
        self._numbers=[]
        return self.__factor()
