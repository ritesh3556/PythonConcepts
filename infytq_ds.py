#class node:
#    def __init__(self,item):
#        self.item=item
#        self.next=None
#class linked:
#    def __init__(self):
#        self.head=None        
#    def printf(self):
#        temp=self.head
#        while(temp!=None):
#            print(temp.item)
#            temp=temp.next
#        print('\r')    
#    def insertAtf(self,item):
#        n=node(item)
#        n.next=self.head
#        self.head=n
            


    
  #

#if __name__=='__main__':
    #n=linked()
    #n.head=node(1)
    #second=node(2)
    #third=node(3)
    #n.head.next=second
    #second.next=third
    #n.printf()
    #n1=linked()
    #n1.head=node(4)
    #secon=node(5)
    #thir=node(6)
    #n1.head.next=secon
    #secon.next=thir
    #n1.printf()
 #   n1=linked()
 #   n1.insertAtf(3)
 #   n1.insertAtf(2)
 #   n1.insertAtf(1)
 #   n1.printf()
     
  #  n2=linked()
   # n2.insertAtf(6)
   # n2.insertAtf(5)
   # n2.insertAtf(4)
   # n2.printf()




#class node:
#    def __init__(self,item):
#        self.item=item
#        self.next=None
#        self.prev=None
#class dlinked:
#    def __init__(self):
#        self.head=None

#    def insertAtf(self,item):
#        n=node(item)
#        n.item=item
#        n.prev=None
#        n.next=self.head
#        self.head=n

    
#   def insertm(self,item,index):
#        n=node(item)
#        temp=self.head
#        if self.head==None:
#            n.next=self.head
#            n.prev=None
#            self.head=n 
#        else:
#            l=1
#           while(l<index-1):
#                temp=temp.next
#                l+=1
#            n.next=temp.next
#            n.prev=temp
#            temp.next=n

#   def delete(self,index):
#        temp=self.head        
#        l=1
#        while(l<index-1):
#            temp=temp.next
#            l+=1
#        temp.next=temp.next.next
#        temp.next.next.prev=temp

        





 #   def printf(self):
 #       temp=self.head
 #       while(temp!=None):
 #           print(temp.item)
 #           temp=temp.next
 #   def length(self):
 #       temp=self.head
 #       l=0
 #       while(temp!=None):
 #           l+=1
 #           temp=temp.next
 #       return l    



#if __name__=='__main__':
#    l=dlinked()
#    l.insertAtf(4)
#    l.insertAtf(3)
#    l.insertAtf(2)
#    l.insertm(8,2)#
    #print(dlinked.length(l))
#    l.printf()
#    l.delete(2)
#    l.printf()


class array:
    def __init__(self,size):
        self.size=size
        self.l=[0]*size

    

#class stack:
    #def __init__(self):
        #self.top=-1

    #def sizes(self,size):
      #  self.size=size
     #   self.n=array(size)
    #def push(self,item):
        
      #  if self.top==self.size-1:
      #      print('Stack is full')
     #   else:
     #       self.top+=1
     #       self.n.l[self.top]=item
    #def pop(self):
    #    self.top=self.top-1

    #def peek(self):
   #     return self.n.l[self.top]

  #  def printf(self):
 #       i=self.top
#        while(i>=0):
#            print(self.n.l[i])
#            i-=1

#if __name__=='__main__':
  #  a=stack()
  #  a.sizes(5)
  #  a.push(5)
 #   a.push(4)
 #   a.push(3)
 #   a.push(2)
#    a.push(1)
    #a.push(0)
#    #print(a.peek())
#    a.printf()
    #a.pop()
    


#class ABCMeta:
#    def __init__(type):
#        pass 

#class Shape(metaclass=ABCMeta):
#    def __init__(self):
#        print("i am init ")

#    def draw(self):
#        pass
    
    #def set_color(self):
     #   pass
#class Circle(Shape):
#    def draw_Shape(self):
#        print('draw circle')    


#a=Circle()
#a.draw_Shape()

def binarysearch(l,low,hi,item):
    mid=(low+hi)//2
    if l[mid]==item:
        return item
    
    if low>hi:
        return -1
    if item<l[mid]:
        return binarysearch(l,low,mid-1,item)
    else:
        return binarysearch(l,mid+1,hi,item)    
    
l=[1,2,74,5,1,25,1,47,52,4,]
low=0
hi=len(l)-1
print(binarysearch(l,low,hi,52))









        







































