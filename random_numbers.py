import random

# Create a list of 100 random numbers from 0 to 1000
numbers = [random.randint(0, 1000) for _ in range(100)]

# Sort the list from min to max (without using sort())
sorted_numbers = []
while numbers:
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    sorted_numbers.append(min_num)
    numbers.remove(min_num)

# Calculate the average for even and odd numbers
sum_even = 0
count_even = 0
sum_odd = 0
count_odd = 0

for num in sorted_numbers:
    if num % 2 == 0:
        sum_even += num
        count_even += 1
    else:
        sum_odd += num
        count_odd += 1

# Print the average results
average_even = sum_even / count_even if count_even > 0 else 0
average_odd = sum_odd / count_odd if count_odd > 0 else 0

print("Average for even numbers:", average_even)
print("Average for odd numbers:", average_odd)