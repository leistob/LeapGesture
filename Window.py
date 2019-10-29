import Tkinter as tK
from Event import *


class Window:

    def callback_x(self, *args):
        # Take all data and put it in array
        # data_arr = []
        # data_arr.append()
        Event(UI_VAL_CHANGED, self.slider_var_x.get())

    def __init__(self):
        self.listener = None
        self.canvas = None

        self.w = tK.Tk()
        self.w.title("Gesture Controller")
        self.w.minsize(width=600, height=400)
        self.w.pack_propagate(0)
        self.w.iconbitmap(r'Icon.ico')
        self.w.protocol("WM_DELETE_WINDOW", self.delete_window)

        self.slider_var_x = tK.DoubleVar()
        self.slider_var_x.trace("w", self.callback_x)
        self.slider_var_y = tK.DoubleVar()
        self.slider_var_y.trace("w", self.callback_x)
        self.slider_var_z = tK.DoubleVar()
        self.slider_var_z.trace("w", self.callback_x)

        # self.slider = ttK.Scale(from_=-1, to=1, orient=tK.HORIZONTAL, length=450,
        #                        variable=self.slider_var)
        self.slider = tK.Scale(from_=-1, to=1, orient=tK.HORIZONTAL, resolution=0.01, length=450,
                               variable=self.slider_var_x)
        # self.slider.bind("<ButtonRelease-1>", self.reset_slider)

        self.label = tK.Label(master=self.w, text="CONNECTED")
        self.slider.pack()
        self.create_canvas()
        self.label.pack()

        # self.create_connected_frame()

    def create_connected_frame(self):
        frame = tK.Frame(self.w, bg="blue", width=200, height=200)
        tK.Label(frame, text="label").pack()
        frame.pack()
        frame.config(bg="red")

    def create_canvas(self):
        width = 450
        height = 20
        self.canvas = tK.Canvas(self.w, width=width - 2, height=height - 2, bg="black")
        col_cd_1 = "#%02x%02x%02x" % (231, 0, 29)  # RED
        col_cd_2 = "#%02x%02x%02x" % (171, 70, 6)
        col_cd_3 = "#%02x%02x%02x" % (236, 102, 2)
        col_cd_4 = "#%02x%02x%02x" % (255, 210, 0)
        # col_cd_5 = "#%02x%02x%02x" % (109, 170, 44)
        col_cd_6 = "#%02x%02x%02x" % (50, 188, 77)
        col_cd_7 = "#%02x%02x%02x" % (0, 154, 56)
        col_cd_8 = "#%02x%02x%02x" % (0, 153, 153)  # PETROL

        colors = [col_cd_1, col_cd_2, col_cd_3, col_cd_4, "OliveDrab1", col_cd_6, col_cd_7, col_cd_8]

        for i in range(len(colors)):
            val = i * ((width * 0.5) / len(colors))
            self.canvas.create_rectangle(val, 0, width - val, height, fill=colors[i], outline="", width=0)
        self.canvas.create_line(width / 2, 0, width / 2, height, fill="black", dash=(4, 4))
        self.canvas.pack()

    def reset_slider(self):
        self.set_slider_val(0)

    def set_slider_val(self, val):
        self.slider_var_x.set(val)

    def delete_window(self):
        self.w.destroy()

    def start_ui(self):
        self.w.mainloop()
