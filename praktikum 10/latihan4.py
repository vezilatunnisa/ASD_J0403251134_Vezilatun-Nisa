# =========================================
# Node & Insert BST
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


# =========================================
# Preorder Traversal
# =========================================

def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)


# =========================================
# Tampilkan Struktur Tree
# =========================================

def tampil_struktur(root, level=0, label="Root"):
    if root is not None:
        print(" " * (level * 4) + f"{label}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


# =========================================
# Program utama
# =========================================

root = None

# Data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root)