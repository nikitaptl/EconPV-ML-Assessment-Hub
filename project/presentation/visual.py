import tkinter as tk

def switch_to_input():
    input_frame.pack()
    main_frame.pack_forget()

def switch_to_main():
    main_frame.pack()
    input_frame.pack_forget()

def process_input():
    input_data = entry.get()
    result_label.config(text="Вы ввели: " + input_data)
    switch_to_main()

root = tk.Tk()
root.title("Переключение между экранами")

root.geometry("400x200")

# Основной фрейм
main_frame = tk.Frame(root)
main_frame.pack()

main_label = tk.Label(main_frame, text="Главный экран")
main_label.pack()

input_button = tk.Button(main_frame, text="Ввод данных", command=switch_to_input)
input_button.pack()

# Фрейм для ввода данных
input_frame = tk.Frame(root)

input_label = tk.Label(input_frame, text="Введите данные:")
input_label.pack()

entry = tk.Entry(input_frame)
entry.pack()

confirm_button = tk.Button(input_frame, text="Подтвердить", command=process_input)
confirm_button.pack()

result_label = tk.Label(input_frame, text="")
result_label.pack()

# Показываем только основной фрейм в начале
switch_to_main()

root.mainloop()