class Node:
    def __init__(self,data,next_node= None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self,value):
        if not isinstance(value,int):
            raise TypeError("data must be an integer")
        
    @property
    def next_node(self):
        return self._next_node
    @ next_node.setter
    def next_node(self, value):
        if value is not None and  not isinstance(value, Node):
            raise TypeError("Next_node must be a Node object")
        
        self._next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        result = []
        while current :
            result.append(str(current.data))
            current = current.next_node

        return "\n".join(result)
    
    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head   = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

                new_node.next_node = current.next_node
                current.next_node = new_node

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)