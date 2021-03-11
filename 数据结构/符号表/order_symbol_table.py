class OrderSymbolTable:
    class Node:
        def __init__(self, key, value, next):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self):
        self.head = OrderSymbolTable.Node(None, None, None)
        self.length = 0

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def put(self, key, value):
        #定义两个变量，分别记录当前节点和当前节点的上一个节点
        curr = self.head.next
        pre = self.head
        while curr != None and key > curr.key:
            #变换当前节点和前一个结点
            pre = curr
            curr = curr.next
        #如果当前节点curr的键和要插入的key一样，则替换
        if curr != None and key == curr.key:
            curr.value = value
            return

        #如果当前节点的键和新插入的不一样，把新的节点插入到curr之前
        new_node = OrderSymbolTable.Node(key, value, curr)
        pre.next = new_node

        #元素的个数+1
        self.length += 1


    def delete(self, key):
        cur = self.head
        while cur.next != None:
            if cur.next.key == key:
                cur.next = cur.next.next
                self.length -= 1
                print("successfully, delete key {}".format(key))
                return
            cur = cur.next
        else:
            print("no key named {} was found".format(key))
            return

    def get(self, key):
        cur = self.head
        while cur.next != None:
            if cur.next.key == key:
                print(cur.next.value)
                return cur.next.value
            cur = cur.next
        else:
            print("no value named {} was found".format(key))
            return None



if __name__ == '__main__':
    dic = {1:11,
           2:22,
           4:44,
           3:33,
           5:55}
    table = OrderSymbolTable()
    for key, value in dic.items():
        table.put(key, value)
    for i in range(1,6):
        table.get(i)