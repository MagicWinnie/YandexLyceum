import random
import json

words = json.load(open("words.json", "r", encoding="utf-8"))

length = int(input())
try:
    word = random.choice(words[length])
except KeyError:
    word = random.choice(words[str(length)])

closed_word = list(len(word) * "*")

check = 0
while True:
    print("Your word {}. Enter the letter.".format("".join(closed_word)))
    inp = input()
    if not inp.isalpha():
        print("Bad input. Try once more, please.")
    elif inp not in word:
        check += 1
        if check >= len(word):
            print(f"You loss! Word was {word}.")
            break
        else:
            print(f"There is no such letter in the word. Check is {check}.")
    else:
        for i in range(len(word)):
            if word[i] == inp:
                closed_word[i] = inp
        if "*" not in closed_word:
            print(f"You win! Your word is {word}.")
            break
