class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right= None

class BST:
  def __init__(self):
    self.root=None
  def create(self,val):
    if self.root==None:
      self.root=Node(val)
    else:
      current=self.root
      while True:
        if val<current.data:
          if current.left:
            current=current.left
          else:
            current.left=Node(val)
        elif val> current.data:
          if current.right:
            current=current.right
          else:
            current.right=Node(val)
        else:
          break


def inOrder(root):
  if root:
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

def postOrder(root):
  if root:
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

def preOrder(root):
  if root:
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

def heightOfTree(root):
  if root:
    return 1 + max(heightOfTree(root.left),heightOfTree(root.right))
  else:
    return -1

def levelOrderTraversal(root):
  if root==None:
    return
  q=[root]
  while (len(q)>0):
    n=q.pop(0)
    print(n.data)
    if n.left:
      q.append(n.left)
    if n.right:
      q.append(n.right)

def LowestCommonAncestral(root,v1,v2):
  if(root.data<v1) and (root.data<v2):
    LowestCommonAncestral(root.right,v1,v2)
  elif(root.data>v1) and (root.data>v2):
    LowestCommonAncestral(root.left,v1,v2)
  else:
    return root

def spiralTraversal(root):
  o=[]
  e=[]
  e.append(root)
  #print(root)
  while (len(e)!=0 or len(o)!=0):
    while(len(e)!=0):
      c=e.pop()
      print(c.data)
      if c.right:
        o.append(c.right)
      if c.left:
        o.append(c.left)
    while(len(o)!=0):
        c=o.pop()
        print(c.data)
        if c.left:
            e.append(c.left)
        if c.right:
            e.append(c.right)
  


tree=BST()
n=int(input())
a=[int(i) for i in input().split()]
for i in range(n):
  tree.create(a[i])
#h= heightOfTree(tree.root)
#levelOrderTraversal(tree.root)
#a=LowestCommonAncestral(tree.root,1,7)
#print(a.data)
spiralTraversal(tree.root)
