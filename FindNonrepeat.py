s="swiss"
t={}
count=0
def NonRepeat (s):
    for i in s:
        if i in t:
                t[i] += 1
        else:
                t[i] = 1
    non_repeated = [i for i in t if t[i] == 1]
    
    return non_repeated
result=NonRepeat (s)  
print(result)
