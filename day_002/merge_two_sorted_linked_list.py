class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(list1, list2):
    result = ListNode()
    current = result

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return result.next


# Helper
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# Helper
def createLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == "__main__":
    list_one = createLinkedList([1, 3, 5])
    list_two = createLinkedList([2, 4, 6])

    print("List 1:")
    printList(list_one)

    print("List 2:")
    printList(list_two)

    mergedList = merge(list_one, list_two)

    print("Merged List:")
    printList(mergedList)
