fin = open('citystate.in', 'r')
fout = open('citystate.out', 'w')

line = fin.readline().strip()
if line:
    T = int(line)
    ans = 0
    statelist=[]
    for _ in range(T):
        data = fin.readline().split()
        if len(data) < 2: continue
        
        city, state = data[0], data[1]
        statelist.append(city[0:2] + state)

    for j in statelist: 
        for k in statelist:
            if j[0:2] == j[2:4]: continue 
            
            if j == k[2:4] + k[0:2]:
                ans += 1 
    fout.write(str(ans // 2) + '\n')

fin.close()
fout.close()