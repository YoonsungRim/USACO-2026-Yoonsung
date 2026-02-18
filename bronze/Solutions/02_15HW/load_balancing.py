#Load Balancing
with open("balancing.in", "r") as fin:
    line1 = fin.readline().split()
    if not line1: exit()
    cowsnum, farm = map(int, line1)
    
    coords = []
    x_coords = []
    y_coords = []
    
    for i in range(cowsnum):
        a = list(map(int, fin.readline().split()))
        coords.append(a)
        # 소의 좌표 옆(짝수)에 울타리를 쳐야 하므로 후보군 저장
        x_coords.append(a[0] + 1)
        y_coords.append(a[1] + 1)

anslist=[]
for xfence in range(farm):
    for yfence in range(farm):
        F=[0,0,0,0,0]
        for coord in coords: #[x,y]
            if coord[0]>xfence:#오른쪽
                if coord[1]>yfence:#위에
                    F[1]+=1 #제1사분면에 1 더하기
                else:#오른쪽 아래에 (4사분면)
                    F[4]+=1
            else:#왼쪽
                if coord[1]>yfence:#위에
                    F[2]+=1 #제2사분면에 1 더하기
                else:
                    F[3]+=1 #제 3사분면
        anslist.append(max(F))

with open("balancing.out", "w") as fout:
    fout.write(str(min(anslist)) + "\n")
