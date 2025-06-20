# ---------------------------
# ---retirement_calculator---
# ---------------------------

name = input("Enter your name: ")
name = name.title()
age = int(input("Enter your age: "))
retirement_age = 60
years_left = retirement_age - age

print("Hello " , name)
print("You have" , years_left , "years left to retire.")