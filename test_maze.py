import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    """     def test_maze_create_cells(self):
        win = Window(500, 500)
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        ) """
    

    """    def test_entrance_exit(self):
        win = Window(500, 500)
        num_cols = 10
        num_rows = 7
        m2 = Maze(10, 10, num_rows, num_cols, 15, 15, win)
        self.assertEqual(m2._cells[0][0].has_top_wall, False)
        self.assertEqual(m2._cells[num_cols-1][num_rows-1].has_right_wall, True)"""
    

    """ def test_break_walls(self):
        win = Window(500, 500)
        num_cols = 10
        num_rows = 7
        m2 = Maze(10, 10, num_rows, num_cols, 15, 15, win)
        
        m2._break_walls_r(0,0) """

    def test_visited(self):
        win=Window(500, 500)
        num_cols = 5
        num_rows = 5
        m2 = Maze(10, 10, num_rows, num_cols, 50, 50, win)
       # m2._break_walls_r(0,0)

        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(
                m2._cells[i][j].visited, False
            )


        

if __name__ == "__main__":
    unittest.main()