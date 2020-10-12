from functools import reduce
#The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
fib =  lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
n = eval(input("Enter the number of terms: "))
print(fib(n))
