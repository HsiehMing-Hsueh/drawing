import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFomt
from PIL import Image,ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #
        ttkStyle = ttk.Style()
        ttkStyle.theme_use("default")
        ttkStyle.configure("white.TLabelframe", background="white",bd=0)
        ttkStyle.configure("white.TLabelframe.Ladel", background = "white",foreground="red")
        #畫圖的Frame
        drawingFrame = ttk.LabelFrame(self, text="這裡是畫圖區",style="white.TLabelframe")
        drawingFrame.pack(padx=50, pady=50)
        #畫線
        lineCanvas = tk.Canvas(drawingFrame, width=100,height=30, background="white", bd=0,highlightthickness=0)
        lineCanvas.create_line((0,0),(100,0),width=30,fill="red")
        lineCanvas.pack()
        #畫圓
        ovalCanvas = tk.Canvas(drawingFrame, width=110, height=110,background="white", bd=0, highlightthickness=0)
        ovalCanvas.create_oval((10,10),(100,100),width=10,outline="red",fill="purple")
        ovalCanvas.pack()
        #文字
        f1 = tkFomt.Font(family="Helvetica",size=16,weight="bold")
        textCanvas = tk.Canvas(drawingFrame, width=110, height=110,background="white", bd=0, highlightthickness=0)
        textCanvas.create_text(0,0,text="abc_中文",font=f1,fill="green",anchor="nw")
        textCanvas.pack()
        #地圖
        mapCanvas = tk.Canvas(drawingFrame, width=110, height=110,background="white", bd=0, highlightthickness=0)
        taiwanImage = Image.open("map.png")
        newImage = taiwanImage.resize((100,100),Image.LANCZOS)
        self.taiwanImageTk = ImageTk.PhotoImage(newImage)
        mapCanvas.create_image(0,0,image=self.taiwanImageTk,anchor=tk.NW)
        mapCanvas.create_text(100, 100, text="abc_中文", font=tkFomt.Font(family="Helvetica", size=16),anchor="nw")
        mapCanvas.pack()

def main():
    window = Window()
    window.title('畫圖')
    window.mainloop()

if __name__ == "__main__":
    main()