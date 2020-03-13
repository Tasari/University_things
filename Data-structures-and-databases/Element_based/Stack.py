MAX_STACK_SIZE = 2000

import Element
class Stack:
    def __init__(self, size = MAX_STACK_SIZE):
        if size > MAX_STACK_SIZE:
            size = MAX_STACK_SIZE
        self.__size = size
        self.__stack = [None for x in range(self.__size)]
        self.__top = -1


    @property
    def empty(self):
        return self.__top == -1
    
    
    @property
    def full(self):
        return  self.__top == self.__size - 1

    
    def push(self, data):
        if not self.full:
            self.__top += 1
            self.__stack[self.__top] = data
            return True
        else:
            print('Stos pełny')
            return False

    def pop(self):
        if not self.empty:
            x = self.__stack[self.__top]
            self.__top -= 1
            return x
        else:
            print("Stos pusty")

    def __repr__(self):
        return '\n'.join(list(map(str, self.__stack[self.__top::-1])))
        
x = Stack()
x.push(Element.Element())
print("Print Stack")
print(x)
x.push(Element.Element())
print("Print Stack 2")
print(x)
print("Pops")
print(x.pop())
print(x.pop())
x.pop()
