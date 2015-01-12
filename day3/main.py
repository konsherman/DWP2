# import math
# import random
# class Employee:
#     company = "fullsail"
#     def __init__(self):#constructor function
#         print "Emp created"
#         self.name = "Larry"
#         self.hour = random.randint(0,10)
#
# employees = []
#
# for i in range(100):
#     employees.append(Employee())
#
# employees[0].name = "Bob"
# employees[1].name = "Jim"
#
# for i in employees:
#     print i.hour

class Car:
    def __init__(self,m):
        print "car created"
        self.door = 0
        self.make = m
        self.model = ""
        self.working = True
        self.auto = True

    def start(self):
        if self.working:
            print "My " + self.make + " is Working"
        else:
            print "Car is not starting"







