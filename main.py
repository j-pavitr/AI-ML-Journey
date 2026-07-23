import tkinter as tk

class Countdown:
    def __init__(self, root, minutes):
        self.root = root
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="black")

        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.remaining = minutes * 60

        self.label = tk.Label(
            root,
            font=("Arial", 120, "bold"),
            fg="white",
            bg="black"
        )
        self.label.pack(expand=True)

        self.update()

    def update(self):
        mins = self.remaining // 60
        secs = self.remaining % 60

        self.label.config(text=f"{mins:02}:{secs:02}")

        if self.remaining > 0:
            self.remaining -= 1
            self.root.after(1000, self.update)
        else:
            self.label.config(text="TIME'S UP!")

root = tk.Tk()
Countdown(root, 188)
root.mainloop()