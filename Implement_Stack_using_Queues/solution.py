'''
Docstring for Implement_Stack_using_Queues.solution
'''

class Node:
    '''
    Docstring for Node
    '''
    def __init__(self, value):
        self.value = value
        self.next = None



class Queue:
    '''
    Docstring for Queue
    '''
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x):
        '''
        Docstring for push
        '''
        node = Node(x)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self):
        '''
        Docstring for pop
        '''
        node_val = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return node_val

    def peek(self):
        '''
        Docstring for peek
        '''
        return self.head.value

    def empty(self):
        '''
        Docstring for empty
        '''
        return not self.head




class MyStack:
    '''
    Docstring for MyStack
    '''

    def __init__(self):
        self.in_ = Queue()
        self.out_ = Queue()


    def push(self, x: int) -> None:
        '''
        Docstring for push
        '''
        self.out_.push(x)
        while not self.in_.empty():
            self.out_.push(self.in_.pop())
        self.in_, self.out_ = self.out_, self.in_


    def pop(self) -> int:
        '''
        Docstring for pop
        '''
        return self.in_.pop()


    def top(self) -> int:
        '''
        Docstring for top
        '''
        return self.in_.peek()


    def empty(self) -> bool:
        '''
        Docstring for empty
        '''
        return self.in_.empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
