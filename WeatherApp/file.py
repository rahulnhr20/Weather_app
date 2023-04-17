# Python code to demonstrate working of
# Bitwise OR among List elements
# Using reduce() + lambda + "|" operator

# initializing list
# test_list = [7, 8, 9, 1, 10, 7]
#
# # printing original list
# print("The original list is : " + str(test_list))
#
# # Bitwise OR among List elements
# # Using reduce() + lambda + "|" operator
# res = reduce(lambda x, y: x | y, test_list)
#
# # printing result
# print("The Bitwise OR of list elements are : " + str(res))

# Python code to demonstrate working of
# Bitwise OR among List elements
# Using reduce() + operator.ior
# from operator import ior
# import functools
# # initializing list
# test_list = [1,2,1]
#
# # printing original list
# print("The original list is : " + str(test_list))
#
# # Bitwise OR among List elements
# # Using reduce() + operator.ior
# res = functools.reduce(ior, test_list)
#
# # printing result
# print("The Bitwise OR of list elements are : " + str(res))

# cook your dish here
# import math

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    # print(math.gcd(n, m))

    if(n%2==0 and m%2!=0):
        print(1)
    elif(n%2!=0 and m%2!=0):
        print(1)
    elif(n%2!=0 and m%2==0):
        if(m%n==0):
            print(n)
        else:
            print(1)
    else:
        v = abs(n-m)
        # k = v//2
        ans = min(n,v)
        print(ans)
