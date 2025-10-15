class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node  # ✅ Fixed
    return prev


def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# Example
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print_list(reverse_linked_list(head))
