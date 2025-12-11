import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Canvas Face")

    canvas_width = 400
    canvas_height = 400
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    canvas.create_oval(50, 50, 350, 350, outline="lime", width=4)

    canvas.create_oval(110, 110, 170, 170, fill="red", outline="red")
    canvas.create_oval(230, 110, 290, 170, fill="blue", outline="blue")

    canvas.create_rectangle(105, 90, 175, 100, fill="black", outline="black")
    canvas.create_rectangle(225, 90, 295, 100, fill="black", outline="black")

    canvas.create_rectangle(130, 210, 270, 235, fill="yellow", outline="yellow")

    canvas.create_polygon(
        130, 280,
        270, 280,
        200, 340,
        fill="black"
    )

    root.mainloop()

main()
