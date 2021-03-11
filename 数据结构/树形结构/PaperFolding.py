import BInaryTree
import queue
class PaperFolding:
    def __init__(self, N):
        self.N = N
        self.tree = BInaryTree.BinaryTree()

    def main(self):
        #创造二叉树
        self.folding_process()
        #遍历二叉树
        self.midErgodic()
        print(self.ls)


    def folding_process(self):
        if self.tree.root.value == None:
            self.tree.root.value = "down"
            self.N -= 1

        while self.N != 0:
            self.__layerEgrodic(self.tree.root)
            self.N -= 1

    def __insert_node(self, curr):
        left_node = BInaryTree.BinaryTree.Node(None, "down", None, None)
        right_node = BInaryTree.BinaryTree.Node(None, "up", None, None)
        curr.left = left_node
        curr.right = right_node

    def __layerEgrodic(self, curr):
        self.queue = queue.Queue()
        self.queue.enqueue(self.tree.root)
        #遍历循环队列
        while self.queue.size() != 0:
            #从队列中弹出一个节点
            temp = self.queue.dequeue()
            #如果有左子节点，就把左子节点放入队列中
            if temp.left != None:
                self.queue.enqueue(temp.left)
            #如果有右子节点，就把右子节点放入队列中
            if temp.right != None:
                self.queue.enqueue(temp.right)
            #如果啥都没有，向当前节点添加结点
            if temp.left == None and temp.right == None:
                self.__insert_node(temp)






# 中序遍历
    def midErgodic(self):
        self.ls = []
        self.add_keys_midErgodic(self.tree.root)
        return self.ls

    # 使用中序遍历，把指定的子树中所有键放到ls中
    def add_keys_midErgodic(self, curr_root):
        if curr_root.left != None:
            self.add_keys_midErgodic(curr_root.left)

        self.ls.append(curr_root.value)

        if curr_root.right != None:
            self.add_keys_midErgodic(curr_root.right)


if __name__ == '__main__':
    test = PaperFolding(2)
    test.main()
