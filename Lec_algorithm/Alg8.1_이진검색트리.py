import utility
class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data = data
def bin_search_tree_insert(root,node):
    if root is None:
        root=node
    else:
        if root.data >node.data:
            if root.l_child is None:
                root.l_child=node
            else:
                bin_search_tree_insert(root.l_child,node)
        else:
            if root.r_child is None:
                root.r_child=node
            else:
                bin_search_tree_insert(root.r_child,node)

r = Node(7)
bin_search_tree_insert(r,Node(9))
bin_search_tree_insert(r,Node(1))
bin_search_tree_insert(r,Node(3))
bin_search_tree_insert(r,Node(12))

utility.print_inOrder(r)
print()
utility.print_preOrder(r)
