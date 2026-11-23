1 #Voting Eligibility:

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

2 #Largest number:

 numbers = [10, 25, 5, 40, 15]

largest = max(numbers)

print("Largest number:", largest)

3 #Employee Bonus Calculation:

salary = float(input("Enter salary: "))

if salary > 50000:
    bonus = salary * 0.10
else:
    bonus = 0

print("Bonus:", bonus)

4 # Even or Odd Number

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

5 # Reverse a Word or Sentence

text = input("Enter a word: ")

reverse = text[::-1]

print("Reversed:", reverse)   

6 #Student Pass or Fail

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

7 #Calculate Discount

amount = float(input("Enter total amount: "))

if amount > 100:
    discount = amount * 0.20
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final amount:", final_amount)

8 #Bank Withdrawal – Check Balance

balance = 5000

amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")

9 #Leap Year or Not

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

10 # Extract Even Numbers from a List

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)
