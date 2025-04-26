import sys

# increasing triangle
# def star(n):
#     for j in range(n): # rows
#         for i in range(j+1): # columns
#             print("*", end=" ")
#         print()

# decreasing triangle
# def star(n):
#     for j in range(n): # rows
#         for i in range(j,n): # columns
#             print("*", end=" ")
#         print()

#

# # right sided decreasing triangle
# def star(n):
#     for i in range(n): # rows
#         for j in range(i+1): # columns
#             print(" ", end=" ")
#         for j in range(i,n):
#             print("*", end=" ")
#
#         print()

# # triangle
# def star(n):
#     for i in range(n): # rows 0,1,2
#         for j in range(i,n): # columns (0,3)
#             print(" ", end=" ")
#         for j in range(i):
#             print("*", end=" ")
#         for j in range(i+1):
#             print("*", end=" ")
#
#         print()
#
#
# n=int(sys.argv[1])
# star(n)


# pyramid pattern

def pyramid(level):
    for i in range(level): # 0,1,2
        for j in range(level-i-1): #3-1-1 =2
            print(" ", end="")
        for j in range(i+1): # 0+1 =1, # 0
            print("*", end=" ")
        print()

#
# # level = 3
# # j = 3-0-1 = 2,
# #     3-1-1 = 1,
# #     3-2-1 = 0
# #
#
level = int(input("Enter the no. of levels for the pyramid: "))
pyramid(level)