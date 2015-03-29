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

<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
print(gen(25))
=======
>>>>>>> Stashed changes
    def createList(self, *args):
        """Creer une liste en fonction des options choisis"""
        self.l = []
        for key in args:
            if key=='char':
               self.l += CHARACTERS
            if key=='num':
<<<<<<< HEAD
               self.l += NUMBERS
            if key=='spe':
               self.l += SPECIALS
=======
<<<<<<< Updated upstream
               self. l += NUMBERS
            if key=='spe':
               self. l += SPECIALS
=======
               self.l += NUMBERS
            if key=='spe':
               self.l += SPECIALS
>>>>>>> Stashed changes
>>>>>>> Delete spaces
        self.l = "".join(self.l)

    def gen(self, n):
        """Generate sentence with n symbols"""
        i = 0
        l1 = []
        while i<n:
            a = random.choice(self.l)
            l1.extend(a)
            i = i+1
        l1 = "".join(l1)
<<<<<<< HEAD
        return l1
=======
        return l1
<<<<<<< Updated upstream
char = True
gen1 = Generator()
gen1.createList('num')
print(gen1.gen(34))
=======

char = True
gen1 = Generator()
gen1.createList('num')
print(gen1.gen(34))
>>>>>>> Stashed changes
>>>>>>> Stashed changes
>>>>>>> Delete spaces
