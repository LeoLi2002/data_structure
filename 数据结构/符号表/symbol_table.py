class SymbolTable:
    class Node:
        def __init__(self, key, value, next):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self):
        self.head = SymbolTable.Node(None, None, None)
        self.length = 0

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def put(self, key, value):
        #符号表中已经存在键为key的键值对，那么只需要找到该节点，然后替换为key即可
        cur = self.head
        while cur.next != None:
            if cur.key == key:
                cur.value = value
                break
            cur = cur.next
        #如果符号表中没有键为key的键值对，那么创建新的节点，将键值对存入其中
        else:
            cur = SymbolTable.Node(key, value, None)
            ole_new = self.head
            self.head.next = cur
            cur.next = ole_new

        self.length += 1
        print("{0}:{1}".format(cur.key, cur.value))


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



