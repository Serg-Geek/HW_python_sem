# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не  должно  быть  дубликатов.

original_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
duplicates_list = list(set([x for x in original_list if original_list.count(x) > 1]))
print(duplicates_list)
