class BinaryTree:
    class Node:
        def __init__(self, key, value, left, right):
            self.key = key
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = BinaryTree.Node(None, None, None, None)
        self.size = 0

    def put(self, key, value):
        if self.size == 0:
            self.root.key = key
            self.root.value = value
            self.size += 1
            return
        else:
            self.sub_put(self.root, key, value)
        self.size += 1

    def sub_put(self, sub_root, key, value):

        cur_root = sub_root
        if cur_root.key > key:
            if cur_root.left != None:
                cur_root = cur_root.left
                self.sub_put(cur_root, key, value)
            else:
                new = BinaryTree.Node(key, value, None, None)
                cur_root.left = new
        elif cur_root.key < key:
            if cur_root.right != None:
                cur_root = cur_root.right
                self.sub_put(cur_root, key, value)
            else:
                new = BinaryTree.Node(key, value, None, None)
                cur_root.right = new
        elif cur_root.key == key:
            cur_root.value = value
            self.size -= 1




    def get(self, key):
        if self.size == 0 :
            return False

        return self.sub_get(self.root, key)

    def sub_get(self, sub_root, key):

        cur_root = sub_root
        if cur_root.key > key:
            if sub_root.left != None:
                cur_root = cur_root.left
                return self.sub_get(cur_root, key)
            else:
                print("not found")
                return False
        elif cur_root.key < key:
            if sub_root.right != None:
                cur_root = cur_root.right
                return self.sub_get(cur_root, key)
            else:
                print("not found")
                return False
        elif cur_root.key == key:
            return cur_root.value


    def delete(self, key):
        if self.size == 0:
            return False

        return self.sub_delete(self.root, key)

    def sub_delete(self, sub_root,  key):
         if sub_root == None:
             print("not found")
             return

         #????????????????????????
         curr_node = sub_root
         if curr_node.key > key:
             curr_node = curr_node.left
             return self.sub_delete(curr_node, key)
         if curr_node.key < key:
             curr_node = curr_node.right
             return self.sub_delete(curr_node, key)
         if curr_node.key == key:
             if curr_node.left == None:
                 new = curr_node.right
             elif curr_node.right == None:
                 new = curr_node.left
             else:
                 #?????????????????????
                 new = curr_node
                 while new != None:
                     if new.left.left != None:
                         new = new.left
                     elif new.left.left == None:
                         pin = new.left
                         new.left = None
                         new = pin.left

         # ???????????????????????????
         father_node = self.root
         while father_node != None:
                if father_node.key == key:
                     left = father_node.left
                     right = father_node.right
                     new.left = left
                     new.right = right
                     self.root = new
                     self.size -= 1
                     return
                elif father_node.key > key:
                     if father_node.left.key == key:
                         break
                     else:
                         father_node = father_node.left
                elif father_node.key < key:
                     if father_node.right.key == key:
                         break
                     else:
                        father_node = father_node.right

         #??????????????????
         left = curr_node.left
         right = curr_node.right

         if new == left:
             father_node.left = new
         elif new == right:
              father_node.right = new
         else:
             new.left = left
             new.right = right
             if father_node.key > key:
                 father_node.left = new
             else:
                 father_node.right = new

         self.size -= 1


    #??????????????????????????????
    def key_min(self):
        return self.sub_key_min(self.root).key


    #?????????????????????????????????????????????
    def sub_key_min(self, sub_root):
        min_node = sub_root
        while min_node.left != None:
            min_node = min_node.left
        return min_node


    #??????????????????????????????
    def key_max(self):
        return self.sub_key_max(self.root).key


    # ?????????????????????????????????????????????
    def sub_key_max(self, sub_root):
        max_node = sub_root
        while max_node.right != None:
            #print(max_node.key)
            max_node = max_node.right
        return max_node


    #????????????
    def preErgodic(self):
        self.ls = []
        self.add_keys_preErgodic(self.root)
        return self.ls


    #??????????????????????????????????????????????????????keys?????????
    def add_keys_preErgodic(self, curr_root ):
        if curr_root == None:
            return
        #???curr_root????????????key??????????????????
        self.ls.append(curr_root.key)
        #?????????????????????
        if curr_root.left != None:
            self.add_keys_preErgodic(curr_root.left)

        #?????????????????????
        if curr_root.right != None:
            self.add_keys_preErgodic(curr_root.right)




    #????????????
    def midErgodic(self):
        self.ls = []
        self.add_keys_midErgodic(self.root)
        return self.ls

    #?????????????????????????????????????????????????????????ls???
    def add_keys_midErgodic(self, curr_root):
        if curr_root.left != None:
            self.add_keys_midErgodic(curr_root.left)

        self.ls.append(curr_root.key)

        if curr_root.right != None:
            self.add_keys_midErgodic(curr_root.right)


    #????????????
    def afterEgrodic(self):
        self.ls = []
        return self.ls

    #??????????????????????????????????????????????????????ls???
    def add_keys_afterEgrodic(self, curr_root):
        if curr_root.left != None:
            self.add_keys_midErgodic(curr_root.left)



        if curr_root.right != None:
            self.add_keys_midErgodic(curr_root.right)

        self.ls.append(curr_root.key)


    #????????????
    def layerEgrodic(self):
        self.ls = []
        import queue
        queue = queue.Queue()
        queue.enqueue(self.root)
        while queue.size() != 0:
            curr_node = queue.dequeue()
            self.ls.append(curr_node.key)
            if curr_node.left != None: queue.enqueue(curr_node.left)
            if curr_node.right != None: queue.enqueue(curr_node.right)
        return self.ls



    #??????????????????????????????
    def maxDepth(self):

        return self.maxSubDepth(self.root)


    #?????????????????????????????????
    def maxSubDepth(self, sub_root):
        if sub_root == None:
            return 0

        self.__max = 0
        self.__max_l = 0
        self.__max_r = 0

        #??????????????????????????????
        if sub_root.left != None:
            self.__max_l = self.maxSubDepth(sub_root.left)

        #??????????????????????????????
        if sub_root.right != None:
            self.__max_r = self.maxSubDepth(sub_root.right)
        #????????????????????????+1
        self.__max = max(self.__max_l, self.__max_r) + 1
        return self.__max


















if __name__ == '__main__':
    #????????????????????????
    """
    tree = BinaryTree()
    dic = {}
    for i in range(10):
        dic[i] = i*10

    #??????????????????
    for key, value in dic.items():
        tree.put(key, value)

    #print(tree.root.key)

    #??????????????????
    for key in range(9,-1,-1):
        print(tree.get(key))
    """
    import random
    test_list = [random.randint(1,2000) for i in range(50)]
    dic = {}
    for i in test_list:
        dic[i] = "{}".format(i)*2

    tree = BinaryTree()
    for key, value in dic.items():
        tree.put(key, value)


    #??????????????????
    #tree.delete(5)
    #tree.get(5)


    #???????????????
    print(tree.key_min())

    #?????????????????????
    print(tree.key_max())

    #??????????????????
    print("-------------------------------------------------------------")
    print(tree.size)
    tree.layerEgrodic()
    print(tree.ls)


    #????????????
    depth = tree.maxDepth()
    print(depth)


