import tkinter as tk
import project.presentation.States.State as State
import project.presentation.States.MainState as MainState


class EvaluationPvoutState(State.State):
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
            MainState.MainState.get_state(self.app)), font=(self.app.font, 13))
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
