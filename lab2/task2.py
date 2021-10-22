import re
import string

dividers = ".!?"

class Text:
    def __init__(self,filename):
        if not isinstance(filename,str):
            raise FileNotFoundError('No file found')
        try:
            with open(filename):
                pass   
        except(IOError,FileNotFoundError):
            exit(0)
        self.filename = filename
            
    def count_symbols(self):
        f = open(self.filename)  
        symb = str(len(f.read()) - len(string.whitespace))
        f.close()
        return symb

    def count_words(self):  
        f = open(self.filename)    
        words  = str(len(f.read().split()))
        f.close()
        return words

    def count_sentences(self):   
        f = open(self.filename)    
        sent = str(len(re.split(r'[!/?/.]',f.read())))
        f.close()
        return sent

A = Text("task2.txt")
sym = (A.count_symbols())
wrd = str(A.count_words())
sent = str(A.count_sentences())
print("Symbols: " + sym,"Words: " + wrd,"Sentences: " + sent)