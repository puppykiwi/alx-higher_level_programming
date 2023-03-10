#!/usr/bin/python3
'''creating a student class'''


class Student:
    '''defines a student class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns a dict'''
        if attrs is None:
            return self.__dict__
        else:
            mdict = {}
            for i in attrs:
                if hasattr(self, i):
                    mdict[i] = self.__dict__[i]
            return mdict


if __name__ == "__main__":

    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['last_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
