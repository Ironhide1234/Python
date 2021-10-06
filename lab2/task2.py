import re

dividers = ".!?"

class text:
    def __init__(self,filename):
        self.filename = filename
    def filered(self):
        f = open(self.filename, "r")
        sense = f.read()   
        symb = str(len(sense) - sense.count(' ') - sense.count('\n'))  
        words  = str(len(sense.split()))
        sent = str(len(re.split(r'[!/?/.]',sense)))
        f.close()
        return symb,words,sent

A = text("task2.txt")
smb,wrd,snt = A.filered()
print("Symbols: " + smb,"Words: " + wrd,"Sentences: " + snt)

