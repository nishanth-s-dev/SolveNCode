from typing import Optional

"""
Operations supported :
1. append           -> done
2. prepend          -> done
3. print_list       -> done
4. insert_at
5. delete
6. delete_at
7. find
8. length
9. reverse
10. is_empty
11. get_at
12. clear
"""

class Node:
    def __init__(self, val=0, next: Optional['Node'] = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head_val = None):
        self.head = Node(head_val) if head_val is not None else None

    def __str__(self):
        res = []
        current = self.head
        if current is None:
            return "List is empty"
        while current:
            res.append(str(current.val))
            current = current.next
        return " -> ".join(res) + " -> None"

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        print(self)


def main():
    nodes = LinkedList()
    nodes.append(1)
    nodes.append(2)
    nodes.append(3)
    nodes.append(4)
    nodes.append(5)
    nodes.prepend(0)
    nodes.prepend(-1)
    nodes.prepend(-2)

    print(nodes)

if __name__ == "__main__":
    main()