'''
Docstring for Implement_Queue_using_Stacks.solution
'''
class Node:
    '''
    Docstring for Node
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    '''
    Docstring for Stack
    '''
    def __init__(self):
        self.top = None

    def push(self, value):
        '''
        Docstring for push
        '''
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        '''
        Docstring for pop
        '''
        node_val = self.top.value
        self.top = self.top.next
        return node_val


    def peek(self):
        '''
        Docstring for peek
        '''
        return self.top.value

    def empty(self):
        '''
        Docstring for empty
        '''
        return not self.top




class MyQueue:
    '''
    Docstring for MyQueue
    '''

    def __init__(self):
        self.in_ = Stack()
        self.out_ = Stack()

    def push(self, x: int) -> None:
        '''
        Docstring for push
        '''
        self.in_.push(x)


    def pop(self) -> int:
        '''
        Docstring for pop
        '''
        if self.out_.empty():
            while not self.in_.empty():
                self.out_.push(self.in_.pop())


        return self.out_.pop()

    def peek(self) -> int:
        '''
        Docstring for peek
        '''
        if self.out_.empty():
            while not self.in_.empty():
                self.out_.push(self.in_.pop())


        return self.out_.peek()

    def empty(self) -> bool:
        '''
        Docstring for empty
        '''
        return self.in_.empty() and self.out_.empty()


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
