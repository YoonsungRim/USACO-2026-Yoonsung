#makealldistinct
T=int(input())
for _ in range(T):
    ans=0
    N,K= map(int, input().split()) # N=4 . K=1
    listn=[]
    if K < 0:#절댓값 구함
        absoluteK=-1*K
    else:
        absoluteK=K
    
    listn=list(map(int, input().split()))# 4 1 4 1
    listn.sort()# 1 1 4 4
    dict={}
    for i in listn:
        if i%absoluteK not in dict.keys():
            dict[i%absoluteK]=[i]
        else:#이미 절대값이 dict에 있으면
            dict[i%absoluteK].append(i)

    for j in dict:# K=3 , (key들 순회)
        for l in range(1, len(dict[j])):# [1 1 4 4] --> [1 4 4]
            while dict[j][l] <= dict[j][l-1]:
                dict[j][l] += absoluteK
                ans += 1

    print(ans)

