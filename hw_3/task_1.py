# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга,
# а значение — кортеж вещей. Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
#
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
#
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.



all_frends = {
    'Серж': ('палатка', 'кружка', 'свечка', 'нож', 'карты', 'топор', 'мангал', 'водка', 'презервативы'),
    'Пётр': ('спальник', 'кружка', 'котелок', 'нож', 'консервы', 'водка', 'чай', 'одеяло', 'коврик',\
             'фонарь', 'розжиг', 'шампуры', 'гитара', 'тарелка', 'ложка', 'вилка'),
    'Алёна': ('спальник', 'кружка', 'ложка', 'тарелка', 'нож', 'продукты', 'презервативы', 'вино "Анапа"',\
              'туалетная бумага')
}

# Находим общие элементы между множествами друзей
all_items = set.intersection(*[set(items) for items in all_frends.values()])
print(f'Вещи, которые взяли все друзья: {all_items}')

# Находим уникальные элементы и имена друзей, которые их взяли
unique_items = {}
duplicates = set()
for friend, items in all_frends.items():
    for item in items:
        if item not in duplicates:
            if item in unique_items:
                duplicates.add(item)
                del unique_items[item]
            else:
                unique_items[item] = friend
print(f'Уникальные  вещи и имена друзей: {unique_items}')

# Находим вещи, которые есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
missing_items = {}
for friend, items in all_frends.items():
    for item in items:
        if item not in missing_items:
            missing_items[item] = {friend}
        else:
            missing_items[item].add(friend)
for item, friends in missing_items.items():
    if len(friends) == len(all_frends) - 1:
        print(f'Вещь,  которая  есть у всех кроме {friends.difference(all_items).pop()}: {item}')
