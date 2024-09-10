import random

numbers = [random.randint(1, 100) for _ in range(10)]

print(numbers)

# Calculate the sum of numbers from 1 to 10
sum = 0
for i in numbers:
  sum += i

 #Calculate the average
average = sum / 10

# Print the average
print(average)

print ("branch by neha")