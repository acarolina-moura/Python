# 1 - Define the function to accept one input parameter called nums
# 2 - Initialize a counter to 0
# 3 - Loop through every number in nums
# 4 - Within the loop, if any of the numbers are divisible by 10, increment our counter
# 5 - Return the final counter value

# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.

# Option 1
num = [30, 45, 25, 40, 12, 77, 4, 50]

def divisible_by_ten(num):
    counter = 0
    for nums in num:
        if nums % 10 == 0:
            counter += 1
            print (nums)
    return counter

print(divisible_by_ten(num))

# Option 2
def divisible_by_ten(num):
    counter = 0
    for nums in num:
        if nums % 10 == 0:
            counter += 1
            print (nums)
    return counter

print(divisible_by_ten([20, 25, 30, 35, 40]))