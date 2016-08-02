import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
         #Write your code here
            qu = []
            if not root:
                return None
            
            current = root
            qu.append(current)
            output = []
            
            while(qu):
                current = qu.pop(0)
                output.append(current.data)
                
                if current.left:
                    qu.append(current.left)
                if current.right:
                    qu.append(current.right)

            print " ".join(map(str,output))

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)                
                        