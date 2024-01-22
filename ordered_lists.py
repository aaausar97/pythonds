from linked_lists import Node
    
class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        current = self.head
        prev = None
        temp = Node(item)

        while current is not None and current.data < item:
            prev = current
            current = current.next
        
        if prev is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            prev.next = temp
        

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count
    
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next
        
        if current is None:
            raise ValueError(f'{item} is not in the list')
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
    
    def append(self, item):
        temp = Node(item)
        current = self.head
        previous = None

        while current is not None:
            previous = current
            current = current.next
        
        previous.next = temp
    
    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        return -1
    
    def insert(self, pos, item):
        current = self.head
        prev = None
        index = 0
        while current is not None:
            if index == pos:
                temp = Node(item)
                prev.next = temp
                temp.next = current
            prev = current
            current = current.next
            index += 1
    
    ## todo: pop() and pop(pos) ##

    def __str__(self):
        nodes=[]
        current = self.head
        while current is not None:
            nodes.append(current._data)
            current = current.next
        return str(nodes)