import numpy as np
import os
import pickle
import math
spamFiles = os.listdir('Spam')
hamFiles = os.listdir('Ham')

spam = []
ham = []

for fname in spamFiles:
    f = open("Spam/"+fname)
    mailStr = ""
    for line in f:
        mailStr = mailStr + line
    spam.append(mailStr)

for fname in hamFiles:
    f = open("Ham/"+fname)
    mailStr = ""
    for line in f:
        mailStr = mailStr + line
    ham.append(mailStr)

data = {'spam': spam, 'ham': ham}

pickleOut = open('Dataset.pickle', 'wb')
pickle.dump(data, pickleOut)

def isNum(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
stopwords = set([" ", "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours	ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"])

avoidChars = set([".", "+", "-", "|", "\r", "\n", "/", ":", "!", "\x00", "\xff", "=", "%", "'", ",", "*", "_", "__"])

for idx, document in enumerate(spam):
    spam[idx] = "".join([c if c not in unwanted else " " for c in spam[idx]])
    spam[idx] = spam[idx].split(" ")
    

for idx, document in enumerate(ham):
    ham[idx] = "".join([c if c not in unwanted else " " for c in ham[idx]])
    ham[idx] = ham[idx].split(" ")

for idx, doc in enumerate(ham):
    ham[idx] = [item.lower() for item in ham[idx] if item != "" and item.lower() not in stopwords and not isNum(item.lower())]

for idx, doc in enumerate(spam):
    spam[idx] = [item.lower() for item in spam[idx] if item != "" and item.lower() not in stopwords  and not isNum(item.lower())]

spamtest = spam[int(len(spam)*0.9):]
hamtest = ham[int(len(ham)*0.9):]

spamval = spam[int(len(spam)*0.85): int(len(spam)*0.9)]
hamval = ham[int(len(ham)*0.85):int(len(ham)*0.9)]

spam = spam[:int(len(spam)*0.85)]
ham = ham[:int(len(ham)*0.85)

#print(len(spamval), len(spam))

#print ("len(spamval)")
#print (' len ( spam ) ')
print (spam)
Pspam = len(spam)*1.0/(len(spam)+len(ham))
Pham = 1-Pspam
Pspam, Pham