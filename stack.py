class stacks:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return self.stack
    def push(self,data):
        return self.stack.append(data)
    def pop(self):
        data=self.stack[-1]
        return self.stack.remove(data)
    def pick(self):
        data2=self.stack[-1]
        return data2
    def seize(self):
        return len(self.stack)
# # stack=stacks()
# # stack.push(1)
# # stack.push(2)
# # stack.push(3)
# # print(stack.pop())
#
# print(stack.pick())
