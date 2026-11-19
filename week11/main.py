# #２
# from math import pow
# class Sphere:
#     def __init__(self, r):
#         self.rad = r

#     def volume(self):
#         result = (4 * 3.14 * pow(self.rad, 3)) / 3
#         return round(result, 2)

#     def surface_area(self):
#         ans = 4 * 3.14 * pow(self.rad, 2)
#         return ans
    
#     def __str__(self):
#         pass


# s = Sphere(2)

# print(s.volume())
# print(s.surface_area())



# # 3
# from math import pow, gcd, lcm
# class Calculator:
#     def __init__(self, a, b):
#         self.n1 = a
#         self.n2 = b

#     def add(self):
#         return self.n1 + self.n2 
    
#     def gcd(self):
#         return gcd(self.n1 , self.n2)
    
#     def lcm(self):
#         return lcm(self.n1 , self.n2)
#     def power(self):
#         return round(pow(self.n1, self.n2))


# c = Calculator(2, 10)
# print(c.add())
# print(c.gcd())
# print(c.lcm())
# print(c.power())



# # 4
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def green(self):
#         print(f"My name is {self.name} , {self.age} year olds")

# p = Person("WangMin", 20)
# p.green()



# # 7 
# class Employee:
#     company = "Unknown"
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_info(self):
#         print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company}")

    
# Employee.company = "TechCorp"

# emp1 = Employee("Alice", 50000)
# emp2 = Employee("Bob", 60000)

# emp1.display_info()
# emp2.display_info()


# 8 

# class Temperature:
    
#     def __init__(self, fahrenheit):
#         self.fahrenheit = fahrenheit

#     @classmethod
#     def from_celsius(cls, temp):
#         fahrenheit = temp * (9/5) + 32
#         return cls(fahrenheit)
        
        

# temp = Temperature.from_celsius(25)
# print(temp.fahrenheit)

    
# # 9
# class Student:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

#     """
#     Becuase count is only can see or edit Admin level, 
#     it can't be edit or view attribute.
#     """

#     @classmethod
#     def get_student_count(cls):
#         return Student.count
    
# s1 = Student("Alice")
# s2 = Student("Bob")
# s3 = Student("Charlie")

# print(Student.get_student_count())
    

# # 12
# class Factor:
#     factor_list = [2, 3, 6, 8]

#     def __init__(self, num):
#         print("Original factor_list: ", Factor.factor_list)
#         self.num = num

#     def find_factors(self):
#         return [i for i in Factor.factor_list if self.num % i == 0]
    
#     @staticmethod
#     def add_factors(lst):
#         for i in lst:
#             Factor.factor_list.append(i)
    
#     @staticmethod
#     def show_factor_list():
#         print ([i for i in Factor.factor_list])  

#     @staticmethod
#     def remove_factor(lst):
#         for i in lst:
#             Factor.factor_list.remove(i)
    
#     @staticmethod
#     def isfactor(num, n):
#         return True if num % n == 0 else False 
      
# f = Factor(12)
# print(f.find_factors())
# Factor.add_factors([4, 6, 9])
# Factor.show_factor_list()
# Factor.remove_factor([3, 8])
# Factor.show_factor_list()
# print(Factor.isfactor(15, 3))
# print(Factor.isfactor(15, 4))





# # 14
# import math
# class Shape:

#     def __init__(self):
#         pass

#     def area(self):
#         pass

# class Rectangle(Shape): 
#     def __init__(self, lenght, width):
#         super().__init__()
#         self.lenght = lenght
#         self.width = width
#     def area(self):
#         super().area()
#         return self.lenght * self.width

# class Circle(Shape):

#     def __init__(self, radius):
#         super().__init__()
#         self.r = radius

#     def area(self):
#         super().area()
#         return  round(math.pi * (self.r ** 2), 2)
        
    
# rect = Rectangle(4, 5)
# circle = Circle(3)

# print(rect.area())
# print(circle.area())

# # 16
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def print_name(self):
#         print("Name: ", self.name)

# class Student(Person):
#     def __init__(self, name, gender):
#         super().__init__(name)
#         self.gender = gender

#     def print_info(self):
#         print(self.name, self.gender)

# student = Student("Bob", "Male")
# student.print_info()

# # 18
# class Year:
#     def __init__(self, year):
#         self.__year = year

#     # getter
#     @property
#     def year(self):
#         return(self.__year)
    
#     # setter
#     @year.setter
#     def year(self, y):
#         self.__year = y

#     def isleap(cls):
#         return (cls.year % 4 == 0 and cls.year % 100 !=0) or (cls.year % 400 == 0)


# y = Year(2024)
# print(y.isleap())
# print(y.year)
# y.year = 2023
# print(y.isleap())


# 19

class Rectangle:
    def __init__(self, width, height):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, w):
        if w <= 0:
            self.__width = 0
        else:
            self.__width = w
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        if h <= 0:
            self.__height = 0
        else:
            self.__height = h

    @property
    def area(self):
        return self.__width * self.__height
    
rect = Rectangle(5, 10)
print(rect.area)
rect.width = -3
rect.height = -2
print(rect.area)