# =========================================
# Search (Latihan 3)
# =========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

# buat tree
root = None
data_list = [50, 30, 70, 20, 40, 60, 80]
for data in data_list:
    root = insert(root, data)



def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


# Uji pencarian
key = 16

if search(root, key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")