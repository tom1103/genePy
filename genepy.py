from generator import *
from db import *
from docopt import docopt


help = """Usage: genepy.py generate [--lenght=<INT>]
                 genepy.py read
                 genepy.py save [(<login> <password> <note>)]

    Options:
        -l --lenght=<INT>           Password lenght
        -h --help                   Print this help
"""

generator = Generator()
db = Db()


def principal(arguments):
    lenght = arguments.get('--lenght') or False
    login = arguments.get('<login>') or False
    password = arguments.get('<password>') or False
    note = arguments.get('<note>') or False

    if arguments.get('--help'):
        print(help)

    if arguments.get('generate'):
        generator.createList('all')
        if int(lenght) > 0:
            print(generator.gen(lenght))
        else:
            print(generator.gen(25))

    if arguments.get('read'):
        try:
            data = db.readData()
            db.close()
            print(data)
        except:
            print("Read error !")

    if arguments.get('save'):
        try:
            db.dataInsert(login, password, note)
            db.close()
            print(("These datas \n\nlogin : {}\npassword : {}\nnote : {}\n\nhas been saved").format(login, password, note))
        except:
            print("Error ! Datas not saved")

if __name__ == "__main__":
    principal(docopt(help))
