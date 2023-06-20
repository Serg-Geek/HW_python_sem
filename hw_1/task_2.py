# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.



def digit_check():
    while True:
        try:
            lenght = float(input('Enter the number:\n'))
            return lenght
        except ValueError:
            print('Please, enter the number\n')
            continue

print("enter the length of side 'a' of the triangle")
a =  digit_check() 
print("enter the length of side 'b' of the triangle")
b = digit_check()
print("enter the length of side 'c' of the triangle")
c = digit_check()

TRIANGLE_NO = "triangle does not exist"
TRIANGLE_EQULATIRAL = "equilateral triangle"
TRIANGLE_SCALENE = "scalene triangle"
TRIANGLE_ISOSCELES = "isosceles triangle"

if a > b + c or  b > c + a or c > a + b:
    print(TRIANGLE_NO)
elif  a == b == c:
    print(TRIANGLE_EQULATIRAL)
elif a == b or a == c or c == b:
    print(TRIANGLE_ISOSCELES) 
else: 
    print(TRIANGLE_SCALENE)
    