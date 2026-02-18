#처음에 짝수 두번째 홀수 세번째 짝수 네번쨰 홀수 ...
n=int(input())
numbers=list(map(int, input().split()))
even=0
odd=0

for i in numbers:
    if i%2==0:
        even+=1
    else:
        odd+=1

while odd>even:
    odd-=2
    even+=1

if even>odd+1:
    print(odd*2+1)
else:
    print(even+odd)