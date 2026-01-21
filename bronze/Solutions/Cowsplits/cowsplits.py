#Cow Splits
input1=list(map(int, input().split()))
T=input1[0]
k=input1[1]
for i in range(T):#테스트 케이스 개수
    M=0#시도횟수
    N=int(input()) #문자열 / 3
    S=input() #문자열 하나
    zerolist='0'*len(S)
    halflen=(len(S)//2)-1
    #n=1
    #zero=0
    for j in range(len(S)//2):#모든 줄에 대한 반복문
        if len(S)%2==1:#홀수라면
            n=2
        else:#짝수라면
            n=1
        zero=0
        halflen=(len(S)//2)-1
        for k in range(n):#줄 하나에 대한 반복문
            #4개씩 보기(1번)
            if S[zero:halflen] in S[halflen:]:
                M+=1
                S=S.replace(S[zero:halflen],'')
                zerolist=zerolist.replace(zerolist[zero:halflen],f'{M}'*len(zerolist[zero:halflen]))
                break#겹치는걸 찾아서 자르면 위에있는 forloop에서 다시 시작
            else:
                zero+=n
                halflen+=n
        halflen=(len(S)//2)-2
    print(M)
    print(zerolist)
            #3개씩 보기(3번)
            #2개씩 보기(5번)
            #1번씩 보기(7번) 
#test = cowcowowcowcowcowc