# Basic Assignment
a=10
print(a)
# Tuple Assignment
c,b = (10,19)
print(c)
print(b)

d,e = (10,19,60)
print(d)
print(e)
# error: ValueError: Too many values to unpack

# List Assignment
f,g = [10,19]
print(f)
print(g)

h,i = [10,19,60]
print(h)
print(i)
# error: ValueError: Too many values to unpack

# Sequence Assignment
k,l = 10,19
print(k)
print(l)

s,t = 10,19,60
print(s)
print(t)
# error: ValueError: Too many values to unpack

# Extended sequence assignment
u,v,w = "hai"
print(u) # "h"
print(v) # "a"
print(w) # "i"

x,*y ="python"
print(x) # ["p"]
print(y) # ["y","t","h","o","n"]



# Multiple target assignment
z=z1=z2=z3=20

# Augmented Assignment
A=10
A+=2
# a=a+2






