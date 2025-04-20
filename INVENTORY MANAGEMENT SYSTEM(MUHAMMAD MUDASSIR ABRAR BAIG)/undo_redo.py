import copy
class UndoRedoManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save_state(self, inventory):
        self.undo_stack.append(copy.deepcopy(inventory.products))
        self.redo_stack.clear()

    def undo(self, inventory):
        if self.undo_stack:
            self.redo_stack.append(copy.deepcopy(inventory.products))
            inventory.products = self.undo_stack.pop()

    def redo(self, inventory):
        if self.redo_stack:
            self.undo_stack.append(copy.deepcopy(inventory.products))
            inventory.products = self.redo_stack.pop()
