#Why Did the Cow Cross the Road II
# ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ
with open("circlecross.in", "r") as fin:
    string=fin.readline().strip()

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans=0

for i in alphabet:
    stpt=string.find(i)
    edpt=string.find(i,stpt+1)
    
    sub_string=string[stpt+1:edpt]
    for j in sub_string:
        if sub_string.count(j)==1:
            ans+=1

final_ans=ans // 2

with open("circlecross.out","w") as fout:
    fout.write(str(final_ans) + "\n")