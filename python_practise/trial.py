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

# triangle
def star(n):
    for i in range(n): # rows
        for j in range(i,n): # columns
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")
        for j in range(i+1):
            print("*", end=" ")

        print()


n=int(sys.argv[1])
star(n)


