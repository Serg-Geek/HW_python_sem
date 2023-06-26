# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один
# допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


backpack_capacity = int(input('Введите  максимальную  грузоподъёмность рюкзака в кг -->>')) * 1000

backpack = {
    'зажигалка': 20,
    'компас': 100,
    'фрукты': 500,
    'термос': 1000,
    'аптечка': 200,
    'бинокль': 400,
    'бутерброды': 820,
    'палатка': 5500,
    'спальник': 2250,
    'водка': 600
}
def backpack_equipment(backpack, backpack_capacity):
    if not backpack:
        return []
    res = []
    for k, v in backpack.items():
        if v <= backpack_capacity:
            res.append(k)
            backpack_capacity -= v
    return res

def backpack_sort(backpack, backpack_capacity):
    if not backpack:
        return []
    res = []
    sort_backpack = dict(sorted(backpack.items(), key=lambda x: -x[1]))
    for k, v in sort_backpack.items():
        if v <= backpack_capacity:
            res.append(k)
            backpack_capacity -= v
    return res

print(f'в рюкзак поместятся {backpack_equipment(backpack, backpack_capacity)}')
print(f'в отсортированный рюкзак поместятся {backpack_sort(backpack, backpack_capacity)}')
