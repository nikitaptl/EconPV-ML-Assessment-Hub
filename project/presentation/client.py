import tkinter as tk
from tkinter import messagebox
from project.domain.Predictor import Predictor, Response

class App(tk.Tk):
    value = None
    predictor = Predictor()

    def __init__(self):
        super().__init__()
        self.build_main_interface()

    def build_main_interface(self):
        self.title("PVOUT Evaluation")
        self.geometry("600x400")

        text_pvout = f"PVOUT: {self.value}" if self.value != None else "PVOUT = -"
        self.pvout_label = tk.Label(self, text=text_pvout, font=("Arial", 16))
        self.pvout_label.pack(pady=20)
        self.update_pvout(self.value)

        self.evaluate_button = tk.Button(self, text="Evaluate PVOUT", command=self.switch_interface)
        self.evaluate_button.pack()

        self.interface_state = "main"

    def switch_interface(self):
        if self.interface_state == "main":
            self.interface_state = "evaluation"
            self.create_evaluation_interface()
        else:
            self.interface_state = "main"
            self.destroy_evaluation_interface()
            self.destroy_main_interface()
            self.build_main_interface()

    def create_evaluation_interface(self):
        self.interface_state = "evaluation"
        self.a_label = tk.Label(self, text="Введите DNI")
        self.a_label.pack()

        self.a_entry = tk.Entry(self)
        self.a_entry.pack()

        self.b_label = tk.Label(self, text="Введите DIF")
        self.b_label.pack()

        self.b_entry = tk.Entry(self)
        self.b_entry.pack()

        self.c_label = tk.Label(self, text="Введите среднюю температуру: ")
        self.c_label.pack()

        self.c_entry = tk.Entry(self)
        self.c_entry.pack()

        self.confirm_button = tk.Button(self, text="Подтвердить", command=self.confirm_evaluation)
        self.confirm_button.pack()

        self.back_button = tk.Button(self, text="Back", command=self.switch_interface)
        self.back_button.pack()

        self.evaluate_button.config(state=tk.DISABLED)

    def confirm_evaluation(self):
        a = self.a_entry.get()
        b = self.b_entry.get()
        c = self.c_entry.get()

        responce = self.predictor.predictPvout(DNI = a, DIF = b, TEMP = c)
        if responce.is_succesful:
            value = responce.message
            print(value)
            self.switch_interface()
        else:
            messagebox.showerror("Error", responce.message)

    def destroy_evaluation_interface(self):
        self.a_label.destroy()
        self.a_entry.destroy()
        self.b_label.destroy()
        self.b_entry.destroy()
        self.c_label.destroy()
        self.c_entry.destroy()
        self.confirm_button.destroy()
        self.back_button.destroy()

        self.evaluate_button.config(state=tk.NORMAL)

    def destroy_main_interface(self):
        self.pvout_label.destroy()
        self.evaluate_button.destroy()

    def update_pvout(self, value):
        self.pvout_label.config(text=f"PVOUT: {value}")

app = App()
app.mainloop()