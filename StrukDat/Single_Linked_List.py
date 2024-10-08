class Node :
    def __init__(self,data):
        self.data=data
        self.next=None

    @property
    def get_data(self):
        return self.data

class NonCircular:
    #CONSTRUCTOR
    def __init__(self):
        self.head = None
        self.tail = None
        self._size=0
    #METHOD
    def isempty(self):
        return self._size == 0
    def insert_head(self,data):
        new_node=Node(data)
        if self._size==0:
            self.head=new_node
            self.tail=new_node
        else :
            new_node.next=self.head
            self.head=new_node
        self._size+=1
        return True
    def print(self):
        if self._size==0:
            print("=== Linked List is empty ===")
        else:
            print(f"There are {self._size} nodes in Linked List : ")
            helper=self.head
            while helper is not None:
                print(helper.data,end=" ")
                helper=helper.next
            print()
    def insert_tail(self,data ):
        new_node=Node(data)
        if self._size==0:
            self.insert_head(new_node)
        else:
            self.tail.next=new_node
            self.tail=new_node
        self._size+=1
    # def insert_mid(self,data  ,position):
    #     if self._size==0:
    #         self.insert_head(data)
    #     else:
    #         if position-1==0:
    #             self.insert_head(data)
    #         elif position-1>=self._size:
    #             self.insert_tail(data)
    #         else:
    #             new_node=Node(data)
    #             helper=self.head
    #             for i in range(position-1):
    #                 helper=helper.next
    #             new_node.next=helper.next
    #             helper.next=new_node
    #             self._size+=1
    def find(self,value):
        if self._size==0:
            return False
        else:
            helper=self.head
            while helper.next is not None:
                if helper.data==value:
                    return True
                else:
                    helper=helper.next
            return False
    def update(self, old, new):
        if self._size==0:
            print("=== Linked List is Empty ===")
        else:
            helper=self.head
            while helper is not None:
                if helper.data==old:
                    helper.data=new
                    helper=helper.next
                else:
                    helper=helper.next
            print("=== Data telah diupdate ===")
    def delete_head(self):
        if self._size==0:
            return  False
        elif self._size==1:
            helper=self.head
            self.head=None
            self.tail=None
            del helper
            self._size-=1
        else:
            helper=self.head
            self.head=self.head.next
            del helper
            self._size-=1
            return self.head.data # memunculkan Top pada stack
    def delete_tail(self):
        if self._size==0:
            return False
        elif self._size==1:
            self.delete_head()
        else:
            helper=self.head
            while helper.next is not self.tail:
                helper=helper.next
            delete_=self.tail
            self.tail=helper
            self.tail.next=None
            del delete_
            self._size-=1
        return True
    # def delete_mid(self,position):
    #     if self._size==0:
    #         return False
    #     else:
    #         if position-1==0:
    #             self.delete_head()
    #         elif position>=self._size:
    #             self.delete_tail()
    #         else:
    #             delete_=self.head
    #             for i in range(position):
    #                 delete_=delete_.next
    #             helper=self.head
    #             for i in range(position-2):
    #                 helper=helper.next
    #             helper.next=delete_.next
    #             del delete_
    #             self._size-=1
    #         return True

class Circular:
    def __init__(self) -> None:
        self._head=None
        self._tail=None
        self._size=0
    def insert_head(self,data):
        new_node=Node(data)
        if self._size==0:
            self._head=new_node
            self._tail=new_node
            self._tail.next=self._head
        else:
            new_node.next=self._head
            self._head=new_node
            self._tail.next=self._head
        self._size+=1
    def insert_tail(self,data):
        new_node=Node(data)
        if self._size==0:
            self._head=new_node
            self._tail=new_node
            self._tail.next=self._head
        else:
            self._tail.next=new_node
            self._tail=new_node
            self._tail.next=self._head
        self._size+=1
    # def insert_mid(self,data,position):
    #     if self._size==0:
    #         self.insert_head(data)
    #     else:
    #         if position-1==0:
    #             self.insert_head(data)
    #         elif position>=self._size:
    #             pass

    def print(self):
        if self._size==0:
            print("=== Linked List is Empty ===")
        else:
            print(f"There are {self._size} nodes in Linked List : ")
            helper=self._head
            while helper is not None:
                print(helper.data,end=" ")
                helper=helper.next
                if helper==self._tail:
                    break
            print()