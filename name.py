h='-'
v='|'
d='\\'
c=0
for i in range(12):
    if i>0:
        if i!=5:
            print(v,end='')
    for j in range(7):
        if (i==0 or i==5) and (j>0 and j<5):
            print(h,end=' ')
        elif i>5 and i-j==5:
            print(d,end='')
        else:
            print(' ',end='')
            
            
    if i>0 and i<5: 
        print(v,end='')
    
    print('\r')    