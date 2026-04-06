'''
Docstring for Maximum_Frequency_Stack.solution
'''
from collections import deque, defaultdict

class FreqStack:
    '''
    Docstring for FreqStack
    '''

    def __init__(self):
        self.freq = defaultdict(int)
        self.num = deque()
        self.max_freq = 0

    def push(self, val: int) -> None:
        '''
        Docstring for push
        '''
        self.freq[val] += 1
        self.num.append(val)
        self.max_freq = max(self.freq[val], self.max_freq)


    def pop(self) -> int:
        '''
        Docstring for pop
        '''
        temp = deque()

        while self.num:
            el = self.num.pop()
            if self.max_freq != self.freq[el]:
                temp.append(el)
            else:
                target = el
                self.freq[target] -= 1
                break

        while temp:
            el = temp.pop()
            self.num.append(el)

        if self.max_freq not in self.freq.values():
            self.max_freq -= 1

        return target



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
