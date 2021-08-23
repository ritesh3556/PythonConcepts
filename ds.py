class node:
    def __init__(self):
        self.data = None
        self.next = None 
    def getdata(self):
        return self.data
    def setdata(self,data):
        self.data=data
    def setnext(self,next):
        self.next=next
    def getnext(self):
        return self.next
    def hasnext(self):
        return self.next != None
    
    def listLength(self):
        current=self.head
        count = 0
        while(current != None):
            count+=1
            current = current.next
            
        return count    
    def insertb(self,head,data):
        newNOde = node()
        newNOde.data = data
        if head==None:
            head=newNOde
        else:
            newNOde=self.head
            self.head = newNOde
                

if __name__=="__main__":
    a = node()
    head=None
    a.insertb(head,2)
