import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tools import Taiwan_AQI

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #建立AQI的實體
        aqi_data = Taiwan_AQI()

        mainFrame = ttk.Frame(self)
        mainFrame.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)
        # 上面的Frame
        topFrame = ttk.Frame(mainFrame, height=100)
        topFrame.pack(fill=tk.X)

        ttk.Label(topFrame, text="台灣即時AQI資訊", font=(
            'Helvetica', '20')).pack(pady=(20, 20))
        #下面的Frame
        bottomFrame = ttk.Frame(mainFrame)
        bottomFrame.pack(expand=True, fill=tk.BOTH)

        self.messageText = tk.Text(
            bottomFrame, height=15, width=35, state=tk.DISABLED, takefocus=0, bd=0)
        self.messageText.pack()

        bad5 =aqi_data.get_bad(n=5)
        good5 =aqi_data.get_better(n=5)
        #顯示訊息
        message =""
        #最好的站點訊息
        message += "目前AQI最好的5個站點\n"
        for item in good5:
            siteString = f"{item.site_name},{item.county},{item.aqi}\n"
            message += siteString
        message += "=====================\n"
        #最差的站點訊息
        message += "\n目前AQI最差的5個站點\n"

        for item in bad5:
            siteString = f"{item.site_name},{item.county},{item.aqi}\n"
            message += siteString
        
        self.messageText.configure(state=tk.NORMAL)
        self.messageText.delete("1.0", tk.END)
        self.messageText.insert(tk.END,message)
        self.messageText.configure(state=tk.DISABLED)
def main():
    window = Window()
    window.title('台灣即時AQI資訊')
    window.mainloop()

if __name__ == "__main__":
    main()
