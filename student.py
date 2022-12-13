from student_exception import StudentAgeWrongError

class Student:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            raise StudentAgeWrongError()   #отличный код !!!!