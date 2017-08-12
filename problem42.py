'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
 number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
common English words, how many are triangle words?

'''
from itertools import count


def is_triangle(num, cache = set()):
    largest = 1
    cache.add(1)
    gen = (x * (x + 1) / 2 for x in count(1,1))
    while largest < num:
        next_value = next(gen)
        largest = next_value
        cache.add(next_value)
    return num in cache

def word_to_positions(word: str):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return list(map(lambda x : x + 1, map(letters.find, word.lower())))

text = ''
with open('resources/problem42_words.txt') as stream:
    text += stream.readline()

triangle_words = 0
for word in text.split(','):
    truncated = word.strip('\"')
    word_number = sum(word_to_positions(truncated))
    if (is_triangle(word_number)):
        triangle_words += 1

print(triangle_words)