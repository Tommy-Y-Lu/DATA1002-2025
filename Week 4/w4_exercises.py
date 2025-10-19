## WEEK 4 EXERCISES
# TIP: When focussing on just one exercise, comment out the other exercises
# TIP: Block comment by highlighting a section, then hit ctrl/cmd + /

# Exercise 1: Debugging
# The list below contains a series of numbers. The script should create a list of numbers where each
# number must be greater than the sum of all previous numbers in the original list. Fix the errors! 
# For example, with an original list: [1, 5, 6, 13, 20, 50] 
# The output list would be: 	   	  [1, 5, 13, 50] 

ls = [1, 5, 6, 13, 20, 50]
output_list = []

for i in range(len(ls)):
    if sum(ls[0:i]) < ls[i]:
        output_list.append(ls[i])
print(output_list)

# BONUS Exercise (if already familiar with Python): Code Cracker
# You've received a hidden message
# By using the chr() function, loops, continue, and break
# Skip all numbers less than 50 and all numbers divisible by 7
# Reports have come in however if you go past 999 you will trigger an alert
# Translate the numbers posthaste!

nums = [
    42, 103, 39, 10, 100, 97, 49, 2, 70, 121, 21, 
    84, 693, 13, 33, 999, 116, 111, 111, 102, 97, 114
]

message = ""

# FILL IN HERE!

print("Hidden message:", message)