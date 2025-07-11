import random

numbers = list(range(1, 10))
random.shuffle(numbers)
print("Shuffled numbers:", numbers)
print("Random number from 1–100:", random.randint(1, 100))
