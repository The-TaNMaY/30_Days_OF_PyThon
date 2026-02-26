# Day 2 of 30 Days of Python Programming
# Excercise 1
first_name = "Tanmay"
last_name = "Barman"
full_name = "Tanmay Barman"
country = "India"
city = "Siliguri"
age = 30
year = 2003
is_married = "Single"
is_true = False
is_light_on = True
name , age , year = "Uday", 2020, 2003

# Exercise 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(name))
print(type(age))
print(type(year))

# Exercise 3
print(len(first_name))

a = "Tanmay"
b = "Barman"
if len(a) > len(b):
    print("a has more chareter then ")
else :
    print("both has equal number of charecter")   

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_two - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

import math
r = 30
area_of_circle = math.pi  * r**2
print(area_of_circle)
circum_of_circle = 2 * math.pi * r
print(circum_of_circle)

radius = int(input("Enter Radius of Circle : "))
area_of_user = math.pi * radius**2
print(area_of_user)

user_fname=input("Enter Your First Name: ")
user_lname=input("Enter Your Last Name: ")
user_country=input("Enter Your Country : ")
user_age=input("Enter Your Age: ")
print(user_fname,user_lname,user_country,user_age)

