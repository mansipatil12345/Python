#square
# i=1
# while i<=3:
#     j=1
#     while j<=3:
#         print('*',end=" ")
#         j+=1
#     i+=1
#     print()


#squre with 1,1,1
#           2,2,2
#...........
# i=1
# while i<=3:
#     j=1
#     while j<=3:
#         print(i,end=" ")
#         j+=1
#     i+=1
#     print()


#squre with 1,2,3
#           1,2,3
#...........
# i=1
# while i<=3:
#     j=1
#     while j<=3:
#         print(j,end=" ")
#         j+=1
#     i+=1
#     print()


#p4
# 1 2 3 
# 4 5 6 
# 7 8 9 
# i=1
# k=1
# while i<=3:
#     j=1
#     while j<=3:
#         print(k,end=" ")
#         j+=1
#         k+=1
#     i+=1
#     print()



# i=1
# k=9
# while i<=3:
#     j=1
#     while j<=3:
#         print(k,end=" ")
#         j+=1
#         k-=1
#     i+=1
#     print()



# i=1
# while i<=3:
#     j=1
#     while j<=3:
#         if i%2==0:
#             print("0",end=" ")
#         else:
#             print("1",end=" ")
#         j+=1
#     i+=1
#     print()


# n=int(input("Enter the no: "))
# i=1
# while i<=n:
#     j=1 
     #(here j<= n must be there not i )
#     while j<=n:    
#         if i%2==0:
#             print("0",end=" ")
#         else:
#             print("1",end=" ")
#         j+=1
#     i+=1
#     print()



# n = int(input("Enter any number: "))  #always better to focus on outer boundary
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         if(i==1 or i==n or j==1 or j==n):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     i+=1
#     print()


'''
1 3 5 
7 9 11 
13 15 17 
'''

# start = int(input("Enter the start value: "))
# end = int(input("Enter the ending value: "))
# n = int(input("Enter the number of rows: "))
# m = int(input("Enter the number of cols: "))
# i=1
# k=start
# while i<=n:
#     j=1
#     while j<=m:
#         if k>end:
#             break
#         else:
#             print(k,end=" ")
#             j+=1
#             k+=2
#     i+=1
#     print()



'''
1 1 1 1 1 
1 1     1 
1   1   1 
1     1 1 
1 1 1 1 1 
'''
# n = int(input("Enter any number: "))  #always better to focus on outer boundary
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         if(i==1 or i==n or j==1 or j==n or i==j):
#             print("1",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     i+=1
#     print()




#hw1
# n = int(input("Enter any number: "))  #always better to focus on outer boundary
# i=1
# mid = n//2+1
# while i<=n:
#     j=1
#     while j<=n:
#         if(i==1 or i==n or j==1 or j==n or (i==mid and j==mid)):
#             print("X",end=" ")
#         else:
#             print("O",end=" ")
#         j+=1
#     i+=1
#     print()



#hw2
# n = int(input("Enter any number: "))  #always better to focus on outer boundary
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         if(i==1 or i==n or j==1 or j==n):
#             print("1",end=" ")
#         else:
#             print(i,end=" ")
#         j+=1
#     i+=1
#     print()


#hw3
# n = int(input("Enter any number: "))  #always better to focus on outer boundary
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         if((i+j)%2==0):
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#         j+=1
#     i+=1
#     print()



'''
*
* *
* * * 
'''
# i=1
# while i<=3:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1

'''
1
3 3
5 5 5

'''

# i=1
# while i<=3:
#     j=1
#     while j<=i:
#         print(2*i-1,end=" ")
#         j+=1
#     print()
#     i+=1

#using for 
# k=1
# for i in range(1,4):
#     for j in range(i):
#         print(k,end=" ")
#     print()
#     k+=2


'''
A 
C C 
E E E 
'''

# k=65
# for i in range(1,4):
#     for j in range(i):
#         print(chr(k),end=" ")
#     print()
#     k+=2



    

'''
a 
a b 
a b c 
'''

# for i in range(1,4):
#     k=97
#     for j in range(i):
#         print(chr(k),end=" ")
#         k+=1
#     print()



'''                (imp)
* * * 
  * * 
    * 
'''
# n = 3
# for i in range(n,0,-1):
#     for k in range(n-i):
#         print(" ",end=" ")

#     for j in range(i):
#         print("*",end=" ")
#     print()


'''
    * 
  * * 
* * * 
'''

# n = 3
# for i in range(1,n+1):
#     for k in range(n-i):
#         print(" ",end=" ")

#     for j in range(i):
#         print("*",end=" ")
#     print()


'''
* 
* * 
* * * 
* * 
* 
'''

# n=3
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#this logic is also valid(without nested loop as done above)
# n=3
# for i in range(1,n+1):
#     print(" * " * i,end=" ")
#     print()
# for i in range(n-1,0,-1):
#     print(" * " * i,end=" ")
#     print()




# hw1
'''
    * 
  * * * 
* * * * * 
'''
# n=3
# for i in range(1,n+1):
#     for j in range(n-i,0,-1):
#         print(" ",end=" ")
#     for k in range(2*i-1,0,-1):
#         print("*",end=" ")
#     print()

'''
    1 
  3 3 3 
5 5 5 5 5 
'''
# n=3
# count=1
# for i in range(1,4):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print(count,end=" ")
#     print()
#     count+=2

    
        

'''
7 7 7 7 7 
  5 5 5 
    3 
'''
# n=3
# for i in range(3,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print(2*i+1,end=" ")
#     print()
  



'''
    A 
  B B 
C C C 
  B B 
    A 
'''
# n=3
# x=65
# for i in range(1,4):
#     for j in range(n-i,0,-1):
#         print(" ",end=" ")
#     for k in range(i):
#         print(chr(x),end=" ")
#     print()
#     x+=1
# x-=2
# for i in range(n-1,0,-1):
#     for j in range(n-i,0,-1):
#         print(" ",end=" ")
#     for k in range(i):
#         print(chr(x),end=" ")
#     print()
#     x-=1
    


'''
0         0     (imp)
1 1     1 1 
0 0 0 0 0 0 
'''
# n=3
# for i in range(1,n+1):
#     #number
#     for j in range(i):
#         if i%2==0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     #space
#     for k in range(2*n-2*i):
#         print(" ",end=" ")
#     #number
#     for j in range(i):
#         if i%2==0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()



'''
*         * 
* *     * * 
* * * * * * 
* *     * * 
*         * 
'''
# n=3
# for i in range(1,n+1):
#     #number
#     for j in range(i):
#         print("*",end=" ")
#     #space
#     for k in range(2*n-2*i):
#         print(" ",end=" ")
#     #number
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#      #number
#     for j in range(i):
#         print("*",end=" ")
#         #space
#     for k in range(2*n-2*i):
#         print(" ",end=" ")
#         #number
#     for j in range(i):
#         print("*",end=" ")
#     print()
    

'''
    * 
  * * * 
* * * * * 
  * * * 
    * 
'''
# n=3
# for i in range(1,n+1):
#     for j in range(n-i,0,-1):
#         print(" ",end=" ")
#     for k in range(2*i-1,0,-1):
#         print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i,0,-1):
#         print(" ",end=" ")
#     for k in range(2*i-1,0,-1):
#         print("*",end=" ")
#     print()
        
