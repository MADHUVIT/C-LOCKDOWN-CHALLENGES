strinput=input()
for i in range(len(strinput)):
    print(strinput[i],end='')
    try:
       if strinput[i+1]==strinput[i]:
          print('*',end='')
    except:
        q=0
    
