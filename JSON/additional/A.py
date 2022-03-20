import json

words = json.load(open("russian_words.json", "r", encoding="utf-8"))

last_letter = ""
winner = True
used_words = set()
while True:
    user_word = input()
    if user_word.lower() == "сдаюсь":
        winner = False
        break
    lst_cur_let = user_word[-1] if user_word[-1] not in "ьы" else user_word[-2]
    if user_word[0] not in words or user_word not in words[user_word[0]]:
        print("Такого слова нет.")
        continue
    if last_letter != "" and last_letter != user_word[0]:
        print("Это слово не на букву %s." % (last_letter))
        continue
    if user_word in used_words:
        print("Это слово уже было.")
        continue
    if len(words[lst_cur_let]) == 0:
        winner = True
        break
    word = words[lst_cur_let][0]
    last_letter = word[-1] if word[-1] not in "ьы" else word[-2]
    used_words.add(word)
    del words[word[0]][0]
    print(word)

winner_name = "пользователь" if winner else "компьютер"
print("Игра закончена! Победил %s." % (winner_name))
