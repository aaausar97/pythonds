class Stack:
    """Stack as a list"""

    def __init__(self):
        self._items = []
    
    def is_empty(self):
        # return len(self.items) == 0
        return not bool(self._items)
    
    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()
    
    def peek(self):
        return self._items[-1]
    
    def size(self):
        return len(self._items)
    
    def __str__(self):
        return str(self._items)

def main():
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push("dog")
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s)

def rev_string(string):
    s = Stack()
    for char in string:
        s.push(char)
    rev = []
    while not s.is_empty():
        rev.append(s.pop())
    return "".join(rev)

def check_par(string):
    s = Stack()
    for char in string:
        if char == '(':
            s.push(char)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
    return s.is_empty()


if __name__ == '__main__':
    main()
    print(rev_string('shaudy kash'))
    print(check_par('()'))
    print(check_par('(((()))'))