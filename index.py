# davaleba 1

print("Let's start the game")

score = 0

# question 1
print("1) In what year was the first iPhone released")
answer1 = input('Enter Your Answer: ')

if answer1 == "2007":
    score += 1
    print('correct! you got 1 point')
else:
    print('incorect')    

# question 2
print("2) How many players are there on a baseball team?")
answer2 = input('Enter Your Answer: ')

if answer2 == "9":
    score += 1
    print('correct! you got 1 point')
else:
    print('incorect')    

# question 3
print("3) How many hearts does an octopus have?")
answer3 = input('Enter Your Answer: ')

if answer3 == "3":
    score += 1
    print('correct! you got 1 point')
else:
    print('incorect')    

print("You got" + str(score) + "/3")    

# davaleba 2

operator = input("Enter an operator (+ - * /)")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not a valid operator!")                


# davaleba 3

print(range(1,100,4))
for i in range(1,100,4):
    print(i)

# davaleba 4

count = 0

while count < 100:
    count = count + 1
    if count % 7 == 0:
        print(f"unashtod ikopa: {count}" )

# davaleba 5

nums = int(input("Pls enter any number: "))

n1, n2 = 0, 1
count = 0

if nums <= 0:
   print("Please enter a positive number")

elif nums == 1:
   print("Fibonacci sequence upto",nums,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nums:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

# davaleba 6

for i in range(-10,0):
    print(i)

# davaleba 7    

n = int(input("Enter any Number: "))
reverse = 0
while n > 0:
    r = n % 10
    reverse = (reverse * 10) + r
    n //= 10
print("Reverse is: ",reverse)    