from graphics import Line, Point
class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True 
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.visited = False

        self._win = win


    def draw_cell(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1,y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y1), Point(x1,y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line,  "black")
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line,  "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if undo is not False and undo is not True:
            color = "red"
        else:
            color = "blue"
        
        origin_cell_x = (self._x1 + self._x2)/2
        origin_cell_y = (self._y1 + self._y2) / 2
        origin_cell_center = Point(origin_cell_x, origin_cell_y)

        to_cell_x = (to_cell._x1 + to_cell._x2) / 2
        to_cell_y = (to_cell._y1 + to_cell._y2) / 2
        to_cell_center = Point(to_cell_x, to_cell_y)

        path = Line(origin_cell_center, to_cell_center)
        self._win.draw_line(path, color)
        
        
        

       
