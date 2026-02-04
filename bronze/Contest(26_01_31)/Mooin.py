#it's mooin time(후보 1)
firstinput = list(map(int, input().split()))
T=firstinput[0]
k=firstinput[1]
for _ in range(T):
    N=int(input())#testcase 길이
    S=input().strip()#tescase / OOMOO

    anslist=[]
    anslist.append(S[-1])#    ('O')
    if S[-1]=='O':
        howmanyOs=1
    elif S[-1]=='M':
        howmanyOs=0
    for i in S[-2::-1]: #    OOMO

        if howmanyOs%2==0 : #뒤에있는 O가 짝수일때 (안바뀜)
            if i=='M':
                anslist.append('M')
            elif i=='O':
                anslist.append('O')
                howmanyOs+=1
        elif howmanyOs%2==1 :  #뒤에있는 O가 홀수일때 (바뀜)

            if i=='M':
                anslist.append('O')
                howmanyOs+=1
            elif i=='O':
                anslist.append('M')
    print('YES')
    if k==1:
        print(''.join(anslist[::-1]))
