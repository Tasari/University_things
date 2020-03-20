from Element import Element

class BSTNode(Element):
    def __init__(self,
                 s = 97,
                 h = 53, 
                 data = None, 
                 parent = None, 
                 left = None, 
                 right = None):
        Element.__init__(self, data, s, h)
        self.__l = left
        self.__r = right
        self.__p = parent

    @property
    def l(self):
        return self.__l

    @property
    def left(self):
        return self.l

    @property
    def r(self):
        return self.__r

    @property
    def right(self):
        return self.r
    
    @property
    def p(self):
        return self.__p

    @property
    def parent(self):
        return self.p
    
    @r.setter
    def r(self, x):
        self.__setfield('__r', x)

    @right.setter
    def right(self,x):
        self.__setfield('__r', x)
    
    @l.setter
    def l(self, x):
        self.__setfield('__l', x)

    @left.setter
    def left(self,x):
        self.__setfield('__l', x)

    @p.setter
    def p(self, x):
        self.__setfield('__p', x)

    @parent.setter
    def parent(self,x):
        self.__setfield('__p', x)
    
    def __setfield(self, name, value):
        assert value is None or isinstance(value, BSTNode), "Error"
        if name == '__l':
            self.__l = value
        elif name == '__r':
            self.__r = value
        elif name == '__p':
            self.__p = value

class BST:
    def __init__(self):
        self.__root = None

    def insert(self, x):
        y = self.__root
        if y is None:
            self.__root = x
            return
        while y is not None:
            z = y
            if x < y:
                y = y.left
            else:
                y = y.right
        x.parent = z
        if x < z:
            z.left = x
        else:
            z.right = x
    def inorder(self):
        self.__inorder(self.__root)

    def __inorder(self, node):
        if node is not None:
            self.__inorder(node.left)
            print(node)
            self.__inorder(node.right)
