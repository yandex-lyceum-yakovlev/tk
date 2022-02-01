import tkinter


class Snake:
    dx = 1
    dy = 0
    segments = [[2, 2], [2, 3], [2, 4]]

    def move(self):
        for p in self.segments:
            p[1] += 1


def draw(board, snake):
    for j in range(m):
        for i in range(n):
            c.create_rectangle(j * cell_height, i * cell_width, (j + 1) * cell_height, (i + 1) * cell_width,
                               fill=board[i][j])
    for i, j in snake.segments[:-1]:
        c.create_rectangle(j * cell_height, i * cell_width, (j + 1) * cell_height, (i + 1) * cell_width,
                           fill="green")
    i, j = snake.segments[-1]
    c.create_rectangle(j * cell_height, i * cell_width, (j + 1) * cell_height, (i + 1) * cell_width,
                       fill="red")


def f():
    draw(board, snake)
    snake.move()
    window.after(1000, f)


window = tkinter.Tk()
width = height = 600
n = m = 10
cell_width = width // m
cell_height = height // n
c = tkinter.Canvas(window, width=width, height=height, bg='white')
c.pack()

board = [["gray"] * m for i in range(n)]
snake = Snake()
draw(board, snake)

window.after(1000, f)

window.mainloop()
