MAX_QUEUE_SIZE = 2000
import Element

class Queue:
    def __init__(self, size=None):
        try:
            x = int(size)
            assert x < MAX_QUEUE_SIZE
        except:
            x = MAX_QUEUE_SIZE
        finally:
            if x < 0:
                print("Biorę bezwzględną z podanej ujemnej wartości")
                x = abs(size)
        self.__size = x
        self.__queue = [None for i in range(x)]
        self.__head = 0
        self.__tail = 0

    @property
    def empty(self):
        return self.__head == self.__tail

    @property
    def full(self):
        return ((self.__tail+1)%self.__size) == self.__head


    def enqueue(self, e):
        if self.full:
            print("Kolejka jest pełna")
            return False
        else:
            self.__queue[self.__tail] = e
            self.__tail = ((self.__tail + 1) % self.__size)
            return True



    def dequeue(self):
        if self.empty:
            print("Kolejka jest pusta")
        else:
            x = self.__head
            self.__head = (self.__head +1)%self.__size
            return self.__queue[x]


    @property
    def items(self):
        h = self.__head
        t = self.__tail
        if h <=t:
            return self.__queue[h:t]
        return self.__queue[h:] + self.__queue[:t]

    def __repr__(self):
        return str(self.items)

x = Queue(6)
x.enqueue(Element.Element(chr(44)))
x.enqueue(Element.Element(chr(45)))                                                                                                                                                                                                                                                        
x.enqueue(Element.Element(chr(46)))
x.enqueue(Element.Element(chr(47)))
x.enqueue(Element.Element(chr(48)))
x.dequeue()
x.dequeue()
print(x)
x.enqueue(Element.Element(chr(49)))
x.enqueue(Element.Element(chr(50)))
print(x)