# # # Case1: Class in its simplest form
# class Human:
#     eye = 2
#     ear = 2
#     hand = 2
#     leg = 2
#
# man = Human()
# print(man.eye)
# print(man.ear)
# print(man.hand)
# print(man.leg)

# # # Case2: Class with constructor
# class Person:
#     def __init__(self, name, age):
#         self.its_name = name
#         self.its_age = age
#
#
# p1 = Person("Kevin", 30)
#
# print(p1.its_name)
# print(p1.its_age)

# # # Case3: Class with constructor and a Method(This method which is inside a class is called as a Function)
# class Person:
#     def __init__(self, name, age):
#         self.its_name = name
#         self.its_age = age
#
#     def myfunct(self):
#         print("My name is = ", self.its_name)
#         print("My age is = ", self.its_age)
# p1 = Person("Kevin",30)
# print(p1.its_name)
# print(p1.its_age)
# p1.myfunct()

# # # Case4: Modify or Delete the Object properties outside the class
# # Case4.1 : Changing the value
# class Person:
#     def __init__(self, name, age):
#         self.its_name = name
#         self.its_age = age
#
#     def myfunct(self):
#         print("My name is = ", self.its_name)
#         print("My age is = ", self.its_age)
# p1 = Person("Kevin",30)
# p1.its_name = "Kevin Jose"
# p1.myfunct()


# # # Case4.1 : Deleting the value
# class Person:
#     def __init__(self, name, age):
#         self.its_name = name
#         self.its_age = age
#
#     def myfunct(self):
#         print("My name is = ", self.its_name)
#         print("My age is = ", self.its_age)
# p1 = Person("Kevin",30)
# del p1.its_age
# p1.myfunct()


# # # Case 5 : Inheritance
# # Case5.1: (Child class without any properties --> We use pass keyword)
# class Person:
#   def __init__(self, fname, lname):
#     self.first_name = fname
#     self.last_name = lname
#
#   def print_name(self):
#     print(self.first_name, self.last_name)
#
# class Student(Person):
#   pass
#
#
# p1 = Person("Kevin", "Jose")
# p1.print_name()
#
# s1 = Student("Suresh", "Rao")
# s1.print_name()


# # Case5.2: (Child class with properties -->  We use __init__ () in the child class)

# class Person:
#     def __init__(self, fname, lname):
#         self.first_name = fname
#         self.last_name = lname
#
#     def print_name(self):
#         print(self.first_name, self.last_name)
#
#
# class Student(Person):
#     def __init__(self, first_name, last_name,year):
#         Person.__init__(self,first_name,last_name)
#         self.graduation_year = year
#
#     def welcome(self):
#         print("Welcome", self.first_name, self.last_name, "to the class of", self.graduation_year)
#
# p1 = Person("Kevin", "Jose")
# p1.print_name()
#
# s1 = Student("Suresh","Rao",2011)
# s1.print_name()
# s1.welcome()

