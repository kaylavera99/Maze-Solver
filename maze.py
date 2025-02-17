from cell import Cell
from graphics import Line, Point
import random
import time
class Maze:
    def __init__(self, x1, y1, num_rows,num_cols, cell_size_x, cell_size_y, win, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self.seed = seed

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(i=0, j=0)
        self._reset_cells_visited()
        #self._solve_r()



    def _create_cells(self):
        for cell_col in range(self._num_cols):
            cell_row = []
            for crow in range(self._num_rows):
                draw_cell = Cell(self._win)
                cell_row.append(draw_cell)
            self._cells.append(cell_row)
        
        print(f"Number of columns: {len(self._cells)}")
        print(f"Number of rows in first column: {len(self._cells[0])}")

        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
                

        



    def _draw_cell(self, i, j):
        cell_x1 = self._x1 + i * self._cell_size_x
        cell_y1 = self._y1 + j * self._cell_size_y
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y
        #print(f"Cell ({i}, {j}) -> Top-left: ({cell_x1}, {cell_y1}), Bottom-right: ({cell_x2}, {cell_y2})")

        self._cells[i][j].draw_cell(cell_x1, cell_x2, cell_y1, cell_y2)
        
        #self._break_entrance_and_exit()
        self._animate()



    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.15)


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        last_index_col = self._num_cols - 1
        last_index_row = self._num_rows -1

        self._cells[last_index_col][last_index_row].has_bottom_wall = False
        self._draw_cell(last_index_col, last_index_row)

    
    def _break_walls_r(self, i, j):
        
        #print("I am i", i)
        #print("I am j", j)
        current = self._cells[i][j]
       # print("This is current", current)
        current.visited = True


        while True:
            to_visit = []
            #left
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            #right
            if i < self._num_cols -1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            #up
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            next_direction = random.randrange(len(to_visit))
            next_index = to_visit[next_direction]

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if next_index[0] == i -1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if next_index[1]== j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            if next_index[1] == j -1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False

            next_i, next_j = to_visit[0]
            self._break_walls_r(next_i, next_j)


            
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
                
    

    def _solve_r(self,i=0, j=0):
        end_x_index = self._num_rows - 1
        end_y_index = self._num_cols - 1
        self._animate()
        self._cells[i][j].visited = True

        print(f"Checking cell ({i}, {j}), end is at ({end_x_index}, {end_y_index})")

        if i == end_x_index and j == end_y_index:   #At the end cell 
            print("We got to the end", i, j)
            return True

                
        #Right
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            print(f"Moving right from ({i}, {j}) to ({i+1}, {j})")
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
                
        #Left
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            print(f"Moving left from ({i}, {j}) to ({i-1}, {j})")
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
        #Top
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            print(f"Moving top from ({i}, {j}) to ({i}, {j-1})")
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
        #Bottom
        if j < self._num_rows -1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            print(f"Moving bottom from ({i}, {j}) to ({i}, {j+1})")
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
        self._cells[i][j].draw_move(self._cells[i][j], undo=True)
        return False


    def solve(self):
        if self._solve_r(0, 0)== True:
            return True
        else:
            return False




        


        





