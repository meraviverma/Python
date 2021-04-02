#Python program to remove words that are common in two Strings
# Given two strings S1 and S2, representing sentences, the task is to print both sentences after removing all words
# which are present in both sentences.
#
# Input: S1 = “sky is blue in color”, S2 =”Raj likes sky blue color “
# Output: is in
#              Raj likes
# Explanation: The common words are [ sky, blue, color ]. Removing these words from the two sentences modifies the
# sentences to the specified output.
#
# Input: S1 = “learn data structures and algorithms in “, S2 = “ is the computer science portal
# for Geeks“
# Output: learn data structures and algorithms in
#               is the computer science portal for.

from collections import Counter
def removeCommonWords(sent1,sent2):
    elem1=list(sent1.split())
    elem2=list(sent2.split())

    #calculate frequency
    freq1=Counter(elem1)
    freq2=Counter(elem2)
    print(freq1)
    print(freq2)

    word=0

    for i in range(len(elem1)):
        if elem1[word] in freq2.keys():
            elem1.pop(word)

            word=word-1

        word +=1

    word=0

    for i in range(len(elem2)):
        if elem2[word] in freq1.keys():
            elem2.pop(word)

            word=word-1

        word +=1

    print(*elem1)
    print(*elem2)


sentence1 = "sky is blue in color"
sentence2 = "raj likes sky blue color"

removeCommonWords(sentence1, sentence2)

#Output
# Counter({'sky': 1, 'is': 1, 'blue': 1, 'in': 1, 'color': 1})
# Counter({'raj': 1, 'likes': 1, 'sky': 1, 'blue': 1, 'color': 1})
# ['is', 'in']
# ['raj', 'likes']