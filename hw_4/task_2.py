# Напишите функцию для транспонирования матрицы

def transp_matrix(matrix):
    transposed = list(zip(*matrix))
    return transposed

matrix = [[1, 2, 7], [3, 4, 8], [5, 6, 9] ]
res_matrix = transp_matrix(matrix)
print(matrix)
print(res_matrix)
