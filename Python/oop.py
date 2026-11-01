# # OOP MOLCHALOV

# ### _Video 0_

import requests

r = requests.get('https://google.ru')

type(r)

dir(r)

dir(requests)


# ### *video 1*

class Person:
    name = 'Ivan'


Person.name

# в пайтон все является обьектами, даже классы: фунции модули классы

Person.__name__

dir(Person)

Person.__class__

p =  Person()

type(p)

p.__class__.__name__

p.__class__

new_person = type(p)()

new_person

id(p) == id (new_person)

id (new_person)

id(p)


# ### **Video 2**

class Person:
    name = 'Ivan'


dir(Person)

Person.__dict__

Person.__dict__['name'] = 'asdsad'

# +
#getattr()
#setattr()
#delattr()
# -

Person.name

Person.age = 234324

Person.__dict__

getattr(Person, 'name')

setattr(Person, 'dob', 123)

Person.__dict__

delattr(Person, 'dob')

Person.__dict__


class Person:
    name = 'Ivan'
    def hello():
        print("hello")


Person.hello()

Person.__dict__


# ### **Video 3**

class Person:
    name = 'Ivan'


print(Person.__dict__)

# +
#callable object cuz added class of class method: __call__()   which does every object callable 
# -

p1 = Person()

p1

p2 = Person()

id(p1)

id(p2)

# Свойства класса глобальны для всех объектов

p1.name

p2.name

id(p1.name)

id(p2.name)

id(Person.name)

p1.__dict__

p2.__dict__

Person.__dict__

p1.name = "Akakii"

p2.name = "Tolyan"

p1.__dict__

p2.__dict__

p2.age = 13423

p2.__dict__

# Поскольку питон динамический язык, были созданы новые свойства экземпляров класса, которые были занесены в локальный словарь пространства имен для этих объектов

p1.name

p2.name

Person.__dict__

p1.age

p1 = Person()

p2 = Person()

Person.name = 'Uzbek228'

p1.name

p2.name


# Класс - колабл  объект. При вызове класса, мы получаем его экзмепляр. Экземпляры класса и клаассы имеют изолированные друг от друга пространства имен ("которые никак с друг другом не связаны"), интерпретатор ищет соответствующие атрибуты сначала в локальном пространстве имен, а потом в свойствах класса, если не находит на предыдущем шаге. ИМенно эта особенность позволяет иметь множество обьектов с похожими или одинаковыми свойствами, но с разными значениями

# ### _**Video 4**_

class Person:
    def hello():
        print("hello")


Person.hello

p = Person()

p.hello

hex(id(p))

Person.hello()

p.hello()

type(p.hello)

type(Person.hello)

# Оказывается, функции и методы - разные классы

id(p.hello)

id(Person.hello)

dir(Person.hello)

dir(p.hello)

p.__dict__

'person-dimon'.split('-')

'dimon'.split('-')

Person.hello(p)

p.hello.__self__

hex(id(p))

p.hello.__func__


class Person:
    def hello(instance):
        print(instance)


p = Person()

p.hello()

hex(id(p))


class Person:
    def hello(self):
        print(self)
    # Это пока еще функция, которая просто учитывает, что ее будут вызывать из экземпляра (то есть пока не метод), методом она станет, когда будет создан экземпляр класса и эта функция будет с этим экземпляром связана


# Пространство имен класса и пространство имен экземпляра полностью изолированы, мы  должны помнить, что класс не имеет доступа к пространству имен экземпляра, поэтому нужно передавать ссылку self, то есть сам экземпляр класса

# ### --*Video 5*--

class Person:
    pass


p = Person()

p.name = 'Ivan'

p.name


class Person():
    def create(self):
        self.name = 'Ivan'
    def display(self):
        print(self.name)
    


p = Person()

p.create()

p.display()

p.__dict__


class Person():
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)


p = Person('Sosiska')

p.name

p.__dict__
