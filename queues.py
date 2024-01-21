class Queue:
    """Queue as a list"""

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)
    
    def size(self):
        return len(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)
    
    def dequeue(self):
        return self._items.pop()

    def __str__(self):
        return str(self._items)

def main():
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q)
    print(q.size())
    q.enqueue(80)
    print(q.dequeue())
    print(q.dequeue())
    print(q)

if __name__ == "__main__":
    main()



    
