#livestocklineup
cows=["Beatrice","Belinda","Bella","Bessie","Betsy","Blue","Buttercup","Sue"]
n=int(input())
condition=[]
for _ in range(n):
    words = input().split()
    condition.append([words[0],words[5]])
#[['Buttercup', 'Bella'], ['Blue', 'Bella'], ['Sue', 'Beatrice']]

