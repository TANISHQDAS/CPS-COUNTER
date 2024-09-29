import tkinter as tk
import time
from tkinter import messagebox

class CPS:
    def __init__(self, root):
        self.root = root
        self.root.title("CPS Counter")

        self.clicks = 0
        self.start_time = None
        self.countdown_time = 10
        self.after_id = None

        root.configure(bg='pink')

        self.label = tk.Label(root, text="Click the button as fast as you can!", font=("Arial", 14), fg="darkblue", bg='pink')
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="Click", command=self.start_click, font=("Arial", 14, "bold"), width=15, height=2, bg="orange", fg="red")
        self.button.pack(pady=20)

        self.countdown_label = tk.Label(root, text=f"Time: {self.countdown_time}", font=("Arial", 14), fg='green', bg='pink')
        self.countdown_label.pack(pady=20)

        self.result_label = tk.Label(root, text="CPS: 0", font=("Arial", 14), fg='magenta', bg='pink')
        self.result_label.pack(pady=20)

        self.retry_button = tk.Button(root, text="WANT TO TRY AGAIN", command=self.re_sta, font=("Arial", 14), fg="red")
        self.retry_button.pack(pady=20)
        self.retry_button.pack_forget()

    def start_click(self):
        if self.start_time is None:
            self.start_time = time.time()
            self.root.after(1000, self.countdown)
        self.click()

    def click(self):
        self.clicks += 1

    def countdown(self):
        if self.countdown_time > 0:
            self.countdown_time -= 1
            self.countdown_label.config(text=f"Time: {self.countdown_time}")
            self.after_id = self.root.after(1000, self.countdown)
        else:
            self.cal_cps()

    def cal_cps(self):
        duration = time.time() - self.start_time if self.start_time else 0
        cps = self.clicks / duration if duration > 0 else 0
        self.result_label.config(text=f"CPS: {cps:.2f}")
        self.button.config(state="disabled")

        if cps > 14.1:
            messagebox.askquestion("Auto Clicker?", "Your CPS is unusually high. Are you using an auto-clicker?")

        self.retry_button.pack()

    def re_sta(self):
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        self.clicks = 0
        self.start_time = None
        self.countdown_time = 10

        self.countdown_label.config(text=f"Time: {self.countdown_time}")
        self.result_label.config(text="CPS: 0")
        self.button.config(state="normal")
        self.retry_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = CPS(root)
    root.mainloop()

