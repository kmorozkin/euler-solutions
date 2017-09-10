'''
The series, 1^1 + 2^ + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 10001000.

'''
num = sum(x ** x for x in range(1,1001))
print(str(num)[-10:])