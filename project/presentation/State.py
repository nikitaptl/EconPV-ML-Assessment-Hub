from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import tkinter as tk
from tkinter import messagebox


class State(ABC):
    app = None

    def __init__(self, application):
        self.app = application

    @staticmethod
    def get_state(application):
        return State(application)

    @abstractmethod
    def buildInterface(self) -> None:
        pass

    @abstractmethod
    def destroyInterface(self) -> None:
        pass


class MainState(State):
    @staticmethod
    def get_state(application):
        return MainState(application)

    def buildInterface(self) -> None:
        # pvout_label
        self.app.pvout_description = tk.Label(self.app, font=(self.app.font, 9),
                                              text="Это выходная мощность солнечных батарей")
        self.app.pvout_description.pack(pady=0)

        self.app.pvout_label = tk.Label(self.app, font=(self.app.font, 16))
        self.app.pvout_label.pack(pady=0)
        self.app.update_pvout_label()

        # npv_label
        self.app.npv_description = tk.Label(self.app, font=(self.app.font, 9),
                                            text="Это прибыль или убыток от солнечной батареи")
        self.app.npv_description.pack(pady=0)

        self.app.npv_label = tk.Label(self.app, font=(self.app.font, 16))
        self.app.npv_label.pack(pady=0)
        self.app.update_npv_label()

        # kwp_label
        self.app.kwp_description = tk.Label(self.app, font=(self.app.font, 9),
                                            text="Это оптимальная максимальная мощность солнечной батареи")
        self.app.kwp_description.pack(pady=0)

        self.app.kwp_label = tk.Label(self.app, font=(self.app.font, 16))
        self.app.kwp_label.pack(pady=0)
        self.app.update_kwp_label()
        self.app.space1 = tk.Label(self.app, text="")
        self.app.space1.pack(pady=0)

        # Кнопки
        self.app.evaluate_pvout_button = tk.Button(self.app, text="Оценить PVOUT",
                                                   command=lambda: self.app.switch_interface(
                                                       EvaluationPvoutState.get_state(self.app)),
                                                   font=(self.app.font, 13))
        self.app.evaluate_pvout_button.pack()

        self.app.space2 = tk.Label(self.app, text="")
        self.app.space2.pack(pady=0)

        self.app.evaluate_npv_button = tk.Button(self.app, text="Оценить NPV",
                                                 command=lambda: self.app.switch_interface(
                                                     EvaluationNPVState.get_state(self.app)),
                                                 font=(self.app.font, 13))
        self.app.evaluate_npv_button.pack()
        # Текст, говорящий о том, эффективна ли модель.
        self.app.text_result = tk.Text(self.app)
        self.app.text_result.pack(side="bottom", fill="both", expand=True)
        self.app.update_text()


    def destroyInterface(self) -> None:
        self.app.pvout_description.destroy()
        self.app.pvout_label.destroy()
        self.app.space1.destroy()
        self.app.npv_description.destroy()
        self.app.npv_label.destroy()
        self.app.kwp_description.destroy()
        self.app.kwp_label.destroy()
        self.app.space2.destroy()
        self.app.evaluate_pvout_button.destroy()
        self.app.evaluate_npv_button.destroy()
        self.app.text_result.destroy()




class EvaluationPvoutState(State):
    @staticmethod
    def get_state(application):
        return EvaluationPvoutState(application)

    def buildInterface(self) -> None:
        self.app.a_label = tk.Label(self.app, text="Введите DNI", font=(self.app.font, 12))
        self.app.a_label.pack()

        self.app.a_entry = tk.Entry(self.app, font=(self.app.font, 12))
        self.app.a_entry.pack()

        self.app.b_label = tk.Label(self.app, text="Введите DIF", font=(self.app.font, 12))
        self.app.b_label.pack()

        self.app.b_entry = tk.Entry(self.app, font=(self.app.font, 12))
        self.app.b_entry.pack()

        self.app.c_label = tk.Label(self.app, text="Введите среднюю температуру ", font=(self.app.font, 12))
        self.app.c_label.pack()

        self.app.c_entry = tk.Entry(self.app, font=(self.app.font, 12))
        self.app.c_entry.pack()

        self.app.space = tk.Label(self.app, text="")
        self.app.space.pack(pady=0)
        self.app.confirm_button = tk.Button(self.app, text="Подтвердить", command=self.app.confirm_pvout_evaluation,
                                            font=(self.app.font, 13))
        self.app.confirm_button.pack()

        self.app.back_button = tk.Button(self.app, text="Назад", command=lambda: self.app.switch_interface(
            MainState.get_state(self.app)), font=(self.app.font, 13))
        self.app.back_button.pack()

    def destroyInterface(self) -> None:
        self.app.a_label.destroy()
        self.app.a_entry.destroy()
        self.app.b_label.destroy()
        self.app.b_entry.destroy()
        self.app.c_label.destroy()
        self.app.c_entry.destroy()
        self.app.space.destroy()
        self.app.confirm_button.destroy()
        self.app.back_button.destroy()




class EvaluationNPVState(State):
    @staticmethod
    def get_state(application):
        return EvaluationNPVState(application)

    def buildInterface(self) -> None:
        self.app.cost_label = tk.Label(self.app, text="Введите цену электроэнергии (руб/кВт⋅ч)",
                                       font=(self.app.font, 12))
        self.app.cost_label.pack()

        self.app.cost_entry = tk.Entry(self.app, font=(self.app.font, 12))
        self.app.cost_entry.pack()

        self.app.pvout_label = tk.Label(self.app, text="Введите PVOUT", font=(self.app.font, 12))
        self.app.pvout_label.pack()

        self.app.pvout_entry = tk.Entry(self.app, font=(self.app.font, 12))
        self.app.pvout_entry.pack()
        if (self.app.valuePvout != None):
            self.app.pvout_entry.insert(0, self.app.valuePvout)

        self.app.demand_label = tk.Label(self.app, text="Введите расход электроэнергии в месяц (кВт⋅ч): ",
                                         font=(self.app.font, 12))
        self.app.demand_label.pack()

        self.app.demand_entry = tk.Entry(self.app, font=(self.app.font, 12))
        self.app.demand_entry.pack()

        self.app.space = tk.Label(self.app, text="")
        self.app.space.pack(pady=0)
        self.app.confirm_button = tk.Button(self.app, text="Подтвердить", command=self.app.confirm_npv_evaluation,
                                            font=(self.app.font, 13))
        self.app.confirm_button.pack()

        self.app.back_button = tk.Button(self.app, text="Назад", command=lambda: self.app.switch_interface(
            MainState.get_state(self.app)), font=(self.app.font, 13))
        self.app.back_button.pack()

    def destroyInterface(self) -> None:
        self.app.cost_label.destroy()
        self.app.cost_entry.destroy()
        self.app.pvout_label.destroy()
        self.app.pvout_entry.destroy()
        self.app.demand_label.destroy()
        self.app.demand_entry.destroy()
        self.app.space.destroy()
        self.app.confirm_button.destroy()
        self.app.back_button.destroy()