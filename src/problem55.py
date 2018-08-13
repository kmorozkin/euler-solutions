'''
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that
never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature
of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise.
In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than
fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a
palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a
palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?
'''
from src.utils.digits import num2digits, digits2num

ITERATION_CEIL = 50


def is_palindrome(number):
    digits = num2digits(number)
    size = len(digits)
    for i in range(size // 2):
        if digits[i] != digits[size - i - 1]:
            return False
    return True


def reverse_add(number):
    digits = num2digits(number)
    digits.reverse()
    reversed_number = digits2num(digits)
    return number + reversed_number


Lychrel = 0
for i in range(10000):
    next_num = reverse_add(i)
    count = 0
    while not is_palindrome(next_num) and count < ITERATION_CEIL:
        next_num = reverse_add(next_num)
        count += 1
    if count == ITERATION_CEIL:
        Lychrel += 1
print(Lychrel)

