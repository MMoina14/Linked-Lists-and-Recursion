"""
Linked List and Recursion Lab
Employee Roster Management System
"""


class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Initialize a node with data and next pointer.
        
        Args:
            data (int): The employee ID to store in this node
        """
        # Assign the provided data to an instance variable
        self.data = data
        # Initialize 'next' to None (no next node yet)
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        # Initialize 'head' to None to represent an empty list
        self.head = None

    def insert_at_front(self, data):
        """
        Insert a new node at the front of the list. O(1) operation.
        
        Args:
            data (int): The employee ID to insert
        """
        # Create a new Node with 'data'
        new_node = Node(data)
        
        # Insert it at the front by pointing new node to current head
        new_node.next = self.head
        
        # Update 'head' to the new node
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list. O(n) operation.
        
        Args:
            data (int): The employee ID to insert
        """
        # Create a new Node with 'data'
        new_node = Node(data)
        
        # Special case: if list is empty, new node becomes head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to the end of the list
        current = self.head
        while current.next is not None:
            current = current.next
        
        # Set the last node's 'next' reference to the new node
        current.next = new_node

    def recursive_sum(self):
        """
        Calculate the sum of all node data using recursion.
        
        Returns:
            int: The sum of all employee IDs in the list
        """
        # Use helper function starting from head
        return self._sum_helper(self.head)
    
    def _sum_helper(self, node):
        """
        Recursive helper function to sum all nodes.
        
        Base case: If node is None, return 0
        Recursive case: Return node.data + sum of remaining nodes
        
        Args:
            node (Node): Current node being processed
            
        Returns:
            int: Sum of current node and all subsequent nodes
        """
        # Base case: if current node is None, return 0
        if node is None:
            return 0
        
        # Recursive case: return node.data + recursive call on node.next
        return node.data + self._sum_helper(node.next)

    def recursive_reverse(self):
        """
        Reverse the list in-place using recursion.
        
        This approach uses a helper that processes nodes iteratively
        through recursive calls, reversing the 'next' pointers.
        """
        # Use helper function with prev=None and current=head
        self.head = self._reverse_helper(None, self.head)
    
    def _reverse_helper(self, prev, current):
        """
        Recursive helper to reverse the list.
        
        Approach:
        - Base case: if current is None, prev is the new head
        - Recursive case: save next, reverse pointer, recurse forward
        
        Args:
            prev (Node): The previous node (will become next in reversed list)
            current (Node): The current node being processed
            
        Returns:
            Node: The new head of the reversed list
        """
        # Base case: if current is None, return prev (new head)
        if current is None:
            return prev
        
        # Save the next node before we change the pointer
        next_node = current.next
        
        # Reverse the pointer: current now points to prev
        current.next = prev
        
        # Recurse: move forward with current becoming prev
        return self._reverse_helper(current, next_node)

    def recursive_search(self, target):
        """
        Search for a target value in the list using recursion.
        
        Args:
            target (int): The employee ID to search for
            
        Returns:
            bool: True if target found, False otherwise
        """
        # Use helper function starting from head
        return self._search_helper(self.head, target)
    
    def _search_helper(self, node, target):
        """
        Recursive helper function to search for target.
        
        Base cases:
        1. If node is None, target not found (return False)
        2. If node.data == target, found (return True)
        Recursive case: Search in remaining nodes
        
        Args:
            node (Node): Current node being examined
            target (int): The value to search for
            
        Returns:
            bool: True if target found in current or subsequent nodes
        """
        # Base case 1: reached end without finding target
        if node is None:
            return False
        
        # Base case 2: found the target
        if node.data == target:
            return True
        
        # Recursive case: search in the next node
        return self._search_helper(node.next, target)

    def display(self):
        """
        Display the contents of the list in a readable format.
        
        Prints in format: val -> val -> val -> None
        """
        # Handle empty list
        if self.head is None:
            print("Empty list (None)")
            return
        
        # Traverse from head and collect each node's data
        current = self.head
        result = []
        
        while current is not None:
            result.append(str(current.data))
            current = current.next
        
        # Format output as 'val -> val -> val -> None'
        output = " -> ".join(result) + " -> None"
        print(output)


# ============================================================================
# MAIN DRIVER CODE - Demonstrates all functionality
# ============================================================================

