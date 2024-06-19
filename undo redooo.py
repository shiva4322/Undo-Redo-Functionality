class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class UndoRedoLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def add_change(self, change):
        new_node = Node(change)
        if self.head is None:
            self.head = new_node
            self.current = new_node
        else:
            # If we are in the middle of the list, discard all the redo history
            if self.current.next:
                self.current.next.prev = None
                self.current.next = None
            self.current.next = new_node
            new_node.prev = self.current
            self.current = new_node

    def undo(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.data
        return None  # Nothing to undo

    def redo(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.data
        return None  # Nothing to redo

    def current_state(self):
        if self.current:
            return self.current.data
        return None  # No current state

# Example usage
undo_redo_list = UndoRedoLinkedList()
undo_redo_list.add_change("Shiva 1")
undo_redo_list.add_change("Sai 2")
undo_redo_list.add_change("Ganesh 3")

print(undo_redo_list.current_state())  

undo_redo_list.undo()
print(undo_redo_list.current_state())  

undo_redo_list.undo()
print(undo_redo_list.current_state())  

undo_redo_list.redo()
print(undo_redo_list.current_state())  

undo_redo_list.add_change("Guda 4")
print(undo_redo_list.current_state())  

undo_redo_list.redo()  # Nothing to redo
print(undo_redo_list.current_state())  
