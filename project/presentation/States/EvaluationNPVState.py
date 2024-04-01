import project.presentation.States.State as State
import project.presentation.States.MainState as MainState
import tkinter as tk


class EvaluationNPVState(State.State):
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
            MainState.MainState.get_state(self.app)), font=(self.app.font, 13))
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
