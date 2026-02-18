#TheGreatRevegetation

with open("revegetate.in", "r") as fin:
    N,M=map(int, fin.readline().split()) # N=목초지 개수 M=소 마릿수

    adjland=[]

    for i in range(N+1):
        adjland.append([]) # 목초지 N+1개만큼 []생성

    for _ in range(M):
        u,v=map(int,fin.readline().split()) #소가 밥먹는 목초지 u,v (풀 종류 달라야함)
        adjland[u].append(v)
        adjland[v].append(u)

    answer=[0]*(N+1) # 각 목초지에 어떤 풀을 심었는지...

    for i in range(1,N+1): # 목초지 전체 돌기
        used=[0]*5 # 지금있는 땅에서 쓸수없는 풀 표시
        for neighbor in adjland[i]:
            if answer[neighbor]!=0:
                used[answer[neighbor]]=1

        for seed in range(1,5):
            if used[seed]==0:
                answer[i]=seed
                break

with open("revegetate.out", "w") as fout:
    fout.write("".join(map(str, answer[1:])))
