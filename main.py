import tkinter

window = tkinter.Tk()

width = height = 600
n = m = 10
cell_width = width // m
cell_height = height // n
c = tkinter.Canvas(window, width=width, height=height, bg='white')
c.pack()

for i in range(n):
    for j in range(m):
        c.create_rectangle(i * cell_height, j*cell_width, (i + 1) * cell_height, (j+1) * cell_width, fill="red")

window.mainloop()
