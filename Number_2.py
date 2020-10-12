import random
n = random.randint(0, 100)
multiply = lambda x : x * n
x = eval(input("Input the number to be multiplied with a random integer(0 to 100): "))
print(multiply(x))