def main():
    """
    Main function to test and demonstrate all linked list operations.
    """
    print("=" * 70)
    print("EMPLOYEE ROSTER MANAGEMENT SYSTEM")
    print("Linked List with Recursive Operations")
    print("=" * 70)
    
    # Create a new linked list
    roster = LinkedList()
    
    # ========================================================================
    # Test 1: Insert at End
    # ========================================================================
    print("\n[TEST 1] Inserting Employee IDs at End")
    print("-" * 70)
    employee_ids = [101, 205, 313, 427, 538]
    
    for emp_id in employee_ids:
        roster.insert_at_end(emp_id)
        print(f"  Inserted ID {emp_id}")
    
    print("\nCurrent roster:")
    print("  ", end="")
    roster.display()
    
    # ========================================================================
    # Test 2: Recursive Sum
    # ========================================================================
    print("\n[TEST 2] Calculating Sum of All Employee IDs (Recursive)")
    print("-" * 70)
    total_sum = roster.recursive_sum()
    print(f"  Sum of all employee IDs: {total_sum}")
    print(f"  Expected: {sum(employee_ids)}")
    print(f"  Match: {'✓ PASS' if total_sum == sum(employee_ids) else '✗ FAIL'}")
    
    # ========================================================================
    # Test 3: Recursive Search
    # ========================================================================
    print("\n[TEST 3] Searching for Employee IDs (Recursive)")
    print("-" * 70)
    
    search_tests = [
        (313, True, "Should find (in middle)"),
        (101, True, "Should find (at start)"),
        (538, True, "Should find (at end)"),
        (999, False, "Should NOT find"),
        (0, False, "Should NOT find"),
    ]
    
    for target, expected, description in search_tests:
        found = roster.recursive_search(target)
        status = "✓ PASS" if found == expected else "✗ FAIL"
        result = "FOUND" if found else "NOT FOUND"
        print(f"  ID {target:3d}: {result:9s} - {description:25s} [{status}]")
    
    # ========================================================================
    # Test 4: Display Current List
    # ========================================================================
    print("\n[TEST 4] Display Current List")
    print("-" * 70)
    print("  Before reversal:")
    print("    ", end="")
    roster.display()
    
    # ========================================================================
    # Test 5: Recursive Reverse
    # ========================================================================
    print("\n[TEST 5] Reversing Employee Roster (Recursive)")
    print("-" * 70)
    roster.recursive_reverse()
    
    print("  After reversal:")
    print("    ", end="")
    roster.display()
    
    # Verify sum is still the same
    new_sum = roster.recursive_sum()
    print(f"\n  Sum after reversal: {new_sum}")
    print(f"  Sum unchanged: {'✓ PASS' if new_sum == total_sum else '✗ FAIL'}")
    
    # ========================================================================
    # Test 6: Insert at Front
    # ========================================================================
    print("\n[TEST 6] Inserting New Employee at Front")
    print("-" * 70)
    new_id = 999
    roster.insert_at_front(new_id)
    print(f"  Inserted ID {new_id} at front")
    print("  Updated roster:")
    print("    ", end="")
    roster.display()
    
    # ========================================================================
    # Test 7: Search After Modifications
    # ========================================================================
    print("\n[TEST 7] Verifying Operations After Modifications")
    print("-" * 70)
    
    final_sum = roster.recursive_sum()
    expected_final_sum = total_sum + new_id
    print(f"  New sum: {final_sum}")
    print(f"  Expected: {expected_final_sum}")
    print(f"  Match: {'✓ PASS' if final_sum == expected_final_sum else '✗ FAIL'}")
    
    print(f"\n  Search for {new_id}: {'FOUND ✓' if roster.recursive_search(new_id) else 'NOT FOUND ✗'}")
    print(f"  Search for 101: {'FOUND ✓' if roster.recursive_search(101) else 'NOT FOUND ✗'}")
    
    # ========================================================================
    # Test 8: Empty List Edge Case
    # ========================================================================
    print("\n[TEST 8] Testing Empty List Edge Cases")
    print("-" * 70)
    empty_list = LinkedList()
    
    print("  Empty list display:")
    print("    ", end="")
    empty_list.display()
    
    print(f"  Sum of empty list: {empty_list.recursive_sum()}")
    print(f"  Search in empty list: {empty_list.recursive_search(100)}")
    
    # ========================================================================
    # Summary
    # ========================================================================
    print("\n" + "=" * 70)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("  ✓ insert_at_front() - O(1) operation")
    print("  ✓ insert_at_end() - O(n) operation")
    print("  ✓ recursive_sum() - Demonstrates recursive traversal")
    print("  ✓ recursive_search() - Shows recursive search pattern")
    print("  ✓ recursive_reverse() - In-place reversal using recursion")
    print("  ✓ Edge cases handled (empty list)")
    print("=" * 70)


if __name__ == "__main__":
    main()