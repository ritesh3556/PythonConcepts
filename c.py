#n=int(input("enter"))

#def f(n):
 #   c=0
  #  while(n>0):
   #     if n==1:
    #        return c
      #  elif n%2==0:
     #       n//=2
       #     c+=1
        #elif n%3==0:
         #   n//=3
          #  c+=1
        #else:
         #   n=n-1
          #  c+=1       

#print(f(n))   

def span(l):
    c=0
    if l==0:
        return 0
    if len(l)==1:
        return 1
    z=[]    
    for i in range(len(l)):
        s=l[0]
        k=0
        for j in range(len(l)-1,i,-1):
            if c>=1:
                k+=1
                continue

            if s==l[j]:
                c+=1
        z.append(k)

    print(z)

print(span([1,2,1,1,3]))    
