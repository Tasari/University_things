class Priority_Queue_List:
    def __init__(self):
        '''
        Tworzy liste ktorej bedzie uzywac jako kolejki
        '''
        self.queue=[]
        self.to_sort = False
    
    def is_empty(self):
        '''
        Sprawdza czy kolejka jest pusta
        '''
        return self.queue==[]
    
    def enqueue(self, item):
        '''
        Dodaje podany element do kolejki
        '''
        self.queue.append(item)
        self.to_sort = True
    
    def dequeue(self):
        '''
        Zdejmuje nawiekszy element z kolejki
        '''
        if self.is_empty():
            return None
        else:
            if self.to_sort:
                self.queue.sort(reverse=True)
                self.to_sort = False
            return self.queue.pop(0)
    def size(self):
        '''
        Zwraca ilosc elementow w kolejce
        '''
        return len(self.queue)

    def search(self, value):
        '''
        Szuka podanej wartosci i zwraca jej pozycje w kolejce
        '''
        return self.queue.index(value)

if __name__ == "__main__":
    queue = Priority_Queue_List()
    queue.enqueue(5)
    queue.enqueue(15)
    queue.enqueue(8)
    assert(queue.search(15) == 1)
    assert(queue.size() == 3)
    assert(queue.dequeue() == 15)
    assert(queue.dequeue() == 8)
    assert(queue.dequeue() == 5)
    assert(queue.dequeue() == None)
    assert(queue.is_empty() == True)