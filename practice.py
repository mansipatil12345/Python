#number is even
# i=0
# while i<10:
#     if i%2==0:
#         print(i)
#     i+=1


#sum from 11 to 20
# i=11
# sum=0
# while i<=20:
#     sum+=i
#     i+=1
# print(sum)


# i=21
# evensum=0
# oddsum=0
# count=0
# while i<=40:
#     if i%2==0:
#         evensum+=i
#     else:
#         oddsum+=i
#     i+=1
#     count+=1
# print("Even",evensum)
# print("Odd",oddsum)
# print("Count",count)


# i=10
# while i>=1:
#     print(i)
#     i-=1

# n = int(input("Enter the number for which you want to print table: "))
# i=1
# while i<=10:
#     print(f"{n}x{i}={n*i}")
#     i+=1


# i=97
# vcount=0
# ccount=0
# while i<=122:
#     char = chr(i)
#     if char in 'aeiou':
#         vcount+=1
#     else:
#         ccount+=1
#     i+=1
# print(vcount)
# print(ccount)


# start = int(input("Enter the value of start: "))
# end = int(input("Enter the value of end: "))
# while start<=end:
#     print(f"{start} - {start*start} - {start*start*start}")
#     start+=1


# i=97
# while i<=122:
#     print(chr(i))
#     i+=1


# i=97
# while i<=122:
#     if i%2==0:
#         print(chr(i))
#     i+=1


# start = int(input("Enter the starting num: "))
# end = int(input("Enter the ending num: "))
# for i in range(start,end+1):
#     if i%2==0:
#         print(i)
#     i+=1


# while True:
#     choice = int(input("\n1.Add\n2.Sub\n3.Exit\n4.Enter your choice: "))
#     match choice:
#         case 1:print("Addition")
#         case 2:print("Substraction")
#         case 3:
#             print("Exiting the program.....")
#             break
#         case _:
#             print("Invalid!")



#geometric calculator
# while True:
#     print("----------------------------GEOMETRIC CALCULATOR----------------------------------")
#     print("1.Circle")
#     print("2.Triangle")
#     print("3.Rectangle")
#     print("4.Exit")
#     choice = int(input("Enter your choice: "))
#     match choice:
#         case 1:
#             while True:
#                 print("--------------------CIRCLE----------------------------")
#                 choice = int(input("1.Area\n2.Circumference\n3.Exit\nEnter your choice: "))
#                 match choice:
#                             case 1:
#                                 radius = float(input("Enter the radius of the circle: "))
#                                 area = 3.14*radius*radius
#                                 print(f"The area is: {area:.2f}")
#                             case 2:
#                                 radius = float(input("Enter the radius of the circle: "))
#                                 circumference = 2*3.14*radius
#                                 print(f"The area is: {circumference:.2f}")
#                             case 3:
#                                 print("Exiting the program.....")
#                                 break
#                             case _:
#                                 print("Invalid choice!")
#         case 2:
#             while True:
#                 print("--------------------TRIANGLE----------------------------")
#                 choice = int(input("1.Area\n2.Exit\nEnter your choice: "))
#                 match choice:
#                             case 1:
#                                 height = float(input("Enter the height of the triangle: "))
#                                 base = float(input("Enter the base of the triangle: "))
#                                 area = 0.5*height*base
#                                 print(f"The area is: {area:.2f}")
#                             case 2:
#                                 print("Exiting the program.....")
#                                 break
#                             case _:
#                                 print("Invalid choice!")
#         case 3:
#             while True:
#                 print("--------------------RECTANGLE----------------------------")
#                 choice = int(input("1.Area\n2.Perimeter\n3.Exit\nEnter your choice: "))
#                 match choice:
#                             case 1:
#                                 length = float(input("Enter the length of the rectangle: "))
#                                 breadth = float(input("Enter the breadth of the rectangle: "))
#                                 area = length*breadth
#                                 print(f"The area is: {area:.2f}")
#                             case 2:
#                                 length = float(input("Enter the length of the rectangle: "))
#                                 breadth = float(input("Enter the breadth of the rectangle: "))
#                                 circumference = 2*(length+breadth)
#                                 print(f"The area is: {circumference:.2f}")
#                             case 3:
#                                 print("Exiting the program.....")
#                                 break
#                             case _:
#                                 print("Invalid choice!")
#         case 4:
#             print("Exiting the program.....")
#             break
#         case _:
#             ("Invalid choice!")


#String -> starts from 0 collection of unicode character
#1. slicing done
#2. array operations
#3.concatenation
#4.memebership operator -> 'in'
#5.immutability s[0]="H" not allowed 
#6. string comparision "apple"=="apple" allowed -> return boolean value
#7. functions 
#ord(),chr(),len(),input(),print()

#8.methods - done

# codes
# x='india'
# for ch in x:
#     print(ch)
# for ch in range(len(x)-1,-1,-1): (imp)
#     print(x[ch])


# x='india'
# ecount=0
# ocount=0
# for i in range(0,len(x)):
#     if(i%2==0):
#         print(x[i])
#         ecount+=1
#     if(i%2!=0):
#         print(x[i])
#         ocount+=1
# print(ecount)
# print(ocount)


# x='india'(imp)
# for ch in x:
#     if(ch in 'aeiouAEIOU'):
#         print(ch)


# (imp)
# str=""
# for i in range(0,5):
#     str+=input("Enter 5 characters: ")
# print(str)


# str="hello"
# char = 'l'
# count=0
# for ch in str:
#     if(ch==char):
#         count+=1
# print(count)


# (imp)
# str="hello"
# newstr=''
# len=0
# for ch in str:
#     len+=1
# for i in range(len-1,-1,-1):
#     newstr+=str[i]
# print(newstr)


# str="noon"
# rev=''
# len=0
# for ch in str:
#     len+=1
# for i in range(len-1,-1,-1):
#     rev+=str[i]
# if(str==rev):
#     print("palindrome")
# else:
#     print("not palindrome")



# str="maharashtra"
# newstr=''
# for ch in str:
#     if(ch == 'a'):
#         newstr+='x'
#     else:
#         newstr+=ch
# print(newstr)



# (imp)
# str="I like python"
# count=0
# len=0
# for ch in str:
#     len+=1
# for i in range(0,len):
#     if(str[i]!=" "):
#         if i==0 or str[i-1]==" ":
#             count+=1
# print(count)
    


# str1="race"
# str2="care"
# sortstr1 = sorted(str1)
# sortstr2 = sorted(str2)
# len1=0
# len2=0
# for ch in str1:
#     len1+=1
# for ch in str2:
#     len2+=1
# if(len1!=len2):
#     print("NOT ANAGRAM")
# else:
#     flag= True
#     for i in range(0,len1):
#         if(sortstr1[i]!=sortstr2[i]):
#             flag=False
#             break
#     if(flag==True):
#         print("ANAGRAM")
#     else:
#         print("NOT ANAGRAM")

    
#first occurance(imp)
# str = "Hello"
# target ="l"
# for i in range(0,len(str)):
#     if(str[i]==target):
#         print(i)
#         break

#last occurance (imp)
# str ="Hello"
# target ="l"
# pos = -1
# for i in range(len(str)):
#     if(str[i]==target):
#         pos = i
# print(pos)

#LIST



    






