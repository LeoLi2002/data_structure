import Heap
class HeapSort:
    def __init__(self):
        pass

    #教学中因为使用的是java，python有些功能不用编辑方法，已省略

    def create_heap(self, obj):
        self.obj = Heap.Heap()
        for i in obj:
            self.obj.insert(i)

    #进行排序，首尾互换后，沉默尾，下沉首
    def sort(self):
        end = self.obj.size
        while  end > 1:
            print(end)
            print(self.obj.heap)
            #首尾互换
            self.obj.heap[1], self.obj.heap[end] = self.obj.heap[end], self.obj.heap[1]
            # 沉默尾
            end -= 1
            #下沉
            self.__sink(1, end)




    def __sink(self, start, end):
        curr = start
        end -= 1
        while curr <= end:
            #先找出curr子结点中较大值
            try:
                if self.obj.heap[curr*2] < self.obj.heap[curr*2+1] and curr*2+1 <= end:
                    bigger = curr*2+1
                else:
                    bigger = curr*2
            except:
                try:
                    bigger = curr*2
                except:
                    break
            #用较大值与curr值作比较，判断是否交换
            if self.obj.heap[curr] < self.obj.heap[bigger]:
                self.obj.heap[curr], self.obj.heap[bigger] = self.obj.heap[bigger], self.obj.heap[curr]
                #如果交换，继续下沉
                end -= 1
            #如果不叫唤，break
            else:
                break

if __name__ == '__main__':
    #创建待排序的列表
    ls = [i for i in "abcdefg"]
    #进行排序
    process = HeapSort()
    process.create_heap(ls)
    process.sort()
    #展示排序后的堆
    print(process.obj.heap)