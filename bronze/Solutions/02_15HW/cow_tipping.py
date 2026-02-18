with open("cowtip.in", "r") as fin:
    line1 = fin.readline().strip()
    if not line1: exit()
    lines = int(line1)
    
    field = []
    ans = 0
    
    for _ in range(lines):
        row_data = fin.readline().strip()
        field.append(list(map(int, row_data)))



for i in range(lines,0,-1):
    for j in range(lines,0,-1):#뒤에서부터 반복문
        if field[i-1][j-1]==1:
            for k in range(i):
                for l in range(j):
                    if field[k][l]==0:
                        field[k][l]=1
                    elif field [k][l]==1:
                        field[k][l]=0
            ans+=1


with open("cowtip.out", "w") as fout:
    fout.write(str(ans) + "\n")