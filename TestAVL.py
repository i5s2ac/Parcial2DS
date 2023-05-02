from AVL import AVLTree
import random 

if __name__ == "__main__":
    my_tree = AVLTree()
    root = None 
    keys = list(range(1, 101))
    random.shuffle(keys)

    for key in keys:
        root = my_tree.insert(root, key)

    print("")
    print("Traversal In-Order:")
    my_tree.traverse(root, 'in')
    print("")
    print("\nTraversal Pre-Order:")
    my_tree.traverse(root, 'pre')
    print("")
    print("\nTraversal Post-Order:")
    my_tree.traverse(root, 'post')

    print("\n\nSearching for node with key 25:")
    found_node = my_tree.search(root, 25)
    if found_node:
        print("Node found with key:", found_node.key)
    else:
        print("Node not found.")

    print("\nMinimum value in the tree:", my_tree.min(root))
    print("Maximum value in the tree:", my_tree.max(root))

    print("\nDeleting node with key 25")
    root = my_tree.delete(root, 25)

    #Imprime AVL tree con 100 nodos
    my_tree.draw(root)
    
    