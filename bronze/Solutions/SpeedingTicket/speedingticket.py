with open("speeding.in", "r") as fin:
    firstinput=list(map(int, fin.readline().split()))
    n,m=firstinput[0],firstinput[1]
    speedlimit=[]
    currentspeed=[]
    for _ in range(n):
        a=list(map(int, fin.readline().split()))
        for _ in range(a[0]):
            speedlimit.append(a[1])

    for _ in range(m):
        b=list(map(int, fin.readline().split()))
        for _ in range(b[0]):
            currentspeed.append(b[1])

    diff=[0]
    for i in range(100):
        if speedlimit[i]<currentspeed[i]:
            diff.append(currentspeed[i]-speedlimit[i])

with open("speeding.out", "w") as fout:
    fout.write(str(max(diff)) + "\n")