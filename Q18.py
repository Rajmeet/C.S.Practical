class Stack:
    def __init__(self, condition = False):
        self.stack = []
        self.ring = condition

    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False
    def push(self, item, temp):
        if self.ring:
            while item < self.peek():
                temp.stack.append(self.pop())
            else:
                self.stack.append(item)
        else:
            self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return False
    
    def peek(self):
        if not self.isEmpty():
            return(self.stack[-1])
        else:
            return 0

    def getStack(self):
        return self.stack

ring = Stack(True)
temp = Stack()

while True:
    try: 
        ring.push(int(input("Enter number: ")), temp)
        print("Ring Tower: ", ring.stack)
    except:
        print("done")
        break