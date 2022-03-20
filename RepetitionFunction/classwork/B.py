import sys
from collections import Counter

for line in sys.stdin:
    tmp = line.split()
    wordOrig = tmp[0]
    words = tmp[1:]

    wordOrigCounter = Counter(wordOrig)
    wordsOut = []
    for word in words:
        wordCounter = Counter(word)
        for letter in wordCounter:
            if wordCounter[letter] > wordOrigCounter[letter]:
                break
        else:
            wordsOut.append(word)

    print(*sorted(wordsOut, key=lambda x: len(x), reverse=True))
