class TwoWayLinkList:
    class ListNode:
        def __init__(self, val, pre, next):
            self.val = val
            self.pre = pre
            self.next = next


    def __init__(self):
        #初始化头节点
        self.head = self.ListNode(None, None, None)
        #初始化尾节点
        self.last = self.ListNode(None, None, None)
        #初始化元素个数
        self.length = 0


    #清空链表
    def clear(self):
        #清空头节点
        self.head.next = None
        #清空尾节点
        self.last.pre = None
        #链表长度初始化
        self.length = 0

    #获取链表长度
    def len(self):
        return self.length

    #判断链表是否为空
    def isEmpty(self):
        return self.length == 0


    #获取第一个元素
    def getFirst(self):
        if self.isEmpty:
            return self.head.next.val

    #获取最后一个元素
    def getLast(self):
        if self.isEmpty:
            return self.last.val

    #append方法
    def append(self, t):
        new = self.ListNode(t, None, None)
        #如果链表为空
        if self.isEmpty():
            new.pre = self.head
            self.last = new
            self.head.next = new
        #如果链表不为空
        else:
            oldLast = self.last
            new.pre = oldLast
            oldLast.next = new
            self.last = new

        self.length += 1

    #在i处插入元素t
    def insert(self, index, value):
        #找到i位置前的节点
        n = self.head
        for i in range(index):
            n = n.next
        #找到i位置的节点
        n_next = n.next
        #创建新的节点
        new = self.ListNode(value, n, n_next)
        #断开、连接链表
        n.next = new
        n_next.pre = new
        #链表长度+1
        self.length += 1

    #指定获取位置i处的元素
    def get(self, index):
        n = self.head.next
        for i in range(0,index):
            n = n.next
        return n.val

    #查找到元素t在链表中的位置
    def get_index(self, t):
        # 遍历链表
        n = self.head
        index = -1
        while n.next != None:
            n = n.next
            index += 1
            if n.val == t:
                return index
        return -1


    def tolist(self):
        ls = []
        n =self.head.next
        while n.next != None:
            ls.append(n.val)
            n = n.next
        else:
            ls.append(n.val)
        return ls


    #删除指定位置Index处的元素，如果output为True返回删除元素的值
    def remove(self, index,  output=True):
        # 找到i处前一个节点
        n = self.head
        for i in range(index - 1):
            n = n.next
        # 找到i位置的节点
        n_next = n.next
        # 找到i位置的下一个节点
        n_next_next = n_next.next
        # 前一个节点指向下一个节点
        n.next = n_next_next
        n_next_next.pre = n
        # 返回删除元素的值
        if output:
            print(n_next.val)
        # 元素个数-1
        self.length -= 1

if __name__ == "__main__":
    link_ls = TwoWayLinkList()
    link_ls.link_list()
    for i in range(1,10):
        link_ls.append(i)

    print(link_ls.tolist())
    link_ls.insert(2, 5)
    print(link_ls.tolist())