class Node:
    def __init__(self, v = None):
        self.value = None
        self.next = None
        return
    
    def isempty(self):
        if self.value == None:
            return True
        else:
            return False
    
    def append(self, v):
        if self.isempty():
            self.value = v
        elif self.next == None:
            self.next = Node(v)
        else:
            self.next.append(v)
        return
    
    def insert(self, v):
        if self.isempty():
            self.value = v
        new_node = Node(v)        
        (self.value, new_node.value) = (new_node.value, self.value)
        (self.next, new_node.next) = (new_node, self.next)
        return 
    
    def delete(self, v):
        if self.isempty():
            return
        
        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
        return
    
    
def EvaluateExpression(srt):
    expression = srt.split()
    stack = []
    opt = ['+', '-', '*', '/', '**']
    for i in expression:
        if i not in opt:
            stack.append(i)
        else:
            a = str(eval(stack[-2] + i + stack[-1]))
            stack.pop()
            stack.pop()
            stack.append(a)
    
    return stack[0]

print(EvaluateExpression('1 2 3 2 3 ** ** * + 6 2 / 4 * -'))


def reverse(root):
    prev = None
    current = root
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return
        


        
    