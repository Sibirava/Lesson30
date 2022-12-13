#raise Exception("sdfsdgsgs")
from student import *

s = Student(20)
# print(s.get_age())
#
# s.set_age(-30)
# print(s.get_age())


while True:
    try:
        age = int(input("Input students age:"))
        s.set_age(age)
    except StudentAgeWrongError:
        print("exc")
        break

    print(s.get_age())
