# check number is even from 0-10
# i=0
# while i<10:
#     if i%2==0:
#         print(f"{i} is Even")
#     i+=1

# sum from 11 to 20
# sum = 0
# i=11
# while i<=20:
#     sum+=i
#     i+=1
# print("Sum is : ",sum)


# Even sum and odd sum and count
# i=21
# count=0
# evensum=0
# oddsum=0
# while i<=30:
#     if i%2==0:
#         evensum+=i
#     else:
#         oddsum+=i
#     i+=1
#     count+=1
# print("Even sum is: ",evensum)
# print("Odd sum is: ",oddsum)
# print("Total count is: ",count)


# Print the reverse numbers from 10 to 1
# i=10
# while i>=1:
#     print(i)
#     i-=1

# table
# n = int(input("Enter the number for which you want to print the table: "))
# i=1
# while i<=10:
#     print(f"{n} X {i} = {i*n}")
#     i+=1


#give the vcount and ccount in lowercase alphabets(imp)
# i=97
# vcount=0
# ccount=0
# while i<=122:
#     char = chr(i)
#     if char in 'aeiou':
#         vcount+=1
#     else:
#         ccount+=1
#     print(char,end=" ")
#     i+=1
# print()
# print(vcount,ccount)



# start = int(input("Enter the value of start: "))
# end = int(input("Enter the value of end: "))
# while start<=end:
#     print(f"{start},{start*start},{start*start*start}")
#     start+=1


# 1.print alphabets from uppercase a to z
# 2.print even char print
# 3.even sum and odd sum and count start and end from user op -> sum, count , even count, odd count


# 1.
# a = 65
# z = 90
# while(a<=z):
#     print(chr(a),end=" ")
#     a+=1


# 2.
# a = 65
# z = 122
# while(a<=z):
#     if a%2==0:
#         print(chr(a),end=" ")
#     a+=1


# 3.
# i = 0
# evensum=0
# oddsum=0
# evencount=0
# oddcount=0
# while(i<=100):
#     if i%2==0:
#         evensum+=i
#         evencount+=1
#     else:
#         oddsum+=i
#         oddcount+=1
#     i+=1
# print(f"Even sum is {evensum} and its count is {evencount}")
# print(f"Odd sum is {oddsum} and its count is {oddcount}")


# start = int(input("\nEnter the value of start: ")) #start number is odd so increment by 2 wont work
# end = int(input("\nEnter the value of end: "))
# sum = 0
# for start in range(start,end+1,1):
#     if start%2==0:
#         sum+=start
# print(sum)


# while True:
#     choice= int(input("1.add\n2.sub\n3.mul\n4.div\n5.exit\nEnter your choice: "))
#     match choice:
#         case 1: print("addition")
#         case 2: print("substraction")
#         case 3: print("multiplication")
#         case 4: print("division")
#         case 5:
#             print("Thankyou!")
#             break
#         case _:
#             print("Invalid Input")


# geoemtric calculator - hw complete this
# while True:
#     choice= int(input("1.A\n2.B\n3.exit\nEnter your choice: "))
#     match choice:
#         case 1:
#             while True:
#                 choice1 = int(input("1.P\n2.Q\n3.exit\nEnter your choice: "))
#                 match choice1:
#                     case 1:print("P")
#                     case 2:print("Q")
#                     case 3:
#                         print("Thankyou!")
#                         break
#                     case _:
#                         print("Invalid Choice!")
#         case 2:
#             while True:
#                 choice1 = int(input("1.X\n2.Y\n3.exit\nEnter your choice: "))
#                 match choice1:
#                     case 1:print("X")
#                     case 2:print("Y")
#                     case 3:
#                         print("Thankyou!")
#                         break
#                     case _:
#                         print("Invalid Choice!")
#         case 3:
#             print("Thankyou!")
#             break
#         case _:
#             print("Invalid input")


# pass parameter means nothing helps to create empty block
# ex for pass  parameter
# case 1:
#     pass -> to create empty block(add in notes)


# i=0
# while i<5:
#     i+=1
#     if i==3:
#         continue
#     print(i)
    


