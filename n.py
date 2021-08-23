#import time

#name = "ritesh"
#age = 20
#print("{ \"name is\" : "+name+" , \"age is\" : "+str(age)+"}")
#print("name is = {} and age is = {} ".format(name,age))  
#a,b,c = map(int,input("enter three numbers separated by space ").split())
#s = (a,b,c)
#print(f"average = {sum(s)/3}")
#language = "python"
#for i in range(len(language)):
 #   print(i)

#name = "RiTesH"
#n =""
#for i in name:
 #   print(i.lower())
  #  print(i.upper())
   # if i == i.lower():
       
    #   n+=i.upper()
    #else:
       
 #      n+=i.lower()    
#print#(n)
#s = 34
#print(f"binary of {s}  is {bin(s)[2:]}")


#n = int(input())
#rr = []
#for i in range(n):
#    ui = int(input())
#    arr.append(ui)
##t = set(arr)
#m = max(t)
#print(m)
#t1=time.time()
#def greatest(a,b):
 #  g = (a,b)
  # g = max(g)
  # return g


#def greater(a,b,c):
#   return greatest(greatest(a,b),c)
    


#a,b,c = map(int, input().split())
#print(greater(a,b,c))


#number = int(input())
#def rev(l):
 #  return [i[::-1] for i in l]


#print(rev(['abc','cde','fgh']))

#s= "ritesh2297"
#f= s.islower()
#print(f)      
      
#name ="      riTesh gupta      "
#dot ="..........."
#print(len(name))
#print(name.lower())
#print(name.upper())
#print(name.title())
#print(name.count("t"))
#print(name.strip()+dot)
#print(name.replace("T","q"))
#print(name.find("t"))
#print([print(f"2 * {i} : {2*i}") for i in range(1,11)])
#for i in range(10,0,-1):
 # print(i)
#def fabinacci(n):
#  a=0
#  b=1
  #if n==1:
    #print(a)
  #elif n==2:
    #print(a,b)
#  print(f"{a},{b}",end="")
#  for _ in range(n-2):
#    c=a+b
#    a=b
#    b=c
#    print(f",{b}\t") 
    
#print(fabinacci(3))       
#n=5
#def g():
 # global n
 # n=7
#  return n
#print(n)
#t1=time.time()
#print(g())
#print(n)  
#t2=time.time()
#t=t2-t1
#print(t)
#print([name[i] for i in range(len(name))])
#name=["rietsh","20"]
#print("".join(name))
#a=['r','i','t','e','s','h']
#b='ritesh'
#l=[i for i in b]
#print(l)
#l1=[1,2,3,4]
#l2=[1,2,5,6]
#l1=set(l1)
#l2=set(l2)
#print(f"common in l1 and l2 {l1&l2}")
#def common(l1,l2):
 # return ([i for i in l1 if i in l2])
#print(f"common are {common(l1,l2)}")  
#lt = [1,2,3,[5,1],[6,5],[45]]
#count=0
#for i in lt:
 # if type(i)==list:
#    count+=1
#print(count)
#dictionary--->

#user = {'name':'ritesh','age':20}
#for i,value in user.items():
  #print(value)  
#user['class']='fifth'
#p =user.pop('age')
#print(p)
#print(user)

#def cube_finder(d):
  #cubes={}
  #for i in range(d):
   # cubes[i]=i**3
  #return cubes
#print(cube_finder(3))  
#def check_sum(*args):
 # if any([(type(arg)==int or type(arg)==float) for arg in args]):
 #   t=0
  #  for i in args:
  #    t+=i
   # return t
  #return "invalid input" 
#print(check_sum(1,2.3,5))    
#d =dict(a='name',b=20)
#print(d)
#t2=time.time()
#print(t2-t1)



#s=[[1,2,3,2],[2,3]]
#print(s[1][1])
#for _ in range(int(input('enter'))):
#  name=input("name")
#  score=int(input("score"))
#  m.append([name,score])
#  s.append(score)
#print(m)   
#m=min(s)
#s.remove(min(s))
#i=0
#while(i<len(s)):
#  if m in s:
#    s.remove(m)
#smin=min(s)

