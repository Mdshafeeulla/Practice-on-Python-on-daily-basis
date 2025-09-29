class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def delete_duplicates(self, head):
        """
        Deletes all duplicate nodes from a sorted singly linked list.
        """
        current = head
        while current and current.next:
            # If the current node's value equals the next node's value
            if current.val == current.next.val:
                # Skip the duplicate node by updating the 'next' pointer
                current.next = current.next.next
            else:
                # Move to the next node if no duplicate was found
                current = current.next
        return head


# --- Helper function to build a linked list from a list of values ---
def build_linked_list(data):
    """
    Takes a list of values and returns the head of the linked list.
    """
    if not data:
        return None

    head = ListNode(data[0])
    current = head
    for val in data[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# --- Helper function to print a linked list ---
def print_linked_list(head):
    """
    Prints the values of the linked list.
    """
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return " -> ".join(map(str, values))


# --- Execution ---
input_values = [1, 1, 2, 2, 3, 4]
head_node = build_linked_list(input_values)

print(f"Original list: {print_linked_list(head_node)}")

Dup_solution = Solution()
result_head = Dup_solution.delete_duplicates(head_node)

print(f"List after removing duplicates: {print_linked_list(result_head)}")