import re

dividers = ".!?"

class text:
    def __init__(self,filename):
        if isinstance(filename,str):
            self.filename = filename
        else:
            raise TypeError('Wrong type')

    def symbols(self):
        f = open(self.filename, "r")
        sense = f.read()   
        symb = str(len(sense) - sense.count(' ') - sense.count('\n')) 
        f.close()
        return symb
    def word(self):  
        f = open(self.filename, "r") 
        sense = f.read()   
        words  = str(len(sense.split()))
        f.close()
        return words
    def sentences(self):   
        f = open(self.filename, "r") 
        sense = f.read()   
        sent = str(len(re.split(r'[!/?/.]',sense)))
        f.close()
        return sent

A = text("task2.txt")
sym = str(A.symbols())
wrd = str(A.word())
sent = str(A.sentences())
print("Symbols: " + sym,"Words: " + wrd,"Sentences: " + sent)