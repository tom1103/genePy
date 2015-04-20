import random

CHARACTERS = ['abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ']
NUMBERS = ['0123456789']
SPECIALS = ['&(-_)=$*!:;,?./§%<>#{[|`\^@]}']

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
        pass

    def createList(self, *args):
        """Creer une liste en fonction des options choisis"""
        self.l = []
        for key in args:
            if key == 'all':
                self.l = CHARACTERS+NUMBERS+SPECIALS
                self.l = "".join(self.l)
            else:
                if key == 'char':
                    self.l += CHARACTERS
                if key == 'num':
                    self.l += NUMBERS
                if key == 'spe':
                    self.l += SPECIALS

                self.l = "".join(self.l)

    def gen(self, n):
        """Generate sentence with n symbols"""
        i = 0
        n = int(n)
        l1 = []
        while i < n:
            a = random.choice(self.l)
            l1.extend(a)
            i = i+1
        l1 = "".join(l1)
        return l1
