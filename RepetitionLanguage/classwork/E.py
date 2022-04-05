n = int(input())

names = ['Имиш', 'Ик', 'Акбаль', 'Кан', 'Чик-Чан', 'Кими', 'Маник', 'Ламат',
         'Мулук', 'Ок', 'Чуэн', 'Эб', 'Бен', 'Хиш', 'Мен', 'Киб', 'Кабан',
         'Эцнаб', 'Кавак', 'Ахау']

day_count = 1
inner_day_count = 1
for i in range(1, n + 1):
    if day_count > 13:
        day_count = 1
    if inner_day_count > 20:
        inner_day_count = 1
    day_count += 1
    inner_day_count += 1
print(f"Номер дня: {day_count - 1}")
print(f"Название дня: {names[inner_day_count - 2]}")
