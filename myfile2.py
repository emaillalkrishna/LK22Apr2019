# class Human:
#     eye = 2
#     ear = 2
#
# man = Human
# print(man.eye)
# print(man.ear)

# class Person:
#     def __init__(self, fname, lname):
#         self.first_name = fname
#         self.last_name = lname
#
# p1 = Person("Kevin","Jose")
# print(p1.first_name)
# print(p1.last_name)

# class Person:
#     def __init__(self,fname,lname):
#         self.first_name =fname
#         self.last_name =lname
#
#     def print_name(self):
#         print(self.first_name,self.last_name)
#
# p1= Person("Kevin","Jose")
# print(p1.first_name)
# print(p1.last_name)
# p1.print_name()

class Person:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname

    def print_name(self):
        print(self.first_name,self.last_name)

class Student(Person):
    def __init__(self,fname,lname,year):
        self.passing_year = year
        Person.__init__(self,fname,lname)

    def print_details(self):
        print(self.first_name,self.last_name,self.passing_year)

try:
    p1 = Person("Kevin", "Jose",2000)
    print(p1.first_name)
    print(p1.last_name)
    p1.print_name()
except:
    print("Error message came ")

finally:
    print("Im`m gone mad")


s1= Student("Suresh","Rao",2011)
print(s1.first_name)
print(s1.last_name)
print(s1.passing_year)

s1.print_name()
s1.print_details()

