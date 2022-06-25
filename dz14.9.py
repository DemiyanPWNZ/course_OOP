class NonNegativeName:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value == '' or value.isdigit():
                raise ValueError("Name cannot be negative")
        instance.__dict__[self.name] = value




class Pet:
    name = NonNegativeName()

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master


    @property
    def noage(self):
        return self.age

    @noage.setter
    def noage(self, value):
        if value < 0:
            raise ValueError("Cannot be negative")
        self.age = value

    def com_jump(self):
        print(f"{self.name} подпрыгнула")

    def com_run(self):
        print(f'{self.name} убежала от Вас')

    def com_birthday(self):
        self.age += 1

    def com_sleep(self):
        print(f'{self.name} спит!')


class Dog(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def com_bark(self):
        print("Wof-wof! Wof-wof! Wof-wof!")


class Cat(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def com_meow(self):
        print("Meow-meow! Meow-meow! Meow-meow!")


class Parrot(Pet):

    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def com_fly(self):
        print(f"Попугай {self.name} улетел ")


dog1 = Dog('6loxa', 5, 'semi-master')
cat1 = Cat('kisa', 10, 'master')
parrot1 = Parrot('kakady', 7, 'anti-master')

dog1.com_jump()
dog1.com_sleep()
dog1.com_birthday()
dog1.com_run()
dog1.com_bark()

cat1.com_jump()
cat1.com_sleep()
cat1.com_birthday()
cat1.com_run()
cat1.com_meow()
cat1.name = ''

parrot1.com_run()
parrot1.com_fly()
parrot1.com_birthday()
parrot1.com_jump()
parrot1.com_sleep()