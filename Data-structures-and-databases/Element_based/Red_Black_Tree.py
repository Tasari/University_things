from Binary_Search_Tree import BST, BSTNode

class RBTNode(BSTNode):
    def __init__(self,
                 s = 97,
                 h = 53, 
                 data = None, 
                 parent = None, 
                 left = None, 
                 right = None,
                 color = 0):
        BSTNode.__init__(self,s,h,data,parent,left,right)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        assert color == 0 or color == 1 or color == 2, "Error"
        self.__color = color
    
class RBT(BST):
    def __init__(self):
        s = RBTNode(data='', color = 1)
        s.left = s
        s.right = s
        s.parent = s
        BST.__init__(self, sent = s)

    def insert(self, x):
        BST.insert(self, x)
        x.color = 0
        while x.parent is not self.sent and x.parent.color == 0:
            if x.parent is x.parent.parent.left:
                y = x.parent.parent.right
                if y.color == 0:
                    x.parent.color = 1
                    x.parent.parent.color = 0
                    y.parent.color = 1
                    x = x.parent.parent
                else:
                    if x is x.parent.right:
                        x = x.parent
                        self.rotate_left(x)
                    x.parent.color = 1
                    x.parent.parent.color = 0
                    self.rotate_right(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y.color == 0:
                    x.parent.color = 1
                    x.parent.parent.color = 0
                    y.parent.color = 1
                    x = x.parent.parent
                else:
                    if x is x.parent.left:
                        x = x.parent
                        self.rotate_right(x)
                    x.parent.color = 1
                    x.parent.parent.color = 0
                    self.rotate_left(x.parent.parent)
        self.root.color = 1

r = RBT()
r.insert(RBTNode())
r.insert(RBTNode())
r.insert(RBTNode())
r.insert(RBTNode())
r.insert(RBTNode())


