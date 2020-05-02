class node:
    
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,x):
        self.items.insert(0,x)
    def is_empty(self):
        return len(self.items)==0
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
    def print(self):
        print(self.items)             
class binary:
    
    def __init__(self,x):
        self.root=node(x)
        

    def pre(self,roo):
        
        
        if roo is not None:
            print(roo.val)
            self.pre(roo.left)
            self.pre(roo.right)
        
            
    
            
    def height(self,roo):
        if roo is None:
            return 0
        l=self.height(roo.left)
        r=self.height(roo.right)
        return 1+max(l,r)
    
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        l=self.height(root.left)
        r=self.height(root.right)
        print(l,r)
        ld=self.diameterOfBinaryTree(root.left)
        rd=self.diameterOfBinaryTree(root.right)
        return max(l+r,max(ld,rd))
   
            
            
class bst:
    def __init__(self,data):
        self.root=node(data)
    def insert(self,data):
        if self.root is None:
            self.root=node(data)
        else:
            self._insert(data,self.root)
    def _insert(self,data,curr):
        if data<curr.val :
            if curr.left is None:
                curr.left=node(data)
            else:
                self._insert(data,curr.left)
        elif data>curr.val:
            if curr.right is None:
                curr.right=node(data)
            else:
                self._insert(data,curr.right)
        else:
            print("data is already present")
    def find(self,data):
        if self.root:
            found=self._find(data,self.root)
            if found:
                return True
            else:
                return False
        else:
            return None
    def _find(data,curr):
        if data==curr.val:
            return True
        elif data>curr.val and curr.right:
            self._find(data,curr.right)
        elif data<curr.val and curr.left:
            self._find(data,curr.left)
            

    
                
                
                
def bfs(roo):
    
    q=queue()
    s=0
    if roo is None:
        pass
    
    q.enqueue(roo)
    while len(q)> 0:
        
        x=q.dequeue()
        print(x.val)
        if x.left:
            q.enqueue(x.left)
            
        if x.right:
            q.enqueue(x.right)
    print(s)
        
        
                  
a=binary(1)
a.root.left=node(2)
a.root.right=node(3)
a.root.right.right=node(5)
a.root.left.right=node(9)
a.root.left.left=node(4)
bfs(a.root)








        
    