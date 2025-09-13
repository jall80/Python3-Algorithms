class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# INSERT
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


# TRAVERSALS
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


# SEARCH
def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)


# FIND MIN AND MAX
def find_min(root):
    while root.left:
        root = root.left
    return root.value

def find_max(root):
    while root.right:
        root = root.right
    return root.value


# DELETE
def delete(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min_node(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)
    return root

def find_min_node(root):
    current = root
    while current.left:
        current = current.left
    return current


# EXAMPLE USAGE
if __name__ == "__main__":
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    root = None
    for val in values:
        root = insert(root, val)

    print("In-order traversal (Left → Root → Right):")
    inorder(root)
    print("\nPre-order traversal (Root → Left → Right):")
    preorder(root)
    print("\nPost-order traversal (Left → Right → Root):")
    postorder(root)

    print("\n\nSearch for 6:")
    found = search(root, 6)
    print("Found!" if found else "Not Found.")

    print("Minimum value in tree:", find_min(root))
    print("Maximum value in tree:", find_max(root))

    print("\nDelete value 10 and show in-order again (Left → Root → Right):")
    root = delete(root, 10)
    inorder(root)
    print()
