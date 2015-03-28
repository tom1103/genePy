import random

CHAR = ['abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ']
NUMBERS = ['0123456789']
SPECIAL = ['&(-_)=$*!:;,?./§%<>#{[|`\^@]}']

firstupper = True
firstspecial = True
onlyupper = False
onlylower = False
onlyspecial = False
onlychar = False
special = True

class Generator(object):
    """Generate password with caracteritics"""
    def __init__(self):
        self.l = self._createList()

    def _createList(self):
        l = CHAR+NUMBERS+SPECIAL
        l = "".join(l)
        return l

    def gen(self, n):
        """Generate sentence with n symbols"""
        i = 0
        l1 = []
        while i<n:
            a = random.choice(self.l)
            l1.extend(a)
            i = i+1
        l1 = "".join(l1)
        return l1

gen1 = Generator()
print(gen1.gen(34))