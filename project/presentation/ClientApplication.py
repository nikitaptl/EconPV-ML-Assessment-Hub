from __future__ import annotations
import tkinter as tk
from tkinter import messagebox
from project.domain.Predictor import Predictor
from project.presentation.State import State, MainState


class ClientApplication(tk.Tk):
    valuePvout = None
    valueNPV = None
    valueKWP = None
    font = "Arial"
    predictor = Predictor()
    state: State = None

    def __init__(self, font="Arial"):
        super().__init__()
        self.geometry("600x400")
        self.title("EconPV")
        self.font = font
        self.state = MainState.get_state(self)
        self.state.buildInterface()

    def switch_interface(self, new_state):
        self.state.destroyInterface()
        self.state = new_state
        self.state.buildInterface()

    def confirm_pvout_evaluation(self):
        a = self.a_entry.get()
        b = self.b_entry.get()
        c = self.c_entry.get()

        response = self.predictor.predictPvout(DNI=a, DIF=b, TEMP=c)
        if response.is_succesful:
            self.valuePvout = round(response.message, 3)
            self.switch_interface(MainState.get_state(self))
        else:
            messagebox.showerror("Error", response.message)

    def confirm_npv_evaluation(self):
        a = self.cost_entry.get()
        b = self.pvout_entry.get()
        c = self.demand_entry.get()

        response = self.predictor.predictNPV(a, b, c)
        if response.is_succesful:
            self.valueNPV = round(response.message, 3)
            self.valueKWP = round(self.predictor.predictKWP(a, b, c).message, 1)
            self.switch_interface(MainState.get_state(self))
        else:
            messagebox.showerror("Error", response.message)

    def update_pvout_label(self):
        if (self.valuePvout != None):
            self.pvout_label.config(text=f"PVOUT = {self.valuePvout}")
        else:
            self.pvout_label.config(text=f"PVOUT = –")

    def update_npv_label(self):
        if (self.valueNPV != None):
            self.npv_label.config(text=f"NPV = {self.valueNPV}")
        else:
            self.npv_label.config(text=f"NPV = –")

    def update_kwp_label(self):
        if (self.valueKWP != None):
            self.kwp_label.config(text=f"KWP = {self.valueKWP}")
        else:
            self.kwp_label.config(text=f"KWP = –")

    def update_text(self):
        self.text_result.delete("1.0", "end")
        if (self.valueNPV != None):
            new_text = "dd"
            if (self.valueNPV < 0):
                new_text = f"К сожалению, установка солнечной батареи в этом месте и в этих условиях не является экономически выгодной, ведь чистая приведённая стоимость отрицательная: {self.valueNPV}"
            elif (0 <= self.valueNPV <= 10000):
                new_text = f"Установка солнечной батареи в этом месте и в этих условиях окупится, но её экономический потенциал невелик, ведь чистая приведённая стоимость равна {self.valueNPV}"
            else:
                new_text = f"Установка солнечной батареи в этом месте и в этих условиях имеет большой экономический потенциал! Чистая приведённая стоимость составила {self.valueNPV}"
            self.text_result.insert(tk.END, new_text)

app = ClientApplication("Montserrat")
app.mainloop()
