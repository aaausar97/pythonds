class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        return self._data
    
    def set_data(self, node_data):
        self._data = node_data
    
    data = property(get_data, set_data)

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node

    next = property(get_next, set_next)

    def __str__(self):
        return str(self._data)
    
class UnorderedList:
    
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

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
      
    def __str__(self):
        nodes=[]
        current = self.head
        while current is not None:
            nodes.append(current._data)
            current = current.next
        return str(nodes)
        
        




def main():
    my_list = UnorderedList()
    my_list.add(14)
    my_list.add(15)
    my_list.add(10)
    print(my_list.is_empty())
    print(my_list.size())
    my_list.add(16)
    print(my_list.search(17))
    print(my_list.search(14))
    print(my_list)
    my_list.remove(14)
    print(my_list.search(14))
    my_list.add(12)
    my_list.append(13)
    print(my_list)


if __name__ == '__main__':
    main()