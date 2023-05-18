import tkinter as tk
import pyperclip

class Credentials:
    def __init__(self, CARD, PASSWORD, LOGIN_TIMER):
        self.card = CARD
        self.password = PASSWORD
        self.remaining_time = LOGIN_TIMER

    def display_credentials(self):
        def copy_username():
            pyperclip.copy(self.card)

        def copy_password():
            pyperclip.copy(self.password)

        root = tk.Tk()
        root.title("Credentials")
        root.geometry("300x150")
        root.attributes('-topmost', True)

        # Create a label to display the remaining time
        self.timer_label = tk.Label(root)
        self.timer_label.pack()

        self.update_timer(root)

        copy_username_button = tk.Button(root, text="Copy Username", command=copy_username)
        copy_username_button.pack()

        copy_password_button = tk.Button(root, text="Copy Password", command=copy_password)
        copy_password_button.pack()

        root.mainloop()

    def update_timer(self, root):
        # Update the timer label with the remaining time
        self.timer_label.config(text=f"Time remaining: {self.remaining_time} seconds")

        if self.remaining_time > 0:
            # Decrement the remaining time and update the timer after 1 second
            self.remaining_time -= 1
            root.after(1000, self.update_timer, root)
        else:
            # If the time is up, destroy the Tkinter window
            root.destroy()
