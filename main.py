from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    num_rows = 5
    num_cols = 5
    margin = 1
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)


    maze = Maze(1, 1, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()


    win.wait_for_close()
main()