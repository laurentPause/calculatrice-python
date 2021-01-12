import tkinter as tk
window = tk.Tk()

# Frames
result_frame = tk.Frame(master=window, width=300, height=100, bg="gray")
result_frame.pack(fill=tk.X)

button_frame = tk.Frame(master=window, width=300, height=100, bg="black")
button_frame.columnconfigure(0)
button_frame.rowconfigure(0)
button_frame.pack(fill=tk.BOTH, expand=True)


# Results
ecran = tk.Label(master=result_frame)
result = tk.Entry(master=result_frame, width=40,)
ecran.pack(fill=tk.X,padx=10, pady=10)
result.pack(fill=tk.X, padx=10, pady=10)

# callback
def insertNumber(nb):
    content = result.get()
    result.delete(0, tk.END)
    result.insert(0, f"{content}{nb}")
def insertSigne(signe):
    content = result.get()
    result.delete(0, tk.END)
    ecran['text'] = f"{ecran['text']} {content} {signe}"

# Buttons

# buttons number
number = 7
for row  in range(1,4):
    for col in range(3):
        nb = number
        button = tk.Button(master=button_frame,
                           text=f"{number}", command=lambda x=nb: insertNumber(x))
        button.grid(row=row, column=col)
        number += 1
    number -= 6
#buttons signe
signes = ('/', '*', '-', '+', '=')
nb_row = 0
for signe in signes:
    button = tk.Button(master=button_frame,text=f"{signe}", command= lambda x=signe: insertSigne(x))
    button.grid(row=nb_row,column=4)
    nb_row += 1

# START
window.mainloop()
