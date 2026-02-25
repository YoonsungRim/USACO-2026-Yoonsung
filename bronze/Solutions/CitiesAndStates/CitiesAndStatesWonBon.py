T=int(input())
ans=0
statelist=[] # [MIFL,DATX,FLMI,CLSC,BOMA,ORFL]
for i in range(T):
    N,K= input().split()
    statelist.append(N[0:2]+K)
#[MIFL,DATX,FLMI,CLSC,BOMA,ORFL]
for j in statelist[1::]: #FLMI
    for k in statelist: #MIFL
        if j== k[2:4]+k[0:2]: #쌍을 찾음
            ans+=statelist.count(k)