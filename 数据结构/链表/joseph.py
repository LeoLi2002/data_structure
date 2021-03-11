import LinkList

def create():
   #创建41人节点
    dic = {}
    for i in range(1,42):
        linknode_val = {"num":i, "note":False}
        dic["P{}".format(i)] = LinkList.LinkList.LinkNode(linknode_val, None)
        if i == 16:
            dic["P{}".format(i)].val["note"] = True
        if i == 31:
            dic["P{}".format(i)].val["note"] = True

    #将链表连接，变成循环链表
    link = LinkList.LinkList()
    link.link_list()
    link.head = dic["P1"]
    cur = link.head
    for i in range(2,42):
        cur.next = dic["P{}".format(i)]
        print(cur.next, i)
        cur = cur.next
    dic["P41"].next = link.head
    print(dic["P41"].next)

   #进行问题模拟
    n = 41
    count = 1
    cur = link.head
    while n > 2:
        count += 1

        if count % 3 == 0:
           cur.next = cur.next.next
           count = 1
           n -=1

        cur = cur.next
    if n == 2:
        print(cur.val["note"], cur.next.val["note"])


create()


