cowdict={'Bessie':0, 'Elsie':0, 'Daisy':0, 'Gertie':0, 'Annabelle':0, 'Maggie':0, 'Henrietta':0}


with open("notlast.in", "r") as fin:
    n = int(fin.readline())
    for _ in range(n):
        input1=fin.readline().split()
        cow=input1[0]
        times=int(input1[1])
        if cow in cowdict.keys():#
            cowdict[cow]+=times

cowslist=list(cowdict.values())
firstmin=min(cowslist)
while firstmin in cowslist:
    cowslist.remove(min(cowslist))

with open("notlast.out", "w") as fout:
    if cowslist==[]:
        fout.write( "Tie\n")
    else:
        num=cowslist.count(min(cowslist))
        secondmin=min(cowslist)
        if num>1:#두번째로 작은게 2개 이상이면:
            fout.write( "Tie\n")
        else:
            for i in cowdict:
                if cowdict[i]==secondmin:
                    fout.write(i + "\n")

                # 만약에 num이 딕셔너리에 있다면:
                # 그 키를 프린트해라.
