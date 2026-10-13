class MyQueue:

    def __init__(self):
        self.MyQueue = []

    def push(self, x: int) -> None:
        self.MyQueue.append(x)

    def pop(self) -> int:
        output = self.MyQueue.pop(0)
        return output

    def peek(self) -> int:
        output = self.MyQueue[0]
        return output
        
    def empty(self) -> bool:
        if len(self.MyQueue)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()