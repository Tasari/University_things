from Element import Element, Key

class ElementList(Element): 
    def __init__(self, s = 97, h = 53, data = None, right = None): 
        Element.__init__(self,data, s, h) 
        self.right = right
        
    @property 
    def right(self): 
        return self.__right
    
    @right.setter
    def right(self, nextval):
        assert nextval is None or isinstance(nextval,ElementList), "Error"
        self.__right = nextval

class List:
    def __init__(self):
        self.__head = None

    def insert(self, e):
        e.right = self.__head
        self.__head = e
    
    def search(self, e):
        x = self.__head
        while x is not None and x.key != e:
            x = x.right
        return x
    
    def delete(self, x):
        y = self.__head
        if x is y:
            self.__head = x.right
        while y is not None and y.right is not x:
            y = y.right
        try:
            y.right = x.right
            x.next = None
        except:
            pass

    def __repr__(self):
        x = self.__head
        s = ''
        while x is not None:
            s += str(x)
            x = x.right
        return s


l = List()
l.insert(ElementList(data=chr(14)))
l.insert(ElementList(25))
l.insert(ElementList(data=chr(34)))
print(l)
x = l.search(Key(34))
l.delete(x)
print(l)