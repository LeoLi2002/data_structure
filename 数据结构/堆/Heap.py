"""
剩余问题：并不按顺序
分析：由堆的定义可以得出，堆的建立不能保证从大到小的，所以要进行堆排序

"""
class Heap:
    def __init__(self):
        self.heap = [None]
        self.size = 0

    #判断索引处i处的元素是否小于索引j处的元素
    def isless(self, i, j):
        return self.heap[i] < self.heap[j]

    #交换堆中i处的值和j处的值
    def exch(self,i ,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    #删除对中最大元素，并返回这个元素
    def delMax(self):
        max = self.heap[1]
        #首先将最大元素与最后一个元素交换，之后删除最后一个元素
        self.exch(1, self.size)
        self.heap.remove(self.heap[self.size])
        #采用下沉算法，将换上去的最后一个元素放到合适位置
        self.size -= 1
        self.sink(1)

        return max

    #往堆中插入一个元素
    def insert(self, value):
        if self.size == 0:
            self.heap.append(value)
            self.size += 1
            return
        self.heap.append(value)
        self.size += 1
        self.swim(self.size)

    #使用上浮算法，使索引k处的元素能处在堆中一个正确的位置
    def swim(self, k):
        cur_index = k
        while cur_index > 1:
            if self.heap[cur_index] > self.heap[cur_index//2]:
                self.exch(cur_index, cur_index//2)
                cur_index = cur_index//2
            else:
                break



    #使用下沉算法，使索引k处的元素处在堆中一个正确的位置
    def sink(self,k):
        cur_index = k
        while cur_index*2 <= self.size:
            if cur_index*2 + 1 > self.size:
                bigger = cur_index * 2
            elif self.heap[cur_index*2] < self.heap[cur_index*2+1]:
                bigger = cur_index * 2 + 1
            else:
                bigger = cur_index * 2

            if self.isless(cur_index, bigger):
                self.exch(cur_index, bigger)
                cur_index = bigger
            else:
                break








if __name__ == '__main__':
    #创建堆对象
    heap = Heap()
    #往堆中存入字符串数据
    for i in "abcdefg":
        heap.insert(i)
    print(heap.heap)
    #通过循环从堆中删除数据
    while heap.size > 0:
        print(heap.delMax())
    #