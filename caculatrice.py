import tkinter as tk
window = tk.Tk()

# Frames
result_frame = tk.Frame(master=window, width=300, height=100, bg="gray")
result_frame.pack(fill=tk.X)

button_frame = tk.Frame(master=window, width=300, height=100, bg="black")
button_frame.columnconfigure(1, minsize=100)
button_frame.rowconfigure(1, minsize=3)
button_frame.pack(fill=tk.BOTH, expand=True)


# Results
ecran = tk.Label()
result = tk.Entry(master=result_frame, width=40,)
ecran.pack(fill=tk.X,padx=10, pady=10)
result.pack(fill=tk.X, padx=10, pady=10)


def test(nb):
    content = result.get()
    result.delete(0, tk.END)
    result.insert(0, f"{content}{nb}")

# Buttons


number = 7
for i in range(3):
    for j in range(3):
        nb = number
        button = tk.Button(master=button_frame,
                           text=f"{number}", width=3, height=3, command=lambda x=nb: test(x))
        button.grid(row=i, column=j)
        number += 1
    number -= 6


# START
window.mainloop()
