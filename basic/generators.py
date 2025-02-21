# Generators in python

# Generators yield one result at a time
# They dont store everything at once in the memmory
# yield

# Generators dont hold all the values in the memmory
# They are more memmory efficience


def square(nums):
    for i in nums:
        yield(i * i)

my_nums = square([1, 2, 3, 4, 5, 6])

for num in my_nums:
    print(num)
    
    
    
# Create them as a list comprehension
# Add () instead of [] to make it a generator
my_nums2 = (x*x for x in [1, 2, 3, 4, 5])