## WEEK 2 EXERCISES
# TIP: When focussing on just one exercise, comment out the other exercises
# TIP: Block comment by highlighting a section, then hit ctrl/cmd + /

# 1. PROGRAMS
# Exercise 1: Fix the errors
print("Hello World"
Print("this line has wrong case")

# Exercise 2: Correct indentation
if True:
print("This needs fixing")

# Exercise 3: Predict the output
x = 5
X = 10
print(x)
print(X)

# BONUS Exercise (if already familiar with Python): Discount Calculator
# Apply a 20% discount if total price is $100 or more, 10% if between $50–$100, otherwise no discount.
# Rearrange the following lines into an executable program

if total > 100:
if total >= 100:
elif total < 99:
elif total >= 50:
elif total > 50 and total < 99:
else:
discount = 0.10
discount = 0.20
discount = 0.0
total = float(input("Enter the total price: "))
final_price = total - (total * discount)
print("Final price:", final_price)

# 2. VARIABLES
# Exercise 1: Declare variables
age = ___      # integer
price = ___    # float
name = ___     # string
is_active = ___ # boolean

# Exercise 2: Reassign variable type and print
# REASSIGN HERE
print(age)
print(price)
print(name)
print(is_active)

# BONUS Exercise (if already familiar with Python): Write a program that store product details, update stock, and generate a formatted report.

# 3. EXPRESSIONS & ASSIGNMENT
# Exercise 1: Writing expressions
x = 4
y = 2
# Write an expression that adds x and y, multiplies by 3, and stores in result
result = ___
print(result)

# Exercise 2: Without changing numbers, only operators, parentheses etc., how many numbers can be calculated?
value1 = 10 + 2 * 5
print(value1)
# assign value 2, 3, etc.

# BONUS Exercise (if already familiar with Python): Simple Bank Account

print("Bank Account Simulator")
balance = 1000
transaction = input("Enter 'deposit' or 'withdraw': ").lower()
amount = # FILL IN HERE #

if transaction == "deposit":
    # FILL IN HERE #
    print("Deposit successful! New balance:", balance)
elif # FILL IN HERE #
    if # FILL IN HERE #
        # FILL IN HERE #
        print("Withdrawal successful! New balance:", balance)
    else:
        print("Insufficient funds.")
else:
    print("Invalid transaction type.")

# 4. NOTIONAL MACHINE
# Exercise 1: Trace code
x = 10
y = 5
x = x + y
y = x - y
x = x - y
print(x, y) 

# Exercise 2: What is the output?
a = 5
b = a + 3
a = b - 2
c = a + b
a = c - 1
c = a + b
print(a, b, c)

# BONUS Exercise (if already familiar with Python): Predict final values of x, y, and total without running the code. Then run it to check.

x = 1
y = 2
total = 0

for i in range(1, 4):      
    x = x + i
    for j in range(i):
        y = y + j
        if (x + y) % 2 == 0:
            total += x
        else:
            total -= y

print(x, y, total)

# 5. Navigating CSVs
# Import Data


# Calculate key representative statistics


# Filter and calculate


# Let's do it in Excel