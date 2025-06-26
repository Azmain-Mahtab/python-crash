import sys

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

a = float(sys.argv[1])
operation = sys.argv[2]
b = float(sys.argv[3])




if operation == 'add':
    print(add(a, b))
elif operation == 'sub':
    print(sub(a, b))
elif operation == 'mul':
    print(mul(a, b))

