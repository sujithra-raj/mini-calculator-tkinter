import tkinter as tk
BG = "#F6F1F8"
CARD = "#FFF7FB"
ACCENT = "#CDB4DB"
ACCENT2 = "#FFC8DD"
TEXT = "#4A4A4A"
TOGGLE_OFF = "#444"
TOGGLE_ON = "#7dd3fc"      # pastel blue
KNOB = "#ffffff"
toggle_state = False
 
PASTEL = {
    "bg": "#F8F4FF",
    "entry": "#FFF7FC",
    "button": "#CDB4DB",
    "text": "#4A4A68",
    "accent": "#BDE0FE",
    "ico":"🌙 mode",
}
DARK = {
    "bg": "#1E1E2E",
    "entry": "#2A2A3D",    #0B1956
    "button": "#3A3A5A",
    "text": "#EAEAF0",
    "accent": "#89B4FA",
    "ico":"☀ mode",
}
BTN_STYLE = {
    "font": ("Courier New", 11, "bold"),
    "relief": "flat",
    "bd": 0,
    "padx": 14,
    "pady": 6,
}

current_theme= PASTEL
root=tk.Tk() #creares window
root.title("MINI CALCULATOR")
#root.config(bg=BG)


title=tk.Label(root, text= "Mini Calculator", font=("Courier New",18,"bold"))
title.pack(pady=15)

n= tk.StringVar()
m=tk.StringVar()

def onu(text): #only number checking fn. checks every key
    return text.isdigit() or text == ""
vcmd = root.register(onu)

input_frame=tk.Frame(root, bg=current_theme["bg"],padx=15,pady=15)
input_frame.pack(pady=10)
topbar=tk.Frame(input_frame, bg=current_theme["bg"])
topbar.grid(row=0,column=0,sticky="ew")
input_frame.grid_columnconfigure(0, weight=1)
entry_box=tk.Frame(input_frame, bg=current_theme["entry"])
entry_box.grid(row=1, column=0, pady=10)
e1=tk.Entry(input_frame, textvariable=n, validate="key",
    validatecommand=(vcmd, "%P"))
e1.pack(in_=entry_box,pady=5)
e2=tk.Entry(input_frame, textvariable=m, validate="key",
    validatecommand=(vcmd, "%P"))
e2.pack(in_=entry_box, pady=5)
entry_style={  "font": ("Courier New", 12),
    "bg": "#FFFFFF",
    "fg": TEXT,
    "relief": "ridge",
    
    "insertbackground": TEXT}
e1.config(**entry_style)
e2.config(**entry_style)

def add():
    a=int(e1.get())
    b=int(e2.get())
    result_label.config(text=f"result: {a+b}")
    hisbox.insert(tk.END, f"{a}+{b}={a+b}\n")
def sub():
    a=int(e1.get())
    b=int(e2.get())
    result_label.config(text=f"Result: {a-b}")
    hisbox.insert(tk.END, f"{a}-{b}={a-b}\n")
def mul():
    a=int(e1.get())
    b=int(e2.get())
    result_label.config(text=f"Result: {a*b}")
    hisbox.insert(tk.END, f"{a}*{b}={a*b}\n")
def div():
    a=int(e1.get())
    b=int(e2.get())
    if b==0:
        result_label.config(text="Error: division by zero")
        hisbox.insert(tk.END, f"{a}/0 -> zero error\n")
    else:
        result_label.config(text=f"Result: {a/b}")
        hisbox.insert(tk.END, f"{a}/{b}={a/b}\n")
def clear():
    e1.delete(0, tk.END)
    e2.delete(0,tk.END)
    result_label.config(text="Result:")
def clrh():
    hisbox.delete(1.0, tk.END)
def checkent(*args):
    if n.get() and m.get():
        add_button.config(state="normal")
        sub_b.config(state="normal")
        mulb.config(state="normal")
        divb.config(state="normal")
    else:
        add_button.config(state="disabled")
        sub_b.config(state="disabled")
        mulb.config(state="disabled")
        divb.config(state="disabled")
