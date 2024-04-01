from __future__ import annotations
import tkinter as tk
from tkinter import messagebox
from project.domain.Predictor import Predictor
from project.presentation.InterfaceStates.State import State, MainState, EvaluationPvoutState


class App(tk.Tk):
    valuePvout = None
    valueNPV = None
    font = "Arial"
    predictor = Predictor()
    state : State = None

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
            self.switch_interface(MainState.get_state(self))
            self.valuePvout = response.message
            self.update_pvout_label()
        else:
            messagebox.showerror("Error", response.message)

    def confirm_npv_evaluation(self):
        a = self.cost_entry.get()
        b = self.pvout_entry.get()
        c = self.demand_entry.get()

        response = self.predictor.predictNPV(a, b, c)
        if response.is_succesful:
            self.switch_interface(MainState.get_state(self))
            self.valueNPV = response.message
            self.update_npv_label()
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


app = App("Montserrat")
app.mainloop()
