#Minimum of two numbers in Python
def mini(a,b):
    if a > b:
        return b
    else:
        return a

a=2
b=3
print(mini(a,b))

a=21
b=32
minimum=min(a,b)
print(minimum)