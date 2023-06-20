# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.



START = 2
END = 10
HALF = 2

for i in range(START, END):
    for j in range(START, END // HALF + 1):
        print(f"{j:>2} X {i:>1} = {i * j:>2}", end="   ")
    print()
print()
for i in range(START, END):
    for j in range(END // HALF + 1, END):
        print(f"{j:>2} X {i:>1} = {i * j:>2}", end="   ")
    print()