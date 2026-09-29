## x=[10,20,30]
# print(x)
# print(x[1])
# #update
# x[2]=300
# print(x)


# y=[10,"hiii",90.78,True]
# print(type(x))#to check type
# #for loop to print each value at time
# for i in range(len(y)):
#     print(y[i])

#using methods and functions
#1.Using functions
# x=[20,10,30]
# print(len(x),max(x),min(x),sum(x),sorted(x))
# print(sorted(x,reverse=True))#for reversing 

#2.Using methods
# x=[]
# print(x)
# x.append(10) #adds value at last of list
# print(x)

# #extend
# x.extend([3,4]) #merges the list
# print(x)

# #copy
# y=x.copy()
# print(y)

# #count
# print(x.count(8))#return the occurrance of value passed

# #insert
# x.insert(1,5) #index at which you want to val
# print(x)

#remove
# x=[20,30,40]
# x.remove(20)
# print(x)

# x.pop()
# print(x)

# x.clear()
# print(x)


#find len of list
#count the presence of el
#find max in list
#calculate total of list el
#print duplicate el
#remove duplicate el
#print unique el of list
#create a list by taking user input
#remove el from list without remove method


#create a list by taking user input
# x=[]
# size=int(input("Enter the size of the list: "))
# for i in range(size):
#     ip = int(input("Enter the value: "))
#     x.append(ip)
# print(x)


# find len of list
# x=[10,20,30,40]
# len=0
# for i in x:
#     len+=1
# print(len)


#count the presence of el
# x=[10,10,20,30,40,50]
# count=0
# len=0
# for i in x:
#     len+=1
# ip = int(input("Enter the el to find: "))
# for i in range(len):
#     if x[i]==ip:
#         count+=1
# print(count)


#max
# x=[10,10,20,30,40,50]
# len=0
# max=x[0]
# min=x[0]
# for i in x:
#     len+=1

# for i in range(len):
#     if (x[i]>max):
#         max=x[i]
#     if(x[i]<min):
#         min=x[i]
# print(max)
# print(min)


#duplicate
# x=[10,10,20,20,20,30,40,50]
# len=0
# y=[]
# for i in x:
#     len+=1
# for i in range(len):
#     count=1
#     for j in range(i+1,len-i-1):
#         if(x[i]==x[j]):
#             count+=1
#     if(count>1):
#             print("duplicate value is:", x[i])


#unique and remove duplicate element
# x=[10,10,20,20,20,30,40,50]
# res=[]
# for i in x:
#     if i not in res:
#         res.append(i)
# print(res)


#remove el without remove method
# x=[10,20,30,40,5]
# res=[]
# inp = int(input("Enter el to remove: "))
# for i in x:
#     if i != inp:
#         res.append(i);
# print(res)

#do it in list only dont create another res list (check this)
# x=[10,20,30,40,5]
# inp = int(input("Enter el to remove: "))
# for i in x:
#     if i == inp:
#         x[i+1]=x[i]
# print(x)

    

#nested list 
# x=[[101,102,103],[201,202,203],[301,302,303]]
# print(x)
# print(x[1][1])
# x[2][2] = 403
#to print single row
# print(x[1])


#printing inside el
# x=[[101,102,103],[201,202,203],[301,302,303]]
# #only sublist 
# # for i in x:
# #     print(i) 

# for i in x:
#     for j in i:
#         print(j,end=" ")
#     print()


#sum of el 
# x=[[101,102,103],[201,202,203],[301,302,303]]
# sum=0
# for i in x:
#     for j in i:
#         sum+=j
# print(sum)


# divisible by 5
# x=[[101,102,103],[201,205,203],[301,302,305]]
# sum=0
# found=0
# for i in x:
#     for j in i:
#         if(j%5==0):
#             print(j,end=" ")
#             found=1
# if(found==1):
#     print("found")
# else:
#     print("Not found")


#count
# x=[[101,102,103],[201,202,203],[301,302,303]]
# floor = 0
# sum=0
# for i in x:
#     count=0
#     for j in i:
#         count+=1
#     floor+=1
#     # print("row count",i,"is",count)
#     print(f"floor {floor} has {count} rooms..")


#hws :
#1 above question (marked on)
#2 rowise sum (print every row print)
#3 colwise sum (- || -)
#4 diagonal sum (2 diagonals)
#5 count sum and print el on odd idx and even idx (even idx-> even sum) and (odd idx -> odd sum) and sum of odd and even (3op)
#6 sum of border el - middle el = val ?



#1 
# x=[[101,102,103],[201,202,203],[301,302,303]]
# for i in x:
#     sum=0
#     for j in i:
#         sum+=j
#     print(f"Sum of row {i} is : {sum}")


#2
# x=[[101,102,103],[201,202,203],[301,302,303]]

# k=0
# for i in range(len(x)):
#     sum=0
#     for j in range(len(x[i])):
#         sum+=x[j][k]
#     k+=1
#     print(f"Sum of col {i} is : {sum}")


#3
# x=[[101,102,103],[201,202,203],[301,302,303]]
# d1=0 
# d2=0
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         if(i==j):
#             d1+=x[i][j]
# # print(f"Sum of  d1 is : {d1}")

# # for i in range(len(x)):
# #     for j in range(len(x[i])):
#         if((i+j)==len(x)-1):
#             d2+=x[i][j]     
# print(f"Sum of  d1 is : {d1}")   
# print(f"Sum of  d2  is : {d2}")


#4
# x=[[101,102,103],[201,202,203],[301,302,303]]
# evensum=0
# oddsum=0
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         if((i+j)%2==0):
#             evensum+=x[i][j]
#         else:
#             oddsum+=x[i][j]
# print(f"Even sum and odd sum for row {i} is: {evensum} and {oddsum}")


#5
# x=[[101,102,103],[201,202,203],[301,302,303]]
# sr=0
# er=len(x)-1 
# sc=0
# ec=len(x[0])-1
# sum=0

# #top
# for j in range(sc,ec+1):
#     sum+=x[sr][j]

# #right
# for i in range(sr+1,er+1):
#     sum+=x[i][ec]

# #bottom
# for j in range(ec-1,sc-1,-1):
#     sum+=x[er][j]

# #left
# for i in range(er-1,sr,-1):
#     sum+=x[i][sc]

# center = x[len(x)//2][len(x)//2]
# val = sum-center 
# print(f"The value is: {val}")


#another logic is this 
# if(i==0 or j==0 or i==len(x)-1 or j==len(x)-1):
#     sum1+=x[i][j]









    

    
    

