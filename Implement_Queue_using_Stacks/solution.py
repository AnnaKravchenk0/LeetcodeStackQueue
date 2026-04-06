class Node:
    '''
    Docstring for Node
    '''
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:
    '''
    Docstring for MyQueue
    '''

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        '''
        Docstring for push
        '''
        node = Node(x)
        if not self.head:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node


    def pop(self) -> int:
        '''
        Docstring for pop
        '''
        node = self.head
        self.head = self.head.next

        if not self.head:
            self.tail = None
        return node.value

    def peek(self) -> int:
        '''
        Docstring for peek
        '''
        return self.head.value

    def empty(self) -> bool:
        '''
        Docstring for empty
        '''
        if self.head:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# x = 5
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# print(param_2)
# print(param_3)
# print(param_4)
