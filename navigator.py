from maze import *
from exception import *
from stack import *

class PacMan:
    navigator_maze = []

    def __init__(self, grid: Maze) -> None:
        self.navigator_maze = grid.grid_representation

    def is_valid(self, x, y):
        if x < 0 or x >= len(self.navigator_maze):
            return False
        elif y < 0 or y >= len(self.navigator_maze[0]):
            return False
        return True

    def is_safe(self, x, y, visited):
        n = len(self.navigator_maze)
        m = len(self.navigator_maze[0])
        if (0 <= x < n and 0 <= y < m):
            return (self.navigator_maze[x][y] == 0 and not visited[x][y])
        else:
            return False

    def find_path(self, start, end):
        n = len(self.navigator_maze)
        m = len(self.navigator_maze[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        if not self.is_valid(start[0],start[1]) or not self.is_valid(end[0],end[1]) or self.navigator_maze[start[0]][start[1]] == 1 or self.navigator_maze[end[0]][end[1]] == 1:
            raise PathNotFoundException
        
        move_x = [1, 0, -1, 0]
        move_y = [0, 1, 0, -1]
        my_stack = Stack()
        path = []
        my_stack.push(start)
        visited[start[0]][start[1]] = True

        while not my_stack.is_empty():
            here = my_stack.peek()
            x, y = here

            if here == end:
                while not my_stack.is_empty():
                    temp = my_stack.pop()
                    path.append(temp)
                path.reverse()
                return path

            move_made = False
            for i in range(4):
                new_x = x + move_x[i]
                new_y = y + move_y[i]

                if self.is_safe(new_x, new_y, visited):
                    my_stack.push((new_x, new_y))
                    visited[new_x][new_y] = True
                    move_made = True
                    break

            if not move_made:
                my_stack.pop()

        raise PathNotFoundException()