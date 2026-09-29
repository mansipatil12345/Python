# lambda function or Ananomous function in Python
# sometme we define a function without any Name
# these nameless function called as lambda function
# lambda function are anonymous function in python
# lambda args:expression

# (normal function)
# def function_name(args):
#     expr

# syntax of lambda function:
# lambda args:expression


#normal function 
# def addition(a,b):
#     return a+b
# print(addition(10,20))

#LAMBDA
#lambda function - use to consize the code and instant use
# addition:lambda a,b:a+b
# print(addition(20,30))

# s=lambda x:x**2
# print(s(8))


#WAP to print the square of given list
# l=[1,2,3,4,5,6,7,8,9,10]
#MAP
#map(function,sequence) used to apply functionality on each
#element of sequence and generate new sequence

# def square(n):
#     return n*n
# square = list(map(square,l))
# print(square)

# sq = list(map(lambda n:n**2,l))
# print(sq)



#WAP to convert all list elment into uppercase
# li=["Banana","apple","orange"]

# list = list(map(lambda n:n.upper(),li))
# print(list)


#FILTER
# filter(function,sequence)
#used to filter out the value based on condition

# list = [1,2,3,4,5,6,7,8,9,10]
# even = list(filter(lambda n:n%2==0,list))
# print(even)

#WAP to print the square of even numbers from 1?
# li=[1,2,3,4,5,6,7,8,9,10]
# evenno=list(filter(lambda n:n%2==0,li))
# evenno.insert(0,1)
# even = list(map(lambda n:n**2,evenno))
# print(even)


#WAP to flter out the strings starting with vowels 
# l=["apple","banana","orange"]
# even = list(filter(lambda n:n[0] in 'aeiou',l))
# print(even)


#REDUCE
#returns single value 
# x=1 y=2 x+y = 3, then x= 3,y=3 it continues till end
# from functools import reduce
# l=[1,2,3,4]
# add = reduce(lambda x,y:x+y,l)
# print(add)

# from functools import reduce
# l=[1,2,3,4]
# mul = reduce(lambda x,y:x*y,l)
# print(mul)

# list1=["1","12","13"]
