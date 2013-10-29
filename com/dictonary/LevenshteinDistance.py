#!/usr/bin/python
import time
import sys

def levenshtein( word1, word2 ):
    columns = len(word1) + 1
    rows = len(word2) + 1

    # build first row
    currentRow = [0]
    for column in xrange( 1, columns ):
        # Inital condition to fill with 0,1,2
        currentRow.append( currentRow[column - 1] + 1 )

    for row in xrange( 1, rows ):
        previousRow = currentRow
        currentRow = [ previousRow[0] + 1 ]

        for column in xrange( 1, columns ):

            insertCost = currentRow[column - 1] + 1 # 2

            deleteCost = previousRow[column] + 1 # 2

            if word1[column - 1] != word2[row - 1]:
                replaceCost = previousRow[ column - 1 ] + 1
            else:                
                replaceCost = previousRow[ column - 1 ] # 0

            currentRow.append( min( insertCost, deleteCost, replaceCost ) )

    return currentRow[-1]

def search( words, word, maxCost ):
    results = []
    for word in words:
        
        if (len(results) == 10):
            # No need to process any more words
            break
        
        cost = levenshtein( TARGET, word )

        if cost <= maxCost:
            results.append(word )

    return results

if __name__ == '__main__':
    DICTIONARY = "/usr/share/dict/words";
    TARGET = 'yello'
    MAX_COST = 1

    # read dictionary file
    words = open(DICTIONARY, "rt").read().split();
    results = search( words, TARGET, MAX_COST )

    for result in results: print result        
