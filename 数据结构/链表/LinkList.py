class LinkList:
    class LinkNode:
        def __init__(self, x, next):
            self.val = x
            self.next = next


    #构造方法
    def __init__(self):
        #初始化头节点
        self.head = self.LinkNode(None, None)
        #初始化元素个数
        self.length = 0

    #清空列表
    def clear(self):
        self.head.next = None
        self.length = 0

    #获取链表的长度
    def len(self):
        return self.length

    #判断链表是否为0
    def isEmpty(self):
        return self.length == 0

    #获取指定位置i的元素
    def get(self, i):
        #通过循环从头节点开始往后找，一次找0次
        n = self.head.next
        for j in range(i):
            n = n.next
        return n

    #append方法
    def append(self, t):
        #找到当前最后一个节点
        n = self.head
        while n.next != None:
            n = n.next
        #创建新节点
        new = self.LinkNode(t, None)
        n.next = new
        #长度+1
        self.length += 1

    #在i位置添加一个元素
    def insert(self, index, value):
        #找到i位置前的节点
        n = self.head
        for i in range(index):
            n = n.next
        #找到i位置的节点
        n_next = n.next
        #创建新的节点，并且新节点指向i位置的节点
        new = self.LinkNode(value, n_next)
        #原来i位置的前一个结点指向新节点
        n.next = new

        #元素个数+1
        self.length += 1

    #删除指定位置Index处的元素，如果output为True返回删除元素的值
    def remove(self, index, output=True):
        #找到i处前一个节点
        n = self.head
        for i in range(index-1):
            n = n.next
        #找到i位置的节点
        n_next = n.next
        #找到i位置的下一个节点
        n_next_next = n_next.next
        #前一个节点指向下一个节点
        n.next = n_next_next
        #返回删除元素的值
        if output:
            print(n_next.val)
        #元素个数-1
        self.length -= 1


    #查找元素t第一次出现的位置
    def get_index(self, t):
        #遍历链表
        n = self.head
        index = -1
        while n.next != None:
            n = n.next
            index += 1
            if n.val == t:
                return index
        return -1

    #单项链表转化成列表
    def tolist(self):
        ls = []
        #遍历列表，以此把元素中的val值添加到ls中
        n = self.head.next
        while n.next != None:
            ls.append(n.val)
            n = n.next
        else:
            ls.append(n.val)
        return ls

    #反转整个链表
    def reverse(self):
        #判断当前链表是否为空链表，如果是，则结束运行；如果不是，则调用重载的反转方法
        if self.isEmpty():
            return
        self.reverse2(self.head.next)
        print("reverse2开始调用")



    #指定反转
    def reverse2(self, curr):
        if curr.next == None:
            self.head.next = curr
            print("reverse2开始回调")
            return curr
        pre = self.reverse2(curr.next)
        pre.next = curr
        curr.next = None
        print("reverse2调用一次")
        return curr





if __name__ == "__main__":
    link_ls = LinkList()
    link_ls.link_list()
    for i in range(1,10):
        link_ls.append(i)
    print(link_ls.tolist())
    link_ls.reverse()
    print(link_ls.tolist())










