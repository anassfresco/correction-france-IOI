class nod:
    def __init__(self,data):
        self.data=data
        self.next_node=None
class linked_list:
    def __init__(self):
        self.head=None
        self.seize=0
    def insertstart(self,data):
        self.seize=self.seize+1
        newnode=nod(data)
        if not self.head:
            self.head=newnode
        else:
            newnode.next_node=self.head
            self.head=newnode
    def seize(self):
        return self.seize
    def seize2(self):
        mask=0
        actualnode=self.head
        while actualnode is not None:
            mask+=1
            actualnode=actualnode.next_node
        return mask
    def insert_end(self,data):
        self.seize+=1
        newnode=nod(data)
        actualnode=self.head
        while actualnode.next_node is not None:
            actualnode=actualnode.next_node
        actualnode.next_node=newnode
    def remove(self,data):
        self.seize -= 1
        if self.head is None:
            return

        current_data=self.head
        previous_data=None
        while current_data.data!=data:
            previous_data=current_data
            current_data=current_data.next_node
        if previous_data==None:
            self.head=current_data.next_node
        else:
            previous_data.next_node=current_data.next_node
    def traverse_lisa(self):
        actual=self.head
        while actual is not None:
            print(actual.data)
            actual=actual.next_node
    def somme_list(self):
        s=0
        b=[]
        actual_node=self.head
        while actual_node is not None:
            s=s+actual_node.data
            b.append(actual_node.data)
            actual_node=actual_node.next_node
        print(s)
        print(b)
    # def search_item(self,data):
    #     current_data=self.head
    #     new=nod(data)
    #     while (current_data.data!=data):
    #         current_data=current_data.next_node
    #     if current_data.data is data:
    #         print(True)
    #     else:
    #         print(False)
    def insert_with_index(self,data,index):
        new_data=nod(data)
        i=0
        actual_node=self.head
        previous_node=None
        while i<index:
            previous_node=actual_node
            actual_node=actual_node.next_node
            i=i+1
        previous_node.next_node,new_data.next_node=new_data,actual_node
    def remove_first(self):
        self.seize-=1
        self.head=self.head.next_node
    def remove_last(self):
        self.seize-=1
        actual_node=self.head
        previous_node=None
        while actual_node.next_node is not None:
            previous_node=actual_node
            actual_node=actual_node.next_node
        previous_node.next_node=None





linked=linked_list()
linked.insertstart(5)
linked.insertstart(15)
linked.insertstart(55)
linked.insert_end(4)


linked.insert_with_index(23,2)
linked.somme_list()
linked.remove_first()
linked.remove_last()
linked.somme_list()

print(linked.seize2())






