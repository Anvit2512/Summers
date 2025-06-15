class Node:
    """Class to represent a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Class to represent the singly linked list."""
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        """Add a node with the given data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Added {data} as the head of the list.")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f"Added {data} to the end of the list.")

    def print_list(self):
        """Print all elements of the list."""
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        print("Linked List contents:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node from the list (1-based index)."""
        try:
            if self.head is None:
                raise Exception("Cannot delete from an empty list.")

            if n <= 0:
                raise IndexError("Index should be 1 or greater.")

            if n == 1:
                print(f"Deleting node {n} with value {self.head.data}")
                self.head = self.head.next
                return

            current = self.head
            count = 1
            while current is not None and count < n - 1:
                current = current.next
                count += 1

            if current is None or current.next is None:
                raise IndexError("Index out of range.")

            print(f"Deleting node {n} with value {current.next.data}")
            current.next = current.next.next

        except Exception as e:
            print(f"Error: {e}")


# ===========================
# TEST CASES
# ===========================

if __name__ == "__main__":
    ll = LinkedList()

    # Add sample data
    ll.add_to_end(10)
    ll.add_to_end(20)
    ll.add_to_end(30)
    ll.add_to_end(40)

    # Print initial list
    ll.print_list()

    # Delete 3rd node
    ll.delete_nth_node(3)
    ll.print_list()

    # Try deleting out-of-range
    ll.delete_nth_node(10)

    # Try deleting from an empty list
    empty_list = LinkedList()
    empty_list.delete_nth_node(1)

    # Try deleting with invalid index
    ll.delete_nth_node(0)
