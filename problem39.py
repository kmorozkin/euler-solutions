'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
 there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

'''
def triangle_right(hip, cat1, cat2):
    return hip ** 2 == cat1 ** 2 + cat2 ** 2

def hipotenuse_range(p):
    max = p // 2
    min = p // 3
    return range(min, max)

def triangles_gen(p, hip):
    min = 1
    max = p - hip - 1
    while max > min:
        if (triangle_right(hip, min, max)):
            yield (hip, min, max)
        min += 1
        max -= 1

occurrences = {}

for p in range(3, 1001):
    occurrences[p] = 0
    for hip in hipotenuse_range(p):
        for triangle in triangles_gen(p, hip):
            occurrences[p] += 1

occurrences_mirrored = {v:k for k, v in occurrences.items()}
max_occurrences = max(occurrences_mirrored)
print('Result: {} with occurrences {}'.format(occurrences_mirrored[max_occurrences], max_occurrences))