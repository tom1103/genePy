import random

char = 'abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&(-_)=$*!:;,?./§%<>#{[|`\^@]}'


def gen(n):
    i = 0
    l1 = []
    while i<n:
        a = random.choice(char)
        l1.extend(a)
        i = i+1
    l1 = "".join(l1)
    return l1

print(gen(25))