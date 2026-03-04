#===============================================
#nama : vezilatun nisa
#nim : J0403251134
#kelas: b1
#===============================================
#implementasi dasae: node pada linked list
#===============================================
#membuat class node (merupakan)
class node:
    def __init__(self,data):
        self.data = data #meniympan nilai/data
        self.next = None #pointer ke note berikutnya
node("A")
nodeA = node ("A")
nodeB = node ("B")
nodeC = node ("C")

nodeA.next = nodeB
nodeB.next = nodeC

head = nodeA

current = head
while current is not None:
    print(current.data)
    current = current.next

    class linkedlist:
        def insert_awal(self,data):
            node_baru = node(data)
            node_baru.next = self.head
            self.head = node_baru

            def tampilkan(self):
                current = self.head
                while current is not None:
                    print(current.data)
                    current = current.next

print("=====list baru=====")
ll=linkedlist()
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()