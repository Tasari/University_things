class Node:
    def __init__(self, key):
        '''
        Przypisuje wartosc wezlowi i okresla ze nie ma przed nim ani za nim zadnego elementu
        '''
        self.prev = None
        self.key = key
        self.next = None

    def set_next(self, Node):
        '''
        Podlacza podany wezel jako nastepca wezla na ktorym stosujemy metode
        '''
        self.next = Node
    
    def set_prev(self, Node):
        '''
        Podlacza podany wezel jako poprzednik wezla na ktorym stosujemy metode
        '''
        self.prev = Node

    def set_key(self, new_key):
        '''
        Zmienia wartosc wezla na podana
        '''
        self.key = new_key

    def get_next(self):
        '''
        Zwraca nastepce wezla 
        '''
        return self.next
    
    def get_prev(self):
        '''
        Zwraca poprzednika wezla
        '''
        return self.prev

    def get_key(self):
        '''
        Zwraca wartosc wezla
        '''
        return self.key

class Node_based_priority_queue:
    def __init__(self):
        '''
        Tworzy kolejke w ktorej glowa jest pusty wezel
        '''
        self.head = Node(None)
    
    def get_head(self):
        '''
        Zwraca wezel bedacy glowa
        '''
        return self.head
    
    def set_head(self, Node):
        '''
        Ustawia podany wezel jako glowe
        '''
        self.head = Node

    def is_empty(self):
        '''
        Sprawdza czy wezel bedacy glowa jest wezlem pustym
        '''
        return self.get_head().get_key() == None

    def enqueue(self, val):
        '''
        Dodaje wezel z podana wartoscia do kolejki w odpowiednim miejscu
        porownujac wartosc przypisana do wezla
        I jezeli jest on najwiekszy ustawia go jako glowe
        '''
        node = Node(val)
        actual = self.get_head()
        while 1:
            if actual.get_key() == None:
                key = 0
            else:
                key = actual.get_key()
            if key > node.get_key():
                actual = actual.get_next()
            else:
                node.set_next(actual)
                node.set_prev(actual.get_prev())
                if actual.get_prev() == None:
                    self.set_head(node)

                else:
                    actual.get_prev().set_next(node)
                actual.set_prev(node)
                break
    def dequeue(self):
        '''
        Jesli kolejka nie jest pusta to zdejmuje wezel z najwyzsza wartoscia z kolejki, 
        i zmienia nastepce swojego poprzednika na swojego nastepce,
        a poprzednika swojego nastepcy na swojego poprzednika,
        po czym zwraca ten wezel  
        '''
        if not self.is_empty():
            maximum = self.get_head()
            new_next = maximum.get_next()
            self.set_head(new_next)
            return maximum 
        else:
            return Node(None)
    
    def size(self):
        '''
        Zwraca ilosc elementow w kolejce
        '''
        size = 1
        actual = self.get_head()
        while actual.get_next().get_key() != None:
            actual = actual.next
            size += 1
        return size
    
    def search(self, key):
        place = 0
        actual = self.get_head()
        if actual.get_key() == key:
            return place
        elif actual.get_key() == None:
            return None
        else:
            actual = actual.get_next()
            place += 1

if __name__ == "__main__":
    queue = Node_based_priority_queue()
    queue.enqueue(5)
    queue.enqueue(15)
    queue.enqueue(8)
    assert(queue.search(15) == 0)
    assert(queue.size() == 3)
    assert(queue.dequeue().get_key() == 15)
    assert(queue.dequeue().get_key() == 8)
    assert(queue.dequeue().get_key() == 5)
    assert(queue.dequeue().get_key() == None)
    assert(queue.is_empty() == True)