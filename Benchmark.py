from BST import BinarySearchTree
from AVL import AVLTree
import random
import time

N = 5000000

bst = BinarySearchTree()
avl = AVLTree()
root = None

start_time = time.time()
values = [random.randint(0, 10000000) for _ in range(N)]
value_time = time.time() - start_time
print("Value creation time: {} seconds".format(value_time))

# Node insertion

start_time = time.time()
print("start")
for value in values:
    bst.insert(value)
    root = avl.insert(root, value)
insertion_time = time.time() - start_time   
print("Node insertion time: {} seconds".format(insertion_time)) 

# Number of searches to perform
num_searches = 100

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

# Number of searches to perform
num_searches2 = 500

# Generate random search keys
search_keys2 = [random.randint(0, 10000000) for _ in range(num_searches2)]

# BST search
start_time = time.time()
for key in search_keys2:
    bst.search(key)
bst_search_time2 = time.time() - start_time

# AVL search
start_time = time.time()
for key in search_keys2:
    avl.search(root, key)
avl_search_time2 = time.time() - start_time

print("BST search time 2: {} seconds".format(bst_search_time2))
print("AVL search time 2: {} seconds".format(avl_search_time2))

# Number of searches to perform
num_searches3 = 1000

# Generate random search keys
search_keys3 = [random.randint(0, 10000000) for _ in range(num_searches3)]

# BST search
start_time = time.time()
for key in search_keys3:
    bst.search(key)
bst_search_time3 = time.time() - start_time

# AVL search
start_time = time.time()
for key in search_keys3:
    avl.search(root, key)
avl_search_time3 = time.time() - start_time

print("BST search time 3: {} seconds".format(bst_search_time3))
print("AVL search time 3: {} seconds".format(avl_search_time3))

# Number of searches to perform
num_searches4 = 5000

# Generate random search keys
search_keys4 = [random.randint(0, 10000000) for _ in range(num_searches4)]

# BST search
start_time = time.time()
for key in search_keys4:
    bst.search(key)
bst_search_time4 = time.time() - start_time

# AVL search
start_time = time.time()
for key in search_keys4:
    avl.search(root, key)
avl_search_time4 = time.time() - start_time

print("BST search time 4: {} seconds".format(bst_search_time4))
print("AVL search time 4: {} seconds".format(avl_search_time4))

# Number of searches to perform
num_searches5 = 10000

# Generate random search keys
search_keys5 = [random.randint(0, 10000000) for _ in range(num_searches5)]

# BST search
start_time = time.time()
for key in search_keys5:
    bst.search(key)
bst_search_time5 = time.time() - start_time

# AVL search
start_time = time.time()
for key in search_keys5:
    avl.search(root, key)
avl_search_time5 = time.time() - start_time

print("BST search time 5: {} seconds".format(bst_search_time5))
print("AVL search time 5: {} seconds".format(avl_search_time5))

# Number of searches to perform
num_searches6 = 50000

# Generate random search keys
search_keys6 = [random.randint(0, 10000000) for _ in range(num_searches6)]

# BST search
start_time = time.time()
for key in search_keys6:
    bst.search(key)
bst_search_time6 = time.time() - start_time

# AVL search
start_time = time.time()
for key in search_keys6:
    avl.search(root, key)
avl_search_time6 = time.time() - start_time

print("BST search time 6: {} seconds".format(bst_search_time6))
print("AVL search time 6: {} seconds".format(avl_search_time6))

# Number of searches to perform
num_searches7 = 1000000

# Generate random search keys
search_keys7 = [random.randint(0, 10000000) for _ in range(num_searches7)]

# BST search
start_time = time.time()
for key in search_keys7:
    bst.search(key)
bst_search_time7 = time.time() - start_time

# AVL search
start_time = time.time()
for key in search_keys7:
    avl.search(root, key)
avl_search_time7 = time.time() - start_time

print("BST search time 7: {} seconds".format(bst_search_time7))
print("AVL search time 7: {} seconds".format(avl_search_time7))

# Number of searches to perform
num_searches8 = 500000

# Generate random search keys
search_keys8 = [random.randint(0, 10000000) for _ in range(num_searches8)]

# BST search
start_time = time.time()
for key in search_keys8:
    bst.search(key)
bst_search_time8 = time.time() - start_time

# AVL search
start_time = time.time()
for key in search_keys8:
    avl.search(root, key)
avl_search_time8 = time.time() - start_time

print("BST search time 8: {} seconds".format(bst_search_time8))
print("AVL search time 8: {} seconds".format(avl_search_time8))

# Number of searches to perform
num_searches9 = 1000000

# Generate random search keys
search_keys9 = [random.randint(0, 10000000) for _ in range(num_searches9)]

# BST search
start_time = time.time()
for key in search_keys9:
    bst.search(key)
bst_search_time9 = time.time() - start_time

# AVL search
start_time = time.time()
for key in search_keys9:
    avl.search(root, key)
avl_search_time9 = time.time() - start_time

print("BST search time 9: {} seconds".format(bst_search_time9))
print("AVL search time 9: {} seconds".format(avl_search_time9))

# Number of searches to perform
num_searches10 = 5000000

# Generate random search keys
search_keys10 = [random.randint(0, 10000000) for _ in range(num_searches10)]

# BST search
start_time = time.time()
for key in search_keys10:
    bst.search(key)
bst_search_time10 = time.time() - start_time

# AVL search
start_time = time.time()
for key in search_keys10:
    avl.search(root, key)
avl_search_time10 = time.time() - start_time

print("BST search time 10: {} seconds".format(bst_search_time10))
print("AVL search time 10: {} seconds".format(avl_search_time10))


