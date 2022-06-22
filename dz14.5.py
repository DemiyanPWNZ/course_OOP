class Dog:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def com_jump(self):
        print ("Собака подпрыгнула")

    def com_run(self):
        print('Собака убежала от Вас')

    def com_bark(self):
        print("Wof-wof! Wof-wof! Wof-wof!")

    def com_birthday(self):
        self.age += 1

    def com_sleep(self):
        print('Собака спит!')



class Cat:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def com_jump(self):
        print ("Кот подпрыгнул")

    def com_run(self):
        print('Кот убежал от Вас')

    def com_meow(self):
        print("Meow-meow! Meow-meow! Meow-meow!")

    def com_birthday(self):
        self.age += 1

    def com_sleep(self):
        print('Кот спит!')


class Parrot:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def com_jump(self):
        print ("Попугай прыгает")

    def com_run(self):
        print('Попугай убежал от Вас')

    def com_fly(self):
        print("Попугай улетел ")

    def com_birthday(self):
        self.age += 1

    def com_sleep(self):
        print('Попугай уснул!')




