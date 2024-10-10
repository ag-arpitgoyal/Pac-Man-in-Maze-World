class Stack:
    def __init__(self) -> None:
        # YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self.points = []

    def push(self, point) -> None:
        self.points.append(point)

    def pop(self):
        if not self.is_empty():
            return self.points.pop()
        else:
            raise IndexError("pop from empty stack")

    def is_empty(self) -> bool:
        return len(self.points) == 0

    def peek(self):
        if not self.is_empty():
            return self.points[-1]
        else:
            raise IndexError("peek from empty stack")

    # You can implement this class however you like
