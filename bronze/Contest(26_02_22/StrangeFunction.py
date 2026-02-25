#strangefunction
T=int(input())
for _ in range(T):
    ans=0
    a=input()
    number=[]
    for i in a:
        number.append(int(i))
    for i in range(len(number)):
        if number[i] > 1:
            ans+=1
            break
    for i in range(len(number)):#일단 2-9까지 숫자 바꿔줌 (3 0 3 3)
        if number[i] > 1:
            if number[i]//2==0:#짝
                number[i]=0
            else:#홀
                number[i]=1
    #number = 현재 [1,0,1,1]
                #  1 2 4 8
    for j in number[::-1]:
        if j==1:
            if number.index(j)==0:
                ans+=1 
            else:
                ans+=2**number.index(j)
print(ans)
            