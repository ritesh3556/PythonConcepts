
class Node:
    def  __init__(self,item):
        self.item = item
        self.left=None
        self.right=None

class bs:
    def __init__(self):
        self.root=None


def insertt(root,item):

    if root==None:
        return Node(item)
    if root.item < item:
        root.right = insertt(root.right,item)
    else:
        root.left = insertt(root.left,item)
    return root
def printt(root):
    
    if root!=None:
        print(root.item,end=' ')
        printt(root.left)
        
        
        printt(root.right)



def height(root):

    if root==None:
        return 0

    return height(root.left)+height(root.right)+1

root = None
root = insertt(root,4)
root = insertt(root,1)
root = insertt(root,2)
root = insertt(root,5)
root = insertt(root,6)
root = insertt(root,8)
root = insertt(root,7)
#printt(root)
print(height(root))









