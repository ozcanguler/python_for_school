import random
import my_module
# Generates a random number between
# a given positive range
r1 = random.randint(1, 11)
print("Random number between 1 and 11 is % s" % (r1))
print(my_module.pi)

random_float=random.random()
print(random_float)

print(random_float*5)


r2 = random.uniform(0,5)
print(r2)