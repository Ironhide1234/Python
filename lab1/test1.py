import sys

def answ(oper):
    return eval(oper)

oper = "".join(sys.argv[1:])
   
print(answ(oper))