'''
Created on Oct 28, 2013

@author: anujacharya
'''
import re


def compute(words,search_word):
    result = list()
    for word in words:
        x =  re.search(r'^'+search_word+'.*', word, flags=0)
        if x is not None:
            result.append(x.group())
            if (len(result) == 10):
                break
    print result
            
        
if __name__ == '__main__':
    DICTIONARY = "/usr/share/dict/words";
    TARGET = 'verr'

    # read dictionary file
    words = open(DICTIONARY, "rt").read().split();
    
    compute(words,TARGET)