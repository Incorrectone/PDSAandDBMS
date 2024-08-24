class maxheap:
    def __init__(self):
        self.size = 0
        self.heap = []
    
    def insert(self, val):
        self.size += 1
        self.heap.append(val)
        self.heapify_up(self.size - 1)
    
    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)
    
    def delmax(self):
        if self.size == 0:
            return None
        
        max_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        
        self.heapify_down(0)
        return max_element
        
    def heapify_down(self, index):
        largest = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        
        if left_index < self.size and self.heap[left_index] > self.heap[largest]:
            largest = left_index
        if right_index < self.size and self.heap[right_index] > self.heap[largest]:
            largest = right_index
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)
        
        
    
        