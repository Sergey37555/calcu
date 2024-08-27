import tkinter as tk

def get_values():
    num1 = int(namber1_entri.get())
    num2 = int(namber2_entri.get())
    return num1, num2
def insert_values(value):
    answer_entri.delete(0, 'end')
    answer_entri.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
        num1, num2 = get_values()
        res = num1 / num2
        insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)



windows = tk.Tk()
windows.title('Калькулятор')
windows.geometry('500x600')
windows.resizable(False,False)
button_add = tk.Button(windows,text='+',bg='red',width=7,height=3,command=add)
button_add.place(x=50,y=430)
button_sub = tk.Button(windows,text='-',bg='orange',width=7,height=3,command=sub)
button_sub.place(x=130,y=430)
button_mul = tk.Button(windows,text='/',bg='blue',width=7,height=3,command=div)
button_mul.place(x=130,y=500)
button_div = tk.Button(windows,text='*',bg='green',width=7,height=3,command=mul)
button_div.place(x=50,y=500)
namber1_entri = tk.Entry(windows,width=50,borderwidth=10,bg='yellow')
namber1_entri.place(x=100,y=75)
namber2_entri = tk.Entry(windows,width=50,borderwidth=10,bg='yellow')
namber2_entri.place(x=100,y=160)
answer_entri = tk.Entry(windows,width=50,borderwidth=50,bg='pink')
answer_entri.place(x=50,y=260)
namber1_entri = tk.Label(windows, text='Введите первое число')
namber1_entri.place(x=210,y=50)
namber2_entri = tk.Label(windows, text='Введите второе число')
namber2_entri.place(x=210,y=130)
answer_entri = tk.Label(windows, text='ОТВЕТ')
answer_entri.place(x=240,y=235)
windows.mainloop()