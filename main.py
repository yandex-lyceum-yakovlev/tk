import tkinter


def draw(board):
    for j in range(m):
        for i in range(n):
            c.create_rectangle(j * cell_height, i * cell_width, (j + 1) * cell_height, (i + 1) * cell_width,
                               fill=board[i][j])

window = tkinter.Tk()

width = height = 600
n = m = 10
cell_width = width // m
cell_height = height // n
c = tkinter.Canvas(window, width=width, height=height, bg='white')
c.pack()

board = [["red"] * m for i in range(n)]
board[2][5] = "green"
board[3][2] = "blue"
draw(board)

window.mainloop()
