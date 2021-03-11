class Stack:
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = Stack.Node(None, None)
        self.length = 0

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def push(self, val):
        #创建新节点
        new = Stack.Node(val, None)
        #首节点指向新节点
        old_next = self.head.next
        self.head.next = new
        #新节点指向原来的首节点
        new.next = old_next
        #元素个数+1
        self.length += 1

    def pop(self):
        #找到弹出节点
        pop_node = self.head.next
        pop_node_next = pop_node.next
        #将首节点指向下一个节点
        self.head.next = pop_node_next
        #元素个数-1
        self.length -= 1
        #返回弹出节点
        return pop_node