import math

def mathmodule(v):
    s = math.sqrt(v)
    l = math.log(v)
    #m = math.sin(math.radians(v))
    m = math.sin(v)
    return s , l, m

n = int(input("Enter the number: "))

sqrt, log, sine = mathmodule(n)

print(f"Square root: {sqrt}  \nlogarithm = {log} \nSine = {sine}")