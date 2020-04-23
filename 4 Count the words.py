strinput=input().split(' ')
l=[] #list of non repetitive word
for i in strinput:
    if i not in l:
        l.append(i)
        print(i,strinput.count(i))
        
