class Queue:
    class Node:
        def __init__(self, val, pre, next):
            self.val = val
            self.pre = pre
            self.next = next

    def __init__(self):
        self.head = Queue.Node(None, None, None)
        self.last = Queue.Node(None, None, None)
        self.head.next = self.last
        self.last.pre = self.head
        self.length = 0

    def size(self):
        return self.length

    def isEmpty(self):
        return  self.length == 0

    def enqueue(self, val):
        if self.isEmpty():
            self.last.val = val
            self.last.pre = self.head
            self.head.next = self.head
        else:
            new = Queue.Node(val, None, None)
            old_new = self.head.next
            self.head.next = new
            new.pre = self.head
            new.next = old_new
            old_new.pre = new

        self.length += 1



    def dequeue(self):
        if self.isEmpty():
            return -1
        last = self.last
        new_last = last.pre
        new_last.next = None
        self.last = new_last

        self.length -= 1

        return last.val


if __name__ == '__main__':
    queue = Queue()
    ls = [i for i in range(1,2)]
    print("test enqueue")
    for i in ls:
        queue.enqueue(i)
    for i in ls:
        de = queue.dequeue()
        print(de, ' ',de.val )
