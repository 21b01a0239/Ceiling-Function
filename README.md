# Ceiling-Function
% Built a Python program to count unique binary search tree (BST) structures from multiple input sequences. Used preorder traversal with None placeholders to capture exact tree shapes and compared them using sets for uniqueness. %
import sys
class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root

def preorder_traversal(root, result):
    if not root:
            result.append(None)
            return
    result.append(root.value)
    preorder_traversal(root.left,result)
    preorder_traversal(root.right,result)
def tree_shape(layers):
    root = None
    for layer in layers:
        root = insert(root, layer)
    result = []
    preorder_traversal(root, result)
    return result
def main(argv):
    no_of_prototypes = int(argv[0])
    no_of_layers = int(argv[1])
    layers = []
    for i in range(no_of_prototypes):
        layers.append([int(x) for x in argv[2 + i * no_of_layers : 2 + (i + 1) * no_of_layers]])
    shapes = []

    for item in range(no_of_prototypes):
        shape = tree_shape(layers[item])
        shapes.append(shape)
    same_shape = []
    for itr1 in shapes:
        for itr2 in shapes:
            count_of_None = 0

            if shapes.index(itr1)<shapes.index(itr2):
                for itr in range(len(itr1)):
                    if(itr1[itr] == None and itr2[itr] == None):
                        count_of_None += 1    
            if count_of_None == no_of_layers + 1:
                same_shape.append(itr2)   

    for lists in same_shape:
        if lists in shapes:
            shapes.remove(lists)
    return len(shapes)

if __name__ == "__main__":
    print(main(sys.argv[1:]))
