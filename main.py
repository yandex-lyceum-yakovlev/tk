import tkinter


class Snake:
    dx = 1
    dy = 0
    segments = [[2, 2], [2, 3], [2, 4]]

    def move(self):
        self.segments = self.segments[1:] + [[self.segments[-1][0] + self.dy, self.segments[-1][1] + self.dx]]
        # for p in self.segments:
        #     p[0] += self.dy
        #     p[1] += self.dx

    def key_press(self, event):
        if event.keysym == "Up":
            self.dx, self.dy = 0, -1
        if event.keysym == "Down":
            self.dx, self.dy = 0, 1
        if event.keysym == "Left":
            self.dx, self.dy = -1, 0
        if event.keysym == "Right":
            self.dx, self.dy = 1, 0


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
window.bind_all('<KeyPress>', snake.key_press)
window.after(1000, f)

window.mainloop()
