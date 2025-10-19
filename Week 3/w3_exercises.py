## WEEK 3 EXERCISES
# TIP: When focussing on just one exercise, comment out the other exercises
# TIP: Block comment by highlighting a section, then hit ctrl/cmd + /

# Exercise 1: Grades
# From an input, print out the associated grade from a given score

score = int(input("Enter your score: "))

# BONUS Exercise (if already familiar with Python): Bank Account v2
# Write a program that lets a user withdraw or deposit funds into their bank account.
# • The bank account should start with a default of $0.
# • The user should be able to indicate how many withdraw/deposit transactions they would
#   like to make.
# • Each transaction that is successful you should print the withdraw/deposit success and
#   display the new balance.
# • A transaction will fail if:
#   o The deposit is above the daily limit of $1000
#   o The withdrawal would leave the account with less than $0
# • If a transaction fails, inform the user.
# • If the user enters an invalid transaction type, inform the user.
# • Failed transactions and invalid transaction types will still count towards their total
#   transactions made.
# • After all transactions have finished, print the final balance.

# The following is last week's implementation of the bank account system:

print("Bank Account Simulator")
balance = 1000
transaction = input("Enter 'deposit' or 'withdraw': ").lower()
amount = int(input("Enter amount: "))

if transaction == "deposit":
    balance += amount
    print("Deposit successful! New balance:", balance)
elif transaction == "withdraw":
    if balance <= amount:
        balance -= amount
        print("Withdrawal successful! New balance:", balance)
    else:
        print("Insufficient funds.")
else:
    print("Invalid transaction type.")

# Exercise 2: Pattern Printing
# The program below should print out the following pattern:
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *
# However, there are some bugs in the code. You should be able to find and fix at
# least 3 bugs (and maybe find one that looks like a bug, but isn’t!)

rows = 5
for i in range(0, rows-1):
    for j in range(0, i):
        print("*")
    print()

for j in range(rows, 0, -1):
    for i in range(0, j - 1):
        print("*")
    print()

# BONUS Exercise (if already familiar with Python): Fizzbuzz
# Print numbers 1–30
# If divisible by 3 → “Fizz”
# If divisible by 5 → “Buzz”
# If divisible by both → “FizzBuzz”