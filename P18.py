import tkinter as tk

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (9.0 / 5.0) * (k - 273.0) + 32.0

def calc_temps():
    error_var.set("")
    entry_kelvin.config(bg="white")

    k_text = entry_kelvin.get().strip()

    if k_text == "":
        error_var.set("Kelvin cannot be blank.")
        entry_kelvin.config(bg="#ffcccc")
        clear_results()
        return

    try:
        k_value = float(k_text)
    except:
        error_var.set("Kelvin must be a number.")
        entry_kelvin.config(bg="#ffcccc")
        clear_results()
        return

    if k_value == 0:
        error_var.set("Kelvin cannot be zero.")
        entry_kelvin.config(bg="#ffcccc")
        clear_results()
        return

    if k_value < 0:
        error_var.set("Kelvin cannot be negative.")
        entry_kelvin.config(bg="#ffcccc")
        clear_results()
        return

    c = kelvin_to_celsius(k_value)
    f = kelvin_to_fahrenheit(k_value)

    entry_celsius.delete(0, tk.END)
    entry_celsius.insert(0, f"{c:.2f}")

    entry_fahrenheit.delete(0, tk.END)
    entry_fahrenheit.insert(0, f"{f:.2f}")

def clear_results():
    entry_celsius.delete(0, tk.END)
    entry_fahrenheit.delete(0, tk.END)

def clear_all():
    entry_kelvin.delete(0, tk.END)
    clear_results()
    error_var.set("")
    entry_kelvin.config(bg="white")

root = tk.Tk()
root.title("Temperature Conversion")

label_title = tk.Label(root, text="Temperature Conversion", font=("Arial", 14, "bold"))
label_title.grid(row=0, column=0, columnspan=3, pady=10)

tk.Label(root, text="Kelvin:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_kelvin = tk.Entry(root, width=15)
entry_kelvin.grid(row=1, column=1)

tk.Label(root, text="Celsius:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_celsius = tk.Entry(root, width=15)
entry_celsius.grid(row=2, column=1)

tk.Label(root, text="Fahrenheit:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_fahrenheit = tk.Entry(root, width=15)
entry_fahrenheit.grid(row=3, column=1)

error_var = tk.StringVar()
label_error = tk.Label(root, textvariable=error_var, fg="red")
label_error.grid(row=4, column=0, columnspan=3)

btn_calc = tk.Button(root, text="CALC", width=10, command=calc_temps)
btn_calc.grid(row=5, column=0, pady=10)

btn_clear = tk.Button(root, text="CLEAR", width=10, command=clear_all)
btn_clear.grid(row=5, column=1, pady=10)

btn_quit = tk.Button(root, text="QUIT", width=10, command=root.destroy)
btn_quit.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