#if __name__ == '__main__':
  #  m=[]
 #   s=[]
    #for _ in range(int(input())):
   #     j=[]
   #     name = input()
    #    score = float(input())
    #    m.append([name,score])
    #    s.append(score)
    #l=len(s)    
    #mi=min(s)
    #print(mi)
    #for i in s:
    #    if mi == i:
   #         s.remove(i)
          
    #sm=min(s)
    #n=[]
    #i=0
    #while(i<len(m)):
     #   if sm==m[i][1]:
     #       n.append(m[i][0])
     #   i+=1    
    #n.sort()
    #print(sm)
    #print(n)
   # for i in n:
        #print(i)
#n = int(input())
#student_marks = {}
#for _ in range(n):
  #name, *line = input().split()
 # scores = list(map(float, line))
 # student_marks[name] = scores
#query_name = input()

#print(student_marks)
#print(student_marks.get(query_name))
#a=map(int,input().split())
#n=int(input())
#for i in range(n):
  #x=map(int,input().split())
  #y=map(int,input().split())
#for i in x:
  #print(i)
#def centered_average(nums):
  #n=len(nums)-2
  #nums.sort()
  #print(nums)
  #if(nums[0] == nums[1]):
   # t=0
    #nums.remove(nums[0])
    #print(nums)
    #print(len(nums)-1)
    #for i in range(1,len(nums)-1):
    # print(i)
    #  t+=nums[i]
    #return t//n
  #else:
   # t=0
    #for i in range(1,len(nums)-1):
     # t+=nums[i]
    #return t//n  
#print(centered_average([1, 1, 5, 5, 10, 8, 7]))





#x=5
#y=10
#x^=y 
#y^=x
#x^=y
#print("swap : "+str(x),str(y))

#
#
#
#def f(m):
#  if m == 0:
#    return(0)
#  else:
#    return(m+f(m-1))
#print(f(16)) 
# 
# 
#n = "rritesh golu best hai"
#(n.capitalize())
#print(n.title())

#s = input()
#for x in s.split():
  #print(x)
  #s = s.replace(x, x.capitalize())
 # print(s)
#print(s)   


#Replace all ______ with rjust, ljust or center. 

#thickness = int(input()) #This must be an odd number
#c = 'H'

#Top Cone
#for i in range(thickness):
#  print((c*i).______(thickness-1)+c+(c*i).______(thickness-1))






#n=[1,2,3,4,]
#print(n[::-1])

#print(n)
#m="yes"
#j=1
#for i in range(1,5):
 # print(j)
  #j=j*11

#def f(n):
 # n=str(n)
 # return int(n[::-1])
#print(f(123))
#n=int(input("enter : "))
#for i in range(2,n+1):
 # if n%i==0:
  #  break
#print(i)  
#if i == n:
 # print('yes') 
#else:
 # print('no') 
#n="(ritesh)"
#print(n[-1]) 
#def mystery(l):
 #   l = l + l
  #  return()

#mylist = [22,34,57]
#print(mystery(mylist))
#print(mylist)

#startmsg = "hello"
#endmsg = ""
#for i in range(0,len(startmsg)):
#  endmsg = startmsg[i] + endmsg
 # print(endmsg)
#print(endmsg)  


#x = [13,4,17,1000]
#w = x[1:]
#u = x[1:]

#y = x

#u[0] = 50
#y[1] = 40
#print(x)
#print(x[1])
#print(x[1], y[1], w[0], u[0])
#import sys
#input = sys.stdin.readlines()
#for line in input:
#    if int(line) == 42:
#        break
#    print(int(line))
    



#l = [1,2,3,4]
#a = l
#a[1] = 20
#print(l)

#x = [1,"abcd",2,"efgh",[3,4]]  # Statement 1
#y = x[0:50]                    # Statement 2
#z = y                          # Statement 3
#w = x                          # Statement 4
#x[1] = x[1] + 'd'              # Statement 5
#y[2] = 4                       # Statement 6
#x[1][1] = 'y'                  # Statement 7
#$z[0] = 0                       # Statement 8
#w[4][0] = 1000                 # Statement 9
#a = (x[4][1] == 4)             # Statement 10


#x = [13,4,17,1000]
#w = x[1:]
#u = x[1:]
#y = x
#u[0] = 50
#y[1] = 40

