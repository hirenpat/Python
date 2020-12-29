import modules as mod  # from other file

# All of the following modules are from STD
import random as rand
import math as math
import datetime as dt
import calendar as calendar

import os

courses = ['History', 'Math', 'Physics', 'Eecs', 'Art']

index = mod.find_index(courses, 'Eecs')
print(index)

random_course = rand.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today = dt.date.today()
print(today)
print(calendar.isleap(2017))

print(os.__file__)
