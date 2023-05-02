from BST import BinarySearchTree
from AVL import AVLTree
import random
import time

N = 10000000

bst = BinarySearchTree()
avl = AVLTree()
root = None

values = [random.randint(0, 10000000) for _ in range(N)]

# BST insertion

for value in values:
    bst.insert(value)

# AVL insertion
for value in values:
    root = avl.insert(root, value)

# Number of searches to perform
num_searches = 10000000

# Generate random search keys
search_keys = [random.randint(0, 10000000) for _ in range(num_searches)]

# BST search
start_time = time.time()
for key in search_keys:
    bst.search(key)
bst_search_time = time.time() - start_time

# AVL search
start_time = time.time()
for key in search_keys:
    avl.search(root, key)
avl_search_time = time.time() - start_time

print("BST search time: {} seconds".format(bst_search_time))
print("AVL search time: {} seconds".format(avl_search_time))
    


