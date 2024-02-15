class Heap:

    def __init__(self, max_size) -> None:
        self.heap = [0 for _ in range(max_size)]
        self.size = 0

    
    def compare(self,a, b) -> bool:
        return b > a
    
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
    
    def insert(self, val: int) -> None:
        self.size += 1

        #Insert value at the end of the heap
        self.heap[self.size] = val

        #Move the value to its actual path
        idx = self.size

        while idx>1:
            parent = idx//2
            if self.compare(self.heap[parent], self.heap[idx]):
                self.swap(parent, idx)
                idx = parent
            
            else:
                break
    
    def heapify(self, pos) -> None:
        idx = pos

        while 2*idx <= self.size:
            g = idx
            left = 2*idx
            right = 2*idx + 1

            if self.compare(self.heap[idx], self.heap[left]):
                g = left

            if right <= self.size and self.compare(self.heap[g], self.heap[right]):
                g = right
            
            if g == idx:
                break

            self.swap(g, idx)
            idx = g
        
    def remove(self) -> int:
        self.swap(1,self.size)
        self.size -= 1
        self.heapify(1)

        return self.heap[self.size+1]

    def print(self) -> None:
        print('Heap is: ')
        for x in range(1,self.size+1):
            print(self.heap[x])


if __name__ == '__main__':
    heap = Heap(10)
    heap.insert(10)
    heap.insert(20)
    heap.insert(30)
    heap.insert(25)
    heap.insert(35)

    heap.print()

    print('Greatest Element is : ',heap.remove())

    heap.print()

