# Pac-Man in Maze World

## Overview

This project is a Python-based navigation system for Pac-Man in a 2D maze world. Pac-Man must navigate through a grid while avoiding ghosts and reach a specific destination. The system uses a **stack-based approach** to model and solve the maze traversal problem. The maze is a rectangular grid where cells can either be vacant or occupied by ghosts.

This project is designed for educational purposes as part of an assignment for a data structures course (COL106). The key objective is to implement and use stacks to solve the problem efficiently.

## Features

- **Maze Representation**: The maze is a 2D grid where vacant cells are marked as `0`, and cells containing ghosts are marked as `1`.
- **Stack-based Pathfinding**: The system finds a path from Pac-Man's starting position to his destination, using a stack to track the path.
- **Ghost Management**: Ghosts can be added and removed from specific cells, dynamically altering the maze.
- **Efficient Search**: The pathfinding algorithm ensures a time complexity of **O(n * m)**, where `n` is the number of rows and `m` is the number of columns.

## Project Structure

The project is divided into the following components:

1. **Maze Class** (`maze.py`):
   - Manages the maze grid and allows adding/removing ghosts.
   - Provides utility functions to check whether a cell contains a ghost and to print the maze.

2. **Navigator Class** (`navigator.py`):
   - Handles pathfinding from a given start position to an end position within the maze.
   - Implements the stack-based traversal algorithm to find valid paths, avoiding ghosts.

3. **Stack Class** (`stack.py`):
   - Implements a dynamic stack to support the navigation system.
   - This stack stores the path and helps in backtracking when Pac-Man encounters dead ends.

4. **Exception Handling** (`exception.py`):
   - Contains custom exceptions such as `PathNotFoundException` to handle scenarios where no valid path is found.

5. **Main Script** (`main.py`):
   - A test script that allows you to run and debug the maze navigation system.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/pacman-maze-world.git
   cd pacman-maze-world
