from sys import argv

userinp = argv[1:]

def answ(userinp):
    if len(userinp) == 3:
        try:
            return eval(''.join(userinp))        
        except:
           return None
    else:
        return None
print(answ(userinp))