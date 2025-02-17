from tkinter import Tk, BOTH, Canvas
class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.__root_widget = Tk()
        self.__root_widget.title("My Maze")

        self.__canvas = Canvas(self.__root_widget, bg = "white", width=self.__width, height=self.__height)
        self.__canvas.pack(fill = BOTH, expand = 1)
        self.__is_running = False

        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close())

    
    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def draw_line(self,line, fill_color = "black"):
        line.draw(self.__canvas, fill_color)
    

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__is_running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


    def draw(self, canvas, color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=color, width=2)

