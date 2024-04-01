import project.presentation.States.State as State
import project.presentation.States.EvaluationPvoutState as EvaluationPvoutState
import project.presentation.States.EvaluationNPVState as EvaluationNPVState
import project.presentation.States.RegionEnergyCostState as RegionEnergyCostState
import tkinter as tk


class MainState(State.State):
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
                                                       EvaluationPvoutState.EvaluationPvoutState.get_state(self.app)),
                                                   font=(self.app.font, 13))
        self.app.evaluate_pvout_button.pack()

        self.app.space2 = tk.Label(self.app, text="")
        self.app.space2.pack(pady=0)
        self.app.evaluate_npv_button = tk.Button(self.app, text="Оценить NPV",
                                                 command=lambda: self.app.switch_interface(
                                                     EvaluationNPVState.EvaluationNPVState.get_state(self.app)),
                                                 font=(self.app.font, 13))
        self.app.evaluate_npv_button.pack()

        self.app.space3 = tk.Label(self.app, text="")
        self.app.space3.pack(pady=0)
        self.app.find_region_price = tk.Button(self.app, text="Найти цену электроэнергии в регионе РФ",
                                                 command=lambda: self.app.switch_interface(
                                                     RegionEnergyCostState.RegionEnergyCostState.get_state(self.app)),
                                                 font=(self.app.font, 11))
        self.app.find_region_price.pack()

        self.app.space4 = tk.Label(self.app, text="")
        self.app.space4.pack(pady=0)
        self.app.get_info = tk.Button(self.app, text="Справка",
                                               font=(self.app.font, 11))
        self.app.get_info.pack()

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
        self.app.space3.destroy()
        self.app.find_region_price.destroy()
        self.app.space4.destroy()
        self.app.get_info.destroy()
        self.app.text_result.destroy()
