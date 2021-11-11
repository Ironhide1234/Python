import re
import string

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
        symb = len(f.read())
        f.close()
        return symb

    def count_words(self):  
        f = open(self.filename)    
        words = len(re.findall(r'[a-zA-Z-\']+', f.read()))
        f.close()
        return words

    def count_sentences(self):   
        f = open(self.filename)    
        sent = len(re.split(r'[!/?/.]+',f.read()))
        f.close()
        return sent

A = Text("task2.txt")
sym = A.count_symbols()
wrd = A.count_words()
sent = A.count_sentences()
print(f'Symbols: {sym} Words: {wrd} Sentences: {sent}')