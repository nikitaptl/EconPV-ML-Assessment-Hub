import tkinter as tk
import project.presentation.States.State as State
import project.presentation.States.MainState as MainState
from tkinter import messagebox


class RegionEnergyCostState(State.State):
    price = None

    @staticmethod
    def get_state(application):
        return RegionEnergyCostState(application)

    def buildInterface(self) -> None:
        self.app.region_price_label = tk.Label(self.app, font=(self.app.font, 16))
        self.app.region_price_label.pack(pady=0)
        self.update_price_label()

        self.app.request_label = tk.Label(self.app, text="Введите название региона", font=(self.app.font, 12))
        self.app.request_label.pack()

        self.app.request_entry = tk.Entry(self.app, font=(self.app.font, 12))
        self.app.request_entry.pack()

        self.app.space1 = tk.Label(self.app, text="")
        self.app.space1.pack(pady=0)
        self.app.confirm_button = tk.Button(self.app, text="Найти цену", command=self.confirm_search,
                                            font=(self.app.font, 13))
        self.app.confirm_button.pack()

        self.app.space2 = tk.Label(self.app, text="")
        self.app.space2.pack(pady=0)
        self.app.back_button = tk.Button(self.app, text="Назад", command=lambda: self.app.switch_interface(
            MainState.MainState.get_state(self.app)), font=(self.app.font, 13))
        self.app.back_button.pack()

    def destroyInterface(self) -> None:
        self.app.region_price_label.destroy()
        self.app.request_label.destroy()
        self.app.request_entry.destroy()
        self.app.space1.destroy()
        self.app.confirm_button.destroy()
        self.app.space2.destroy()
        self.app.back_button.destroy()

    def update_price_label(self):
        if (self.price != None):
            self.app.region_price_label.config(text=f"Тариф = {self.price} руб/кВт⋅ч")
        else:
            self.app.region_price_label.config(text=f"Тариф = –")

    def confirm_search(self):
        str = self.app.request_entry.get()

        response = self.app.check_region(str)
        if response.is_succesful:
            self.price = response.message
            self.update_price_label()
            self.app.request_entry.delete(0, 'end')
        else:
            messagebox.showerror("Error", response.message)
