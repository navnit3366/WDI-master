from math import floor

n=int(input())
k=0

while n>0:
    k=k*10+n%10
    n=floor(n/10)

print(k)
