from Single_Linked_List import NonCircular as NC

class Queue:
    #constructor
    def __init__(self):
        self.queue_data=NC()
    @property
    def __len__(self):
        return self.queue_data._size
    def enqueue(self,element):
        return self.queue_data.insert_tail(element)
    def print(self):
        pass
    def dequeue(self):
        pass
    def front(self):
        pass
    def clear(self):
        pass
