N,K=map(int, input().split())
anslist=[]
for _ in range(K):
    x,y,z= map(int, input().split())
    anslist.append((x-1,y-1,z-1))
maxscore=0
possibleboards=0

boards=[""]

for _ in range(N):#가능한 보드 조합들 만들기(N번 반복해서 길이 N의 보드 만들기) N=3이라면
    newboards=[]
    for b in boards:
        newboards.append(b + "M") #["M,"O"]가 있으면 M에 M이랑 O 붙여서 두개 만들기 ["MM","MO"]
        newboards.append(b + "O") #["M,"O"]가 있으면 O에 M이랑 O 붙여서 두개 만들기 ["OM","OO"]
    boards=newboards
#1.boards=["M", "O"]
#2.boards=["M+M","M+O","O+M" "O+O"] = ["MM", "MO", "OM", "OO"]
#3.boards=["MMM", "MMO", "MOM", "MOO", "OMM", "OMO", "OOM", "OOO"]

for board in boards:#["MMM", "MMO", "MOM", "MOO", "OMM", "OMO", "OOM", "OOO"]
    score=0
    for x,y,z in anslist:#숫자가 세개
        if board[x]=='M':#숫자가 가르키는 인덱스가 "M이라면"
            if board[y]=='O':
                if board[z]=='O':
                    score+=1#조건충족
    if score>maxscore:#1등
        maxscore=score
        possibleboards=1
    elif score==maxscore:#공동1등
        possibleboards+=1

print(maxscore, possibleboards)