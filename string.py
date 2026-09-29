# x = "ram"
# print(x)
# print(x[2])
# print('r' in x)
# print('s'in x)

# print(len(x),min(x),max(x))


#method
# x="i like python"
# print(x.upper())
# print(x.lower())
# print(x.title()) #first letter of every word is capitalized 
# print(x.capitalize()) # only first letter or the starting letter is capitalized rest remains small (even upper also changes to small or other than starting letter)
# print(x.swapcase())


# #to remove whitespace
# a ="Maharshtra "
# print(len(a))
# a.strip()  #only removes whitespace (but not stored)  so prev len is printed when output is generated (because white space is counted)
# b=a.strip() #now as the whitespace is removed it is stored in b as the len is stored now it can be printed
# print(len(b))

# a = "Maharashtra world"
# # op = a.split() #splits the whole sentences into words(sperated on basis on white spaces in between)
# #format can be added
# # op = a.split(',') #as no comma is passed in string so whole string is returned in 'Maharashtra world'
# op = a.split('/') #seperated based on '/' so output is ['Maharashtra','world']
# print(op)

# print(a.startswith('M')) #does it starts with 'M' it is case sensitive it treats M and m different - return True or False
# print(a.endswith('o'))   #does it ends with 'o' it is case sensitive    -return True or False                              




# x = "india"
# #op : i n d i a -> idx = 0 1 2 3 4
# for ch in x:
#     print(ch)


#for reverse  
#op: a i d n i a  4 3 2 1 0
# for ch in range(len(x)-1,-1,-1):  # len(x)-> 5 so indx is from 4 so use len(x)-1
#     print(x[ch])





#print even index character , odd ch ka count , vowel character
# x = 'hello'
# count=0
# for i in range(0,len(x)):
#     if(i%2==0):
#         print(x[i],end=" ")
#     else:
#         count+=1
# print()
# print(count)
# for ch in x:
#     if(ch =='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         print(ch,end=" ")

# #or
# for i in range(0,len(x)):
#     if x[i] in 'aeiouAEIOU': #(shorter way)
#         print(x[i])



# str=""
# for i in range(0,5):
#     x = input("Enter five characters: ")
#     str+=x
# print(str)


#len of string 
#count of char present in str
#reverse a string
#palindrome of string 


#1 
# str = 'abc'
# len=0
# for i in str:
#     len+=1
# print(len)


#2
# str ='hello'
# char ='l'
# count=0
# for i in range(0,5):
#     if(str[i]==char):
#         count+=1
# print(count) 


# 3
# str = "hello"
# len=0
# for i in str:
#     len+=1
# rev =""
# for i in range(len-1,-1,-1):
#     rev+=str[i]
# print(rev)


#4
# str = "noon"
# rev =""
# for i in range(len(str)-1,-1,-1):
#     rev+=str[i]
# if(rev==str):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#hw
# maharashtra --> a replace with x 
#anagrams string --> explore 
# count words of string : i like python --> three words are present 
# x = "apple" --> print in sorted way 


#1
# str="Mahrashtra" 
# len=0
# oldstr=""
# for i in str:
#     len+=1
# for i in range(0,len):
#     if(str[i]=='a'):
#         oldstr+='x'
#     else:
#         oldstr+=str[i]
# print(oldstr)


#2,
# str1="race"
# str2="care"
# sortstr1=sorted(str1)
# sortstr2=sorted(str2)
# len1=0
# len2=0
# for i in str1:
#     len1+=1
# for i in str2:
#     len2+=1
# if(len1!=len2):
#     print("Not an Anagram!")
# else:
#     for i in range(0,len1):
#         if(sortstr1[i]!=sortstr2[i]):
#             print("Not an Anagram")
#             break
#     print("Anagram")
               

#4

#3
# str1="count words of string i like python three words are present"
# len=0
# word=1
# for i in str1:
#     len+=1
# for i in range(0,len):
#     if(str1[i]==" "):
#         word+=1
# print(word)


#slicing in notebook'

#reverse using slcing 
# x="hello"
# print(x[ : :-1])

# x="hello"
# print(x.count('l')) #counts the chr (first occ if it is multiple times)
# print(x.find('l'))#return the index of chr
# print(x.find('p')) #it return -1 if not found
# print(x.index('l')) #return the index if not found returns error (substring not found)



#checking method ----> TRUE & FALSE
# x="hi"
# print(x.islower())
# print(x.isupper())
# print(x.isalnum())
# print(x.isalpha())