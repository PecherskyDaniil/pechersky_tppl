import re
from .parser import KeyParser,CondParser
class SpecialDict(dict):
    def __init__(self):
        self.__dict__={}
    def __getitem__(self,item):
        return self.__dict__[item]
    def ploc(self,item):
        ops=CondParser().eval(item)
        tempdict={}
        for key in self.__dict__.keys():
            if not(any(c.isalpha() for c in key)):
                keysarr=KeyParser().eval(key)
                if len(keysarr)==len(ops):
                    p=0
                    
                    for i in range(len(ops)):
                        if len(ops[i])==0:
                            p+=1
                        elif self.__check_cond(float(keysarr[i]),ops[i][0],float(ops[i][1])):
                            p+=1
                    if p==len(ops):
                        tempdict[key]=self.__dict__[key]
        return tempdict
    def iloc(self,key):
        td=[self.__dict__[x] for x in sorted(self.__dict__)]
        return td[key]
    def __check_cond(self,item,cond,conditem):
        if cond=="=":
            return item==conditem
        elif cond==">":
            return item>conditem
        elif cond=="<":
            return item<conditem
        elif cond==">=":
            return item>=conditem
        elif cond=="<=":
            return item<=conditem
        elif cond=="<>":
            return item!=conditem
    def __setitem__(self,key,value):
        self.__dict__[key]=value
    def __delitem__(self,item):
        del self.__dict__[item]
    def keys(self):
        return list(self.__dict__.keys())
    def items(self):
        return list(self.__dict__.items())
    def __str__(self):
        return "SpecialDict: "+str(self.__dict__)

