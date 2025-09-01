#-------------------------
# file: myscript.py

def square(x):
    """Square a number"""
    return x ** 2

for N in range(1,4):
    print(N,"Squared is:", square(N))