n, m  = map(int,input().split())
num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))

if sum(num1)== sum(num2):
    print("Equal")
else:
    print("Not Equal")