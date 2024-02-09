from itertools import permutations
def permutation(s):
    a = permutations(s)
    for i in list(a):
        print(i)
s = int(input())
permutation(s)