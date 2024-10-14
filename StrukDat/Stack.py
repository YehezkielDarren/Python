from Single_Linked_List import NonCircular

class Stack_List:
    # Constructor
    def __init__(self,):
        self._stack_data=[]
        self._top=None
        self._size=0
    # Method
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, item):
        self._stack_data.append(item)
        self._top=self._stack_data[-1]
        self._size+=1
        return True

    def pop_stack(self):
        if self.is_empty():
            return False
        else:
            if self._size == 0:
                self._top=None
                data=self._stack_data.pop()
                self._size-=1
            else:
                self._top=self._stack_data[-2]
                data=self._stack_data.pop()
                self._size-=1
            return data

    def top(self):
        if self.is_empty():
            return None
        else:
            return self._stack_data[-1]

    def clear(self):
        self._stack_data.clear()
        self._size=0
        return True

    @property
    def stack_data(self):
        return self._stack_data


class Stack_SLLNC:
    def __init__(self):
        self._stack_data=NonCircular()

    @property
    def stack_data(self):
        return self._stack_data

    def push(self, item):
        self._stack_data.insert_head(item)
    def pop(self):
        data=self._stack_data.delete_head()
        return data
    def clear(self):
        if self._stack_data.isempty():
            return "Stack was empty"
        while not self._stack_data.isempty():
            self._stack_data.delete_head()
        return "Stack has empty"
