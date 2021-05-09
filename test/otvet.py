         # Наследование


class A:
    def AAA(self):
        print("class A. Method AAA()")


class B(A):
    
    def BBB(self):
        
        self.AAA() 
        print("class B. Method BBB()")


class C(B):
    
    def CCC(self):

        self.AAA()
        self.BBB()
        print("class C. Method CCC()")


objA = A()
objA.AAA() 
print("----------------")


         # Инкапсуляция

class Phone:
    number = "0773 410 413"
    def print_number(self):
        print( "Phone number is: ", self.number )

my_phone = Phone()
my_phone.print_number()

input( "Press Enter to exit" )

         # Полифоризм

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

         # Абстракция

from abc import ABC, abstractmethod
 
 
class Basic(ABC):
    @abstractmethod
    def hello(self):
        print("Hello from Basic class")
 
 
class Advanced(Basic):
    def hello(self):
        super().hello()
        print("Enriched functionality")
 
a = Advanced()
a.hello()


         # Композиция

class Room:
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []
    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))
    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square
 
r1 = Room(6, 3, 2.7) 
print(r1.square)
r1.addWD(1, 1) 
r1.addWD(1, 1)
r1.addWD(1, 2)
print(r1.workSurface()) 

         # Итератор

l = [1,2,3,5,8,11]
i = iter(l)
print(i) 

         # Генератор

a = (i**2 for i in range(1,5))
for i in a:
    print(i)

         # Метаклассы

class ObjectCreator(object):
    pass


my_object = ObjectCreator()
print(my_object)



         # Миксины

class GraphicalEntity:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y

class Button(GraphicalEntity):
    def __init__(self, pos_x, pos_y, size_x, size_y):
        super().__init__(pos_x, pos_y, size_x, size_y)
        self.status = False

    def toggle(self):
        self.status = not self.status

b = Button(10, 20, 200, 100)

         # Как создавать экземпляры класса 

class Employee:  
    """Базовый класс для всех сотрудников"""  
    emp_count = 0  
  
    def __init__(self, name, salary):  
        self.name = name  
        self.salary = salary  
        Employee.emp_count += 1  
  
    def display_count(self):  
        print('Всего сотрудников: %d' % Employee.emp_count)
        
    def display_employee(self):  
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))  
  
  

emp1 = Employee("Андрей", 2000)  

emp2 = Employee("Мария", 5000)  
emp1.display_employee()  
emp2.display_employee()  
print("Всего сотрудников: %d" % Employee.emp_count)