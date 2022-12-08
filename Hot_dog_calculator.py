# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:04:42 2022

@author: oymg81
"""

# 8. Hot Dog Cookout Calculator
# 
# Assume hot dogs come in packages of 10, and hot dog 
# buns come in packages of 8. Write a program that 
# calculates the number of packages of hot dogs and 
# the number of packages of hot dog buns needed for a 
# cookout, with the minimum amount of leftovers. The 
# program should ask the user for the number of people 
# attending the cookout and the number of hot dogs each 
# person will be given. The program should display the 
# following details:
# 
# • The minimum number of packages of hot dogs required
# • The minimum number of packages of hot dog buns required
# • The number of hot dogs that will be left over
# • The number of hot dog buns that will be left over
############
import math
number_of_people = int(input("Enter number of people: "))
number_of_hotdogs_per_person = int(input("Enter number of hot dogs: "))

num_hd_pk = 10
num_buns_pk = 8

# number of hotdog for the event
total_number_of_hotdogs = number_of_people * number_of_hotdogs_per_person

# Number hotdog pack required

num_hotdog_packages_needed = math.ceil(total_number_of_hotdogs / 10)
num_hotdog_buns_needed = math.ceil(total_number_of_hotdogs/8)
num_hotdogs_left_over = (num_hotdog_packages_needed * num_hd_pk)- total_number_of_hotdogs 
num_hotdog_buns_left_over = (num_hotdog_buns_needed * num_buns_pk)- total_number_of_hotdogs

print("Minimum number of packages of hot dogs required =", num_hotdog_packages_needed)
print("Minimum number of packages of hot dog buns required =", num_hotdog_buns_needed)
print("Number of hot dogs left over =", ( num_hotdogs_left_over))
print("Number of hot dogs buns left over =", (num_hotdog_buns_left_over))