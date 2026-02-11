class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head

        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            temp = temp.next
            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")


print("Contoh 1 (Elemen Ada)")
cll1 = CircularSinglyLinkedList()
for i in [3,7,12,19,25]:
    cll1.insert_at_end(i)
cll1.search(12)

print("\nContoh 2 (Elemen Tidak Ada)")
cll2 = CircularSinglyLinkedList()
for i in [5,10,15,20,30]:
    cll2.insert_at_end(i)
cll2.search(25)

print("\nContoh 3 (List Kosong)")
cll3 = CircularSinglyLinkedList()
cll3.search(10)