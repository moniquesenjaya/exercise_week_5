add = lambda x : x + 15
multiply = lambda x,y : x * y

x = eval(input("Input a number (tobe added with 15): "))
print(add(x))

z1 = eval(input("Input the first number to be multiplied: "))
z2 = eval(input("Input the second number to be multiplied: "))
print(multiply(z1,z2))