def apply_theme(theme):
    root.config(bg=theme["bg"])

    e1.config(bg=theme["entry"], fg=theme["text"], insertbackground=theme["text"])
    e2.config(bg=theme["entry"], fg=theme["text"], insertbackground=theme["text"])
    entry_box.config(bg=theme["entry"] )
    result_label.config(bg=theme["bg"], fg=theme["text"])
    topbar.config(bg=theme["bg"])

    hisbox.config(bg=theme["entry"], fg=theme["text"], insertbackground=theme["text"])
    hisfr.config(bg=theme["bg"])
    input_frame.config(bg=theme["bg"])
    btnf.config(bg=theme["bg"])
    #root.config(bg=theme["bg"] )
    title.config(bg=theme["bg"],fg=theme["text"] )
    theme_btn.config(text=current_theme["ico"])



    for btn in (add_button, sub_b, mulb, divb, clrb, theme_btn):
        btn.config(bg=theme["button"], fg=theme["text"], activebackground=theme["accent"])
def toggle_theme():
    global current_theme
    if current_theme == PASTEL:
        current_theme=DARK
         
    else:
        current_theme=PASTEL
         
    apply_theme(current_theme)
    theme_btn.config(text=current_theme["ico"])
     

result_label = tk.Label(root,text="Result:", **BTN_STYLE)
result_label.pack(pady=10)
clrb=tk.Button(root, text = "clear", command= clear)
clrb.pack(pady=5)
btnf=tk.Frame(root, padx=15, pady=15, bg=current_theme["bg"])
btnf.pack(pady=15)
btnf.grid_columnconfigure(0, weight=1)
btnf.grid_columnconfigure(1, weight=1)

add_button = tk.Button(btnf, text="add", command=add, **BTN_STYLE)
add_button.grid(row=0,column=0,padx=8,pady=8)
#add_button.pack(pady = 3)
add_button.config(state="disabled")
sub_b = tk.Button(btnf, text="subtract", command= sub, **BTN_STYLE)
sub_b.grid(row=0, column=1, padx=8, pady=8)
#sub_b.pack(pady = 3)
sub_b.config(state="disabled")
mulb= tk.Button(btnf, text="multiply", command=mul, **BTN_STYLE)
mulb.grid(row=1, column=0, padx=8, pady=8)
#mulb.pack(pady= 3)
mulb.config(state="disabled")
divb=tk.Button(btnf, text="divide", command=div, **BTN_STYLE)
divb.grid(row=1, column=1, padx=8, pady=8)
#divb.pack(pady=3)
divb.config(state="disabled")
tk.Button(root, text="clear history  ", command=clrh).pack()
theme_btn = tk.Button(topbar,  text=current_theme["ico"], command=toggle_theme, bd=0, bg=current_theme["bg"],activebackground=current_theme["bg"])
theme_btn.config(
    relief="flat",
    highlightthickness=0,
    bd=0,
    padx=4,
    pady=4,
    cursor="hand2"
)
theme_btn.pack(side="right", padx=6)
'''btn_style = {
    "font": ("Courier New", 11, "bold"),
    "bg": ACCENT,
    "fg": TEXT,
    "activebackground": ACCENT2,
    "relief": "flat",
    "bd": 0,
    "padx": 12,
    "pady": 6
}

for btn in (add_button, sub_b, mulb, divb):
    btn.config(**btn_style)'''
#add_button.config(disabledforeground="#9A8FB0")
hisfr=tk.Frame(root, padx=10, pady=10, bg=current_theme["bg"])
hisfr.pack(pady=10)
scr=tk.Scrollbar(hisfr)
scr.pack(side=tk.RIGHT,fill=tk.Y)
hisbox=tk.Text(hisfr, height=8, width=30,font=("Courier New",10),relief="groove",bd=1,bg=current_theme["bg"], yscrollcommand=scr.set)
hisbox.pack(side=tk.LEFT)
scr.config(command=hisbox.yview)
#clrb.config(bg=ACCENT2)
n.trace_add("write",checkent)
m.trace_add("write",checkent)
apply_theme(PASTEL)

root.mainloop() #keeps it open
