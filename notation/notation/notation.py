import numpy as np
operators=["+","-","/","*"]
def separate(string: str):
    elems=np.array(string.split(" "))
    ops=elems[np.isin(elems,operators)]
    try:
        digs=elems[np.logical_not(np.isin(elems,operators))].astype(int)
    except:
        raise SyntaxError("Invalid input: only digits!")
    if ops.shape[0]>=digs.shape[0]:
        raise SyntaxError("Invalid input: too many operators!")
    if ops.shape[0]<digs.shape[0]-1:
        raise SyntaxError("Invalid input: too many digits!")
    return ops,digs
def is_prefix(string: str) -> bool:
    arr=string.split(" ")
    opdigcounter=1
    for i in range(len(arr)):
        if arr[i] in operators:
            opdigcounter+=1
        else:
            opdigcounter-=1
        if opdigcounter<0:
            return False
    return True
def in_infix(string: str) -> str:
    if not(is_prefix(string)):
        raise SyntaxError("Invalid input: only prefix!")
    ops,digs=separate(string)
    cd=0
    new_string=""
    co=0
    while co<ops.shape[0] or cd<digs.shape[0]:
        if cd<digs.shape[0]:
            new_string+=str(digs[cd])+" "
            cd+=1
        if co<ops.shape[0]:
            new_string+=ops[co]+" "
            co+=1
    return new_string[:-1]
        
