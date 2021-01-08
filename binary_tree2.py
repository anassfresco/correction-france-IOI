class nod:
    def __init__(self,data):
        self.data=data
        self.right_node=None
        self.left_node=None
class binary_tree:
    def __init__(self):
        self.tree=None
    def insert(self,data):
        new_node=nod(data)
        if not self.tree:
            self.tree=new_node
        else:
            self.insert_recusion(data,self.tree)
    def insert_recusion(self,data,node):
        new_node=nod(data)
        if data<node.data:
            if node.left_node:
                 self.insert_recusion(data,node.left_node)
            else:
                 node.left_node=new_node
        else:
            if node.right_node:
                self.insert_recusion(data, node.right_node)
            else:
                node.right_node = new_node
    def maxNode(self):
        if self.tree is None:
            return
        else:
            self.max_recusion(self.tree)
    def max_recusion(self,node):
        if node.right_node is None:
            return node.data
        else:
            return self.max_recusion(node.right_node)
    def minNode(self):
        if self.tree is None:
            return
        else:
           return  self.min_recusion(self.tree)

    def min_recusion(self, node):
        if node.left_node is None:
            return node.data
        else:
            return self.min_recusion(node.left_node)
    def traverse(self):
            return self.sort(self.tree)
    def sort(self,node):
        if node is None:
            return []
        else:
            return self.sort(node.left_node)+[node.data]+self.sort(node.right_node)
    def traverse_in_order(self):
        if self.tree:
            self.traverse_recusion(self.tree)
    def traverse_recusion(self,node):
        if node.left_node:
            self.traverse_recusion(node.left_node)
        print(node.data)
        if node.right_node:
            self.traverse_recusion(node.right_node)
    def traverse_in_preorder(self):
        if self.tree:
            self.traverse_prerecusion(self.tree)
    def traverse_prerecusion(self,node):
        print(node.data)
        if node.left_node:
            self.traverse_recusion(node.left_node)
        elif  node.right_node:
            self.traverse_recusion(node.right_node)

    def remove_node(self,node):
        delparent = node
        node_delate = node.right_node
        while node_delate.left_node is not None:
            delparent = node_delate
            node_delate = node_delate.left_node
        node.data = node_delate
        if node_delate.right_node is not None:
            if delparent.data > node_delate.data:
                delparent.left_node = node_delate.right_node
            else:
                delparent.right_node = node_delate.right_node
        else:
            if delparent.data > node_delate.data:
                delparent.left_node = None
            else:
                delparent.right_node = None
    def remove_item(self,data):
        if self.tree is None:
            return False
        if self.tree.data==data:
            if not self.tree.right_node  and not self.tree.left_node:
                self.tree=None
            elif  self.tree.left_node and self.tree.right_node is None:
                self.tree=self.tree.left_node
            elif self.tree.left_node and self.tree.right_nodea:
                self.remove_node(self.tree)



        #find root to remove
        parent=None
        node=self.tree
        while node and node.data!=data:
            parent=node
            if data<node.data:
                node=node.left_node
            else:
                node=node.right_node
        #case data not found
        if parent is None or node.data!=data:
            return False
        #case data has no children
        elif node.right_node is None and node.left_node is None:
            if data>parent.data:
                parent.right_node=None
            else:
                parent.left_node=None
            return True
        #case data has left child
        elif node.right_node is None and node.left_node is not None:
            if data>parent.data:
                parent.right_node=node.left_node
            else:
                parent.left_node=node.left_node
            return True
        #case data has right child only
        elif node.right_node is not  None and node.left_node is None:
            if data>parent.data:
                parent.right_node=node.rifd_node
            else:
                parent.left_node=node.left_node
            return True
        else:
            self.remove_node(node)
binary=binary_tree()
binary.insert(76)
binary.insert(34)
binary.insert(44)
binary.insert(64)
binary.insert(94)
binary.insert(32)

print(binary.traverse_in_order())
print(binary.traverse_in_preorder())
