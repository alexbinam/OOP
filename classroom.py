# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:41:28 2018

Alexandra Binam
"""

class Students:
    def __init__(self, idx, first, last):
        self.id = idx
        self.first_name = first
        self.last_name = last
        self.assignments = []
    
    def get_full_name(self):
        return(self.first_name + " " + self.last_name)
        
    def get_assignments(self):
        for assn in self.assignments:
            print(assn.name, assn.grade)
    
    def get_assignment(self, name):
        for assn in self.assignments:
            if assn.name == name:
                return(assn)

    
    
    def get_average(self):
        running_sum = 0
        count = 0
        for key in self.assignments:
            running_sum += key.grade
            count += 1
        our_mean = running_sum/count
        return(our_mean)
            
            
    def submit_assignment(self, assignment):
        self.assignments.append(assignment)

    def remove_assignment(self, assignment):
        self.assignments.remove(assignment)

class Assignments:
    def __init__(self, nme, score):
        self.name = nme
        self.max_score = score
        self.grade = None
        
    def assign_grade(self, grade):
        if grade <= self.max_score:
            self.grade = grade
        else:
            self.grade = None
        print(self.grade)
            

    

    