#print(x[1], y[1], w[0], u[0])


#startmsg = "hello"
#endmsg = ""
#for i in range(0,len(startmsg)):
 # endmsg = startmsg[i] + endmsg
#print(endmsg)


#def mystery(l):
 # l = l + l
  #return()

#mylist = [22,34,57]
#print(mystery(mylist))




#def accordian(l):
 # a = []
  #for i in range(len(l)-1):
   # a.append(max(l[i],l[i+1])-min(l[i],l[i+1]))
  #print(a)
  #n=0
  #for i in range(len(a)-2):
  #  if ((a[i+1]-a[i])>0) and ((a[i+2]-a[i+1])<0):
   #   n+=1
  #if n+1 == len(a)-2:
   # return True    
  #return False

#print(accordian([1,5,1]))    

#name = 'ritesh'
#print(name[-1:])
#def mystery(l):
  #if l == []:
   # return (l)
  #else:
    #return (l[-1:] + mystery(l[:-1]))
#print(mystery([31, 32, 71, 18, 51]))
#pairs = [ (x,y) for x in range(3,0,-1) for y in range(2,0,-1) if (x+y)%3 == 0 ]
#print(pairs)
#d={'name':'ritesh'}
#d['sir_name']='gupta'
#print(d)
#print(help(dict))
#print(dict.__dict__)
#d1={}
#d1[[1,2]]=5

#print(d1)

#def make_chocolate(small, big, goal):
 # for i in range(big+1):
  #  for j in range(small):
   #   if (i*5+big*5 == goal):
    #    return j+1
  #return -1    
      

#print(make_chocolate(4, 1, 9))      



#l=[1,2,4,6,8,7]
#print(l.index(4))

#a=len('aaacopebbb')
#b='abcde'
#print(b[len(b)-3:])


#l = [1,2,54,5,5,85,8,4,1]
#l2=l.copy()
#l2.remove(l2[0])
#l2.remove(l2[-1])
#print(sorted(l2))

#nums=[4, 4, 4, 1, 5]
#nums.sort()
#sum=0
#c=0
#for i in range(1,len(nums)-1):
#  sum+=nums[i]

  #c+=1
#print(sum)  
#print(sum/c)  


#n = input("enter ").split()
#print(n[1])

#Q = int(input())
#l=[]
#a=0
#for j in range(Q):
#    ui = input().split()
#    if ui[0] == 'i' :
#        l.append(int(ui[1]))
#    elif ui[0] == 'd':
#        l.remove(int(ui[1]))
#    #print(a)    
#    if a==0:
#      print(l.index(int(l[0]))+1) 
#     a+=1 
#      continue 
#   # print(l[0],int(ui[1]))  
#    if l[0]<int(ui[1]):
#      print((2*(l.index(l[0])+1)+1))             
#    if l[0]>int(ui[1]):
#      print((2*(l.index(l[0])+1)))  
   
#n=int(input("object")) 
#k=int(input('group'))
#w=int(input("ways"))
#for i in range(w):
  #for j in range(k):
   # for a in range(n):
      #print(i,end='')

#l=[1,2,3]
#l1=sum(l)
#print([[a,b]  for a in l for b in [1,2] if a!=b])
#print([sum([a,b])  for a in l for b in l if a!=b])
#ts=sum([sum([a,b])  for a in l for b in l if a!=b])
#print(f"total list sum = {l1+ts}")
#print(([1,2,3])*([4,5,6]))
#A= [1, 2]
#B = [3, 4]

#A*B = [(1, 3), (1, 4), (2, 3), (2, 4)]
#print(A*b)


#l=['bcdef','bcdef']
#print(set(l))

#name='ritesh'
#print(sorted(name))



#n, m = input().split()

#sc_ar = input().split()

#A = input().split()
#B = input().split()
#print(sc_ar)
#print(A, B)
#print(([(i in A) - (i in B) for i in sc_ar]))
#for i in sc_ar:
  #print((i in A)-(i in B))
  #print(i in B)


#if 'O'>'o':
  #print(True)
#else:
 # print(False)    

#s='Sorting1234'
#print(sorted(s)[::-1])
#for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
  #print((10**(i)//9)*i)
#
         
#$print(l)          

