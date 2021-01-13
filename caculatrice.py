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
ecran.pack(fill=tk.X, padx=10, pady=10)
result.pack(fill=tk.X, padx=10, pady=10)

# callback

def calcul():
    try:
        content = result.get()
        result.delete(0, tk.END)
        calcul =  eval(f"{ecran['text']} {content}")
        ecran['text'] = ""
        result.insert(0, f"{calcul}")
    except ValueError:
        pass
  
def insertNumber(nb):
    content = result.get()
    result.delete(0, tk.END)
    result.insert(0, f"{content}{nb}")
def insertSigne(signe):
    if signe != '=':
        content = result.get()
        if len(content) > 0:
            result.delete(0, tk.END)
            ecran['text'] = f"{ecran['text']} {content} {signe}"
    else:
        calcul()

def delete(btn):
    if btn == 'C':
        result.delete(0, tk.END)
    elif btn == 'CE':
        ecran['text'] = ""
        result.delete(0, tk.END)
    elif btn == '<<':
        last = len(result.get())
        result.delete(last - 1)

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
# buttons signe
signes = ('/', '*', '-', '+', '=')
nb_row = 0
for signe in signes:
    button = tk.Button(master=button_frame,text=f"{signe}", command= lambda x=signe: insertSigne(x))
    button.grid(row=nb_row,column=4)
    nb_row += 1
# button zero
button_zero = tk.Button(master=button_frame,text="0",command=lambda x=0: insertNumber(x))
button_zero.grid(row=4, column=1)
# button virgule
button_virgule = tk.Button(master=button_frame,text=",",command=lambda x='.': insertNumber(x))
button_virgule.grid(row=4, column=2)
# buttons deletes
btn_deletes = ('CE', 'C', '<<')
nb_col= 0
for btn in btn_deletes:
    button = tk.Button(master=button_frame,text=f"{btn}", command= lambda x=btn: delete(x))
    button.grid(row=0,column=nb_col)
    nb_col += 1

# START
window.mainloop()
