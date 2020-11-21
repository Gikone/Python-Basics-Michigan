__title__ = "7.14. and 7.15. Exercises"
__author__ = "Diego Gonzalez" 
__credits__ = ["Diego Gonzalez"]
__date__ = "November 2020"
__version__ = "1.0.1" 

""" 
Exercise 1
prefixes = ["J", "K", "L", "M", "N", "Ou", "P", "Qu"]
suffix = "ack"

for p in prefixes:
    print(p + suffix)
"""
"""
Exercise 2
s = input("Enter a string: ")
print s[::-1]
"""


"""
Exercise 3
for amonth in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']:
    print("One of the months of the year is", amonth)
"""

"""
Exercise 4
num = ['12', '10', '32', '3', '66', '17', '42', '99', '20']
for i in num:
    print(i)

"""
#Starts 7.15. exercises

# 1. Write one for loop to print out each character of the string my_str on a separate line.
"""
my_str = "MICHIGAN"
for i in my_str:
    print(i)
"""

# 2. Write one for loop to print out each element of the list several_things. Then, write another 
# for loop to print out the TYPE of each element of the list several_things. To complete this problem
#  you should have written two different for loops, each of which iterates over the list several_things,
#  but each of those 2 for loops should have a different result.
"""
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for s in several_things:
    print(s)
for t in several_things:
    print(type(t))
"""

# 3. Write code that uses iteration to print out the length of each element of the list stored in str_list.

"""
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code here.
for l in str_list:
    print(len(l))

"""

# 4.Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated,
#  but draw something different than we have done in the past. (Hint: if you are drawing something complicated, it could
#  get tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to 
# draw super fast with no animation.)

"""
import turtle
wn = turtle.Screen()
wn.bgcolor("pink")

t = turtle.Turtle()
t.color("Green")
t.speed(15)
t.shape("turtle")
dist = 10
for i in range(100):
    t.forward(dist)
    t.left(30)
    t.stamp()
    t.forward(dist)
    t.right(145)
    t.forward(dist-7)
    dist += 10
"""
# 5. Write code to count the number of characters in original_str using the accumulation pattern and assign the answer to a 
# variable num_chars. Do NOT use the len function to solve the problem (if you use it while you are working on this problem, comment it out afterward!)

"""
original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0
for i in original_str:
    num_chars += 1
"""


# 6. addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the
#  numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).

"""
addition_str = "2+5+10+20"
num = addition_str.split("+")
sum_val = 0
for i in num:
    sum_val += int(i)
print(sum_val)    


"""


# 7. week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the 
# average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number
#  of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).


"""
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
wtf = week_temps_f.split(',')
print(wtf)
avg = 0
for i in wtf:
    avg += float(i)
    print(avg)
avg_temp = avg/len(wtf)
print(avg_temp)
"""
# 8. Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not hard code the list.

"""
nums = range(68)
print(nums)

"""
