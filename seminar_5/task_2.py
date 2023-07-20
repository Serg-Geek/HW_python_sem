from sys import argv
from guess_num import guess_num as gn

lower_limit, upper_limit, quantity = (int(i) for i in argv[1:])#для работы в терминале

print(gn(lower_limit, upper_limit, quantity))
