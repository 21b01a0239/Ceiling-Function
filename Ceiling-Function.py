# Ceiling-Function
# Built a Python program to count unique binary search tree (BST) structures from multiple input sequences. Used preorder traversal with None placeholders to capture exact tree shapes and compared them using sets for uniqueness. %
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def preorder_traversal(root, result):
    if not root:
        result.append(None)
        return
    result.append(root.value)
    preorder_traversal(root.left, result)
    preorder_traversal(root.right, result)

def tree_shape(layers):
    root = None
    for layer in layers:
        root = insert(root, layer)
    result = []
    preorder_traversal(root, result)
    return result

def main():
    no_of_prototypes = int(input("Enter number of prototypes: "))
    no_of_layers = int(input("Enter number of layers per prototype: "))
    
    layers = []
    for i in range(no_of_prototypes):
        layer_input = input(f"Enter layers for prototype {i+1} (space-separated integers): ")
        layer = list(map(int, layer_input.strip().split()))
        if len(layer) != no_of_layers:
            print("Invalid number of layers. Please try again.")
            return
        layers.append(layer)

    shapes = [tree_shape(layer) for layer in layers]

    same_shape = []
    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            if shapes[i] == shapes[j]:
                same_shape.append(shapes[j])

    for item in same_shape:
        if item in shapes:
            shapes.remove(item)

    print("Number of unique shapes:", len(shapes))

if __name__ == "__main__":
    main()