#def maxaggregate(l):
#  l=[]
#  d={}
 # for i in range(len(l)):
 #   d[l[i][0]]=l[i][1]
 
#print([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)])    

#l=[1,2,32,5,6]
#print(l[:-1])
#print("ritesh yo")


#l=list(map(int,input("enter any number : ").split()))
#s=0
#for i in range(len(l)):
#  s+=l[i]
#print(f"sum is {s}")  
#import math
#AB = float(input())
#BC = float(input())

#print(math.atan2(AB, BC),math.degrees(math.atan2(AB, BC)))

#print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')




#class ClassA:
  #def __init__(self, value):
   #self.value = value
#  def method_a(self) :
#    return 10+self.value
#class ClassB:
#  def _init_(self, val2):
#    self. num=val2
#  def method_b(self, obj):
#    return obj.method_a()+self.num

#obj1=ClassA(20)
#print(obj1.value)
#obj2=ClassB(30)
#print(obj2.method_b(obj1))

#class ClassA:
#  def __init__(self,value):
#    self.value=value

#o=ClassA(20)
#print(o.value)

#class ClassA:
#  def __init__(self, val1) :
#    self.value = val1
#  def method_a(self) :
#    return 10+self.value
#class ClassB:
#  def __init__(self, val2):
#    self. num=val2
#  def method_b(self, obj):
#    return obj.method_a()+self.num

#obj1=ClassA(20)
#obj2=ClassB(30)
#print(obj2.method_b(obj1))


# codechef AB A Con-cat

#n=int(input('enter \n'))
#a,b=input().split()
#k=int(input())
#for i in range(n-2):
#  c=a+b*2
#  a=b
#  b=c
#print(c)
#print(c[k-1])   # ass one as index

#l=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# 
#l1=[]
#for i in range(len(l)):
#  l2=[]
#  for j in range(len(l)):
#    l2.append(l[j][len(l)-1-i])
  #l1.append(l2)  

#print(l1)        


# array rotation                               #4 5 6 
#l=[[4,5,6],[8,4,7]]                    #8 4 7
#l2=[] 
#print([i in range(3) ] for j in range(3)])                                         #2 1 2
#for i in range(len(l)):
#  l1=[]
#  for j in range(len(l)):
#    l1.append(l[j][len(l)-i-1])
 # l2.append(l1)


#for i in l2:o
  #print(*i)


#class A:
#  def __init__(self):
#    #self.data=data
#    pass
#  def how(self,change):
#    self.change=change
#    return self.change#+self.data


#a=A()
#print(a.how(4))


#l=[1,2,3,4,65,4,6,6,6]
#print(l)
#l1=l
#l[2]=93
#l=[1,2]
#print(l)
#print(l1)
#l=[1,2,3,4,2]
#l1=l
#l1.remove(2)
#l.remove(2)
#print(l)
#print(l1)


#def secret(s):
  #i = 0
  #result = ''
 # print(s[0].isdigit())
#  while s[i].isdigit():
#    print(s[i])
#    result = result + s[i]
#    i = i + 1
#  print(result)
#secret('123')


#s='ritesh'
#print(s[5:])
#n=5
#m=3
#l=[1,2,3,4,5]
#l1=[6]
#for i in range(1,len(l)-m+1):
#  for j in range(i,m+i):
#    #print(l[j:m+i])
    #print(l[i:m])
#    if sum(l[j:m+i])<l1[0]:
#      print(l[j:m+i])
#      l1.append(sum(l[j:m+i]))
#print(l1)

t =int(input())



            
    
    
            
        
    
    

while(t):
    
    p,q,r = map(int,input().split())
    a,b,c = map(int,input().split())
    
    op = 0
    i=0
    while(1):
        if (p==a) and (q==b) and (r==c):
            break
        l=[]
        x = a-p
        y = b-q
        z = c-r
        if x!=0:
            l.append(x)
         
        if y!=0:
            l.append(y)
         
        if z!=0:
            l.append(z)
        
        m = min(l) 
         
        if p!=a:
            p+=m
        if q!=b:
            q+=m
        if r!=c:
            r+=m
        op+=1
        i+=1
    
    print(p,q,r)
    print(a,b,c)
    print(op)
    
    
    
    
    
    
    t-=1












