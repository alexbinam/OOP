# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:13:57 2018

Alexandra Binam
"""

from classroom import Students
from classroom import Assignments
 

student_a = Students(123, "Allen", "Allenson")

student_b = Students(456, "Becky", "Beckyson")

a = Assignments('assignment_1', 100)
b = Assignments('assignment_1', 100)
c = Assignments('assignment_2', 100)
d = Assignments('assignment_2', 100)

print('Printing full names and id numbers...')

print(student_a.get_full_name(), student_a.id)
print(student_b.get_full_name(), student_b.id)

print('assigining grades to the assignments...')
a.assign_grade(75)
b.assign_grade(90)
c.assign_grade(85)
d.assign_grade(100)

print('submitting assignments...')
print(student_a.submit_assignment(a))
print(student_a.submit_assignment(c))
print(student_b.submit_assignment(b))
print(student_b.submit_assignment(d))

print('get full names and assignments...')
print(student_a.get_full_name() + " " + str(student_a.get_assignment('assignment_1').name)
+ " " + str(student_a.get_assignment('assignment_1').grade))
print(student_b.get_full_name() + " " + str(student_b.get_assignment('assignment_1').name)
+ " " + str(student_b.get_assignment('assignment_1').grade))

print("get all of becky's assignments...")

print(str(student_a.get_assignments()))

print("Changing Becky's grades and getting the average")
print(student_a.get_average())
print(student_a.remove_assignment(c))
print(student_a.get_average())
