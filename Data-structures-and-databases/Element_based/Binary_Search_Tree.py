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
    def __init__(self, sent = None):
        if sent is None:
            sent = BSTNode(data='')
        self._sent = sent
        self._root = sent
    
    @property
    def sent(self):
        return self._sent
    
    @property
    def root(self):
        return self._root

    def insert(self, x):
        x.parent=self._sent
        x.right=self._sent
        x.left=self._sent
        y = self._root
        if y is self._sent:
            self._root = x
            return
        while y is not self._sent:
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

    def search(self, k):
        actual_node = self._root
        while actual_node is not self._sent and actual_node.key != k:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def inorder(self):
        self.__inorder(self._root)

    def __inorder(self, node):
        if node is not self.sent:
            self.__inorder(node.left)
            print(node)
            self.__inorder(node.right)
    
    def preorder(self):
        self.__preorder(self._root)

    def __preorder(self, node):
        if node is not self._sent:
            print(node)
            self.__preorder(node.left)
            self.__preorder(node.right)

    def postorder(self):
        self.__postorder(self._root)

    def __postorder(self, node):
        if node is not self._sent:
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(node)
    
    def minimum(self, node):
        while node.left is not self._sent:
            node = node.left
        return node

    def maximum(self, node):
        while node.right is not self._sent:
            node = node.right
        return node

    def successor(self, node):
        if node.right is not self._sent:
            return self.minimum(node.right)
        while node.parent is not self._sent and node.parent.right is node:
            node = node.parent
        return node.parent

    def delete(self, node):
        if node.left is self._sent or node.right is self._sent:
            work_node = node
        else:
            work_node = self.successor(node)
        if work_node.left is self._sent:
            x = work_node.right
        else:
            x = work_node.left
        if x is not self._sent:
            x.parent = work_node.parent
        if work_node.parent is self._sent:
            self._root = x
        else:
            if work_node is work_node.parent.left:
                work_node.parent.left = x
            else:
                work_node.parent.right = x
        if work_node is not node:
            node.data = work_node.data
        return node

    def rotate_right(self, y):
        x = y.left
        if x is self._sent:
            return
        y.left = x.right
        x.right.parent = y
        x.parent = y.parent
        if y.parent is self._sent:
            self._root = x
        elif y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x
    
    def rotate_left(self, y):
        x = y.right
        if x is self._sent:
            return
        y.right = x.left
        x.left.parent = y
        x.parent = y.parent
        if y.parent is self._sent:
            self._root = x
        elif y is y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.left = y
        y.parent = x