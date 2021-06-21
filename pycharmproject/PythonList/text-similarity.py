# counting punctuation as well as words
#Counts the word that are matching sample 1 with respect to sample 2

from collections import Counter
def checkCommonWords(sent1,sent2):
    elem1=list(sent1.split())
    elem2=list(sent2.split())

    #calculate frequency
    freq1=Counter(elem1)
    freq2=Counter(elem2)
    #print(freq1)
    #print(freq2)

    word=0
    score=0

    for i in range(len(elem1)):
        if elem1[word] in freq2.keys():
            score=score+1

        word+=1

        #word +=1
    print("words that are matching in sample 1 to sample 2")
    print(score)
    word=0
    score=0
    for i in range(len(elem2)):
        if elem2[word] in freq1.keys():
            score=score+1

        word+=1

        #word +=1
    print("words that are matching in sample 2 to sample 1")
    print(score)

f1 = open(r"C:\Users\RaviVerma\Desktop\BigDataGuide\python\Lab\pycharmproject\sample1.txt", "r")
f2 = open(r"C:\Users\RaviVerma\Desktop\BigDataGuide\python\Lab\pycharmproject\sample2.txt", "r")
sample1=f1.read()
sample2=f2.read()
checkCommonWords(sample1,sample2)
