import networkx as nx
import matplotlib.pyplot as plt
import pydot

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            if root.left and key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if root.right and key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            elif root.left and self.get_balance(root.left) < 0:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            elif root.right and self.get_balance(root.right) > 0:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root
    
    def traverse(self, root, order='in'):
        if root is not None:
            if order == 'in':
                self.traverse(root.left, order)
                print(root.key, end=' ')
                self.traverse(root.right, order)
            elif order == 'pre':
                print(root.key, end=' ')
                self.traverse(root.left, order)
                self.traverse(root.right, order)
            elif order == 'post':
                self.traverse(root.left, order)
                self.traverse(root.right, order)
                print(root.key, end=' ')

    def left_rotate(self, z):
        y = z.right
        if y is None:
            return z

        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if root.key < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)

    def right_rotate(self, y):
        x = y.left
        if not x:
            return y

        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left),
                        self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),
                        self.get_height(x.right))

        return x

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.min_value_node(root.left)

    def max_value_node(self, root):
        if root is None or root.right is None:
            return root
        return self.max_value_node(root.right)
        
    def min(self, root):
        if root is None:
            return None
        current = root
        while current.left:
            current = current.left
        return current.key

    def max(self, root):
        max_node = self.max_value_node(root)
        if max_node:
            return max_node.key
        return None
    
    def _build_graph(self, root, graph, parent=None):
        if root is None:
            return

        graph.add_node(root.key)
        if parent is not None:
            graph.add_edge(parent.key, root.key)

        self._build_graph(root.left, graph, root)
        self._build_graph(root.right, graph, root)

    def draw(self, root):
        tree_graph = nx.DiGraph()
        self._build_graph(root, tree_graph)
        
        pos = nx.drawing.nx_pydot.graphviz_layout(tree_graph, prog="dot")

        nx.draw(tree_graph, pos, with_labels=True, node_size=400, node_color="lightblue", font_size=8, font_weight="bold")
        plt.show()