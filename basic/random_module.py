# Random module in python

import random


# Generate a random number between 0 and 1
value = random.random()
print(value)


# Random integer (inclusive)
random_integer = random.randint(1, 10)
print(random_integer)


# Random choice
# This can get the same element multiple times
colors = ["red", "green", "black", "blue", "white"]
random_color = random.choice(colors)
print(random_color)


# Get 10 random values
# k is the amout of time its going to repeat
# weights is the chances of the color  being picked
random_colors = random.choices(colors, weights=[10, 10, 12, 1, 12], k=10)
print(f"Random colors: {random_colors}")


# Random shuffle
# This is going to randomly shuffle the list
deck = list(range(1, 53))
random.shuffle(deck)

# Random sample
# Get 10 random unique values
random_sample = random.sample(deck, k=10)
print(random_sample)


