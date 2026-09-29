# x = (10,20,30)
# print(x)
# print(x[2])

# for i in range(len(x)):
#     print(x[i])


# two methds
#1.count
#2.index



#1 - 12
# 2 - 14
# 3 - 15
# 4 - 21
# 5 - 25
# 6 - 30

# x=(
#     (12,14,15),
#     (21,25,30)
# )
# k=1
# for i in x:
#     for j in i:
#         print(f"{k} - {j}")
#         k+=1



#tuple of list and list etc...
# x=((10,20),(41,(42,43)),[101,201])
# print(x[2][1])
# print(x[1][0])
# print(x[1][1])
# print(x[1][1][1])


# to print the nested loop as well

# for mainitem in x:
#     for subitem in mainitem:
#         if type(subitem) == tuple:
#             for item in subitem:
#                 print(item)
#         else:
#             print(subitem)


#1 
# x=((10,20),(41,(42,43)),[101,201])
# x[2][0]=205
# for mainitem in x:
#     for subitem in mainitem:
#         if type(subitem) == tuple:
#             for item in subitem:
#                 print(item)
#         else:
#             print(subitem)


#2
# x=((10,20),(41,(42,43)),[101,201])
# x[2][0]=205
# sum=0
# for mainitem in x:
#     if type(mainitem) == list:
#         for item in mainitem:
#             sum+=item
# print(sum)



#3
# x=((10,20),(41,(42,43)),[101,201])
# x[2][0]=205
# mul=1
# for mainitem in x:
#     for subitem in mainitem:
#         if type(subitem) == tuple:
#             for item in subitem:
#                 mul*= item
# print(mul)


#4
#update x[2][0] = 205
#list -> sum
#inside tuple -> mul(42*43)
#remaining el -> 10,20,41_-> sum -> then do sum of digits
# x=((10,20),(41,(42,43)),[101,201])
# x[2][0]=205
# lsum=0
# rsum=0
# mul=1
# for mainitem in x:
#     if type(mainitem)==tuple:
#         for subitem in mainitem:
#             if type(subitem) == tuple:
#                 for item in subitem:
#                     mul*=item
#             else:
#                 rsum+=subitem
#     else:
#         for item in mainitem:
#             lsum+=item   
# print(mul)
# print(rsum)
# print(lsum)
# dsum=0
# while rsum>0:
#     rem = rsum%10
#     dsum+=rem
#     rsum//=10
# print(dsum)




    
        






        