# count number of digits(imp)
# num = int(input("Enter the number: "))
# count = 0
# while num>0:
#     count+=1
#     num//=10  #use floor to get int value
# print(count)


# calculate the sum of digits(imp)
# num = int(input("Enter the number: "))
# sum =0
# while num>0:
#     rem = num%10
#     sum += rem
#     num//=10
# print(sum)


# calculate factors for a number(imp)
# no = 6
# for i in range(1,no+1):
#     if(no%i==0):
#         print(i)


# sum of factors of 7
# no = 7
# sum=0
# for i in range(1 , no+1):
#     if(no%i==0):
#         sum+=i
# print(sum)


# sum of fatorial of every digit in number(imp)
# num = 1234
# sum=0
# while num>0:
#     rem = num%10
#     fact=1
#     for i in range(1,rem+1):
#         fact = fact*i
#     sum+=fact
#     num//=10
# print(sum)


# reverse of a number
# n=123
# rev = 0
# while(n>0):
#     rem = n%10
#     rev = (rev*10)+rem
#     n//=10
# print(rev)


# no is palindrome(imp)
# n=121
# temp=n
# rev = 0
# while(n>0):
#     rem = n%10
#     rev = (rev*10)+rem
#     n//=10
# if(temp==rev):
#     print("Number is palindrome")
# else:
#     print("Number is not a palindrome")


# no is spy or not(imp)
# n = 132
# sum =0
# prod =1
# while n>0:
#     rem = n%10
#     sum+=rem
#     prod*=rem
#     n//=10
# # print(sum)
# # print(prod)
# if(sum==prod):
#     print("Number is spy")
# else:
#     print("Number is not spy")


# Neon number(imp)
# n = 9
# sq = n*n
# sum=0
# while sq>0:
#     rem = sq%10 #store in rem no sq create diff variable
#     sum+=rem
#     sq//=10
# if(n==sum):
#     print("Number is Neon")
# else:
#     print("Number is not Neon")


# perfect number:(addition of factors (excluding itself)==orignal number)
# n =28
# sum=0
# for i in range(1,28):
#     if(n%i==0):
#         sum+=i
# if(sum==n):
#     print("Number is perfect")
# else:
#     print("Number is not perfect")

# n =28
# sum=0
# i=1
# while i<n:
#     if(n%i==0):
#         sum+=i
#     i+=1
# if(sum==n):
#     print("Number is perfect")
# else:
#     print("Number is not perfect")


# while True:
#     choice = int(
#         input(
#             "1.Perfect Number\n2.Palindrome\n3.Factorial\n4.Spy\n5.Neon\n6.Exit\nEnter your choice: "
#         )
#     )
#     match choice:
#         case 1:
#             n = int(input("Enter your Number: "))
#             sum = 0
#             for i in range(1, n):
#                 if n % i == 0:
#                     sum += i
#                     i += 1
#             if sum == n:
#                 print("Number is perfect")
#             else:
#                 print("Number is not perfect")

#         case 2:
#             n = int(input("Enter your Number: "))
#             temp = n
#             rev = 0
#             while n > 0:
#                 rem = n % 10
#                 rev = (rev * 10) + rem
#                 n //= 10
#             if temp == rev:
#                 print("Number is palindrome")
#             else:
#                 print("Number is not a palindrome")

#         case 3:
#             n = int(input("Enter your Number: "))
#             sum = 0
#             fact = 1
#             for i in range(n, 1, -1):
#                 fact = fact * i
#             print(f"factorial is: {fact}")

#         case 4:
#             n = int(input("Enter your Number: "))
#             sum = 0
#             prod = 1
#             while n > 0:
#                 rem = n % 10
#                 sum += rem
#                 prod *= rem
#                 n //= 10
#             if sum == prod:
#                 print("Number is spy")
#             else:
#                 print("Number is not spy")

#         case 5:
#             n = int(input("Enter your Number: "))
#             sq = n * n
#             sum = 0
#             while sq > 0:
#                 rem = sq % 10
#                 sum += rem
#                 sq //= 10
#             if n == sum:
#                 print("Number is Neon")
#             else:
#                 print("Number is not Neon")

#         case 6:
#             print("Thankyou!")
#             break

#         case _:
#             print("Invalid choice!")


