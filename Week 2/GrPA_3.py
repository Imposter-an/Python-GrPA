# part 1 - If pattern
word = "glow" # str
continuous_tense = True # bool

# part 2
age = 5 # int
is_member = True # bool

# part 3

color_code = "R" # str: valid values are R-red, G-green and B-blue

time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

# <eoi>

# part 1 - basic if

new_word = word  # donot remove this line

# remove the "ing" suffix from `new_word` if it is there
if new_word.endswith("ing"):
    new_word = new_word[:-3]

# add the suffix "ing" to `new_word` if `continuous_tense` is True
# write the whole if else block here
if continuous_tense:
    new_word = new_word + "ing"
else:
    new_word = new_word

# part 2 - If else pattern

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if age >= 18:
    age_group = "Adult"
else:
    age_group = "Child"

# applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
# write the whole if else block
if is_member:
    if age >= 18:
        applicant_type="Adult Member"
    else:
        applicant_type="Child Member"
else:
    if age >= 18:
        applicant_type="Adult Non-member"
    else:
        applicant_type="Child Non-member"

# part 3 if ... elif .. else

# based on the value of `color_code` assign the `color` value in lower case and "black" if `color_code` is none of R, B and G

if color_code == "R":
    color = "red"
elif color_code == "B":
    color = "blue"
elif color_code == "G":
    color = "green"
else:
    color = "black"



is_time_valid=int(time[:2])>=1 and int(time[:2])<=12
# bool: True if time is valid (should be ranging from 1 - 12 both including) else False 

# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
time_in_hrs = int(time[:2])%12 + (time[-2:] == "PM")*12


# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range

# write your code here


if not is_time_valid:
    time_of_day="Invalid"
elif time_in_hrs>=6 and time_in_hrs<12:
    time_of_day="Morning"

elif time_in_hrs>=12 and time_in_hrs<18:
    time_of_day="Afternoon"

elif time_in_hrs>=18 and time_in_hrs<24:
    time_of_day="Evening"

elif time_in_hrs>=0 and time_in_hrs<6:
    time_of_day="Night"