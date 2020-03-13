from Element import Element

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

a = ElementList()
b = ElementList()
a.right = b
print(a)
print(b)
print(a.right is b)