import random

class Key:
    def __init__(self, value=None):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        try:
            self.__value = None if value is None else int(value)
        except:
            print("Blad")

    def __eq__(self, compared):
        if self.value == None or compared.value == None:
            return False
        return self.value == compared.value
    
    def __lt__(self, compared):
        if compared.value == None:
            return False
        if self.value == None:
            return True
        return self.value < compared.value 
    
    def __gt__(self, compared):
        if self.value == None:
            return False
        if compared.value == None:
            return True
        return self.value > compared.value
    
    def __le__(self, compared):
        if compared.value == None:
            return False
        if self.value == None:
            return True
        return self.value <= compared.value

    def __ge__(self, compared):
        if self.value == None:
            return False
        if compared.value == None:
            return True
        return self.value >= compared.value

    def __repr__(self):
        return str(self.value)

class Element:
    def __init__(self, data=None, s=13, h=43):
        self.__s = s
        self.__h = h
        self.__data = data
        if data == None:
            self.__data = ''.join([chr(random.randint(33, 125)) for i in range(4096)])
        self.__key = Key() 
        self.keygen()


    def keygen(self):
        k = 0
        for x in self.__data:
            k = (k*self.__s+ord(x))%self.__h
        self.__key.value = k

    
    @property
    def data(self):
        return self.__data


    @data.setter
    def data(self, d):
        self.__data = d
        self.keygen()


    def __repr__(self):
        return "<Element with key: {}>".format(hex(self.__key.value))


    @property
    def key(self):
        return self.__key


    def __eq__(self, e):
        if self.key != e.key:
            return False
        return self.data == e.data

    def __lt__(self, e):
        if self.key < e.key:
            return True
        if self.key > e.key:
            return False
        return self.data < e.data
