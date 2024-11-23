from threading import Thread
import sqlite3
from pprint import pprint
from tkinter import *
from tkinter.ttk import Combobox, Radiobutton, Treeview
from tkinter import messagebox



class Transport():
    def __init__(self, h, w, l1, m, name):
        self.h = h
        self.w = w
        self.l1 = l1
        self.m = m
        self.name = name

    def get_inf(self):
        print("тип: ", self.name, "\nгрузоподъёмность: ", self.m, "\nдлина: ", self.l1, "\nширина: ", self.w, "\nвысота: ", self.h)


def fnew():
    global window1
    window1 = Tk()
    window1.title("add transport")
    window1.geometry("600x400")
    lab = Label(window1, text="выберите транспорт")
    lab.grid(row=0, column=0)
    global com
    com = Combobox(window1, width=20)
    com['values'] = ('газель', 'бычок', 'MAN-10', 'фура')
    com.current(0)
    
    columns2 = ("name", "m", "l1", "w", "h", "n")
    tree = Treeview(window1, columns=columns2, show="headings")
    tree.grid(row = 0, column=1, rowspan=5)
    tree.heading("name", text="тип", anchor=W)
    tree.heading("m", text="грузоподъёмность", anchor=W)
    tree.heading("l1", text="длина", anchor=W)
    tree.heading("w", text="ширина", anchor=W)
    tree.heading("h", text="высота", anchor=W)
    tree.heading("n", text="количество", anchor=W)
    tree.column('#1', stretch=NO, width=60)
    tree.column('#2', stretch=NO, width=120)
    tree.column('#3', stretch=NO, width=50)
    tree.column('#4', stretch=NO, width=60)
    tree.column('#5', stretch=NO, width=50)
    tree.column('#6', stretch=NO, width=80)
    cur.execute('''SELECT * FROM tTr''')
    for i in cur.fetchall():
        tree.insert('', END, values=i)
    com.grid(row=1, column=0)
    b12 = Button(window1, text="Выбрать", command=vib)
    b12.grid(row=2, column=0)


def vib():
    na = com.get()
    if na == "газель":
        k = 0
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="газель"''')
                n = cur.fetchall()[0][5]
                trans1[k][5] = n + 1
                cur.execute('''DELETE FROM tTr WHERE name="газель"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break

    elif na == "бычок":                                      
        k = 1
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="бычок"''')
                n = cur.fetchall()[0][5]
                trans1[k][5] = n + 1
                cur.execute('''DELETE FROM tTr WHERE name="бычок"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break

    elif na == "MAN-10":
        k = 2
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="MAN-10"''')
                n = cur.fetchall()[0][5]
                trans1[k][5] = n + 1
                cur.execute('''DELETE FROM tTr WHERE name="MAN-10"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break

    elif na == "фура":
        k = 3
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="фура"''')
                n = cur.fetchall()[0][5]
                trans1[k][5] = n + 1
                cur.execute('''DELETE FROM tTr WHERE name="фура"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break
    columns2 = ("name", "m", "l1", "w", "h", "n")
    tree = Treeview(window1, columns=columns2, show="headings")
    tree.grid(row = 0, column=1, rowspan=5)
    tree.heading("name", text="тип", anchor=W)
    tree.heading("m", text="грузоподъёмность", anchor=W)
    tree.heading("l1", text="длина", anchor=W)
    tree.heading("w", text="ширина", anchor=W)
    tree.heading("h", text="высота", anchor=W)
    tree.heading("n", text="количество", anchor=W)
    tree.column('#1', stretch=NO, width=60)
    tree.column('#2', stretch=NO, width=120)
    tree.column('#3', stretch=NO, width=50)
    tree.column('#4', stretch=NO, width=60)
    tree.column('#5', stretch=NO, width=50)
    tree.column('#6', stretch=NO, width=80)
    cur.execute('''SELECT * FROM tTr''')
    for i in cur.fetchall():
        tree.insert('', END, values=i)
    
    tree11 = Treeview(window, columns=columns2, show="headings")
    tree11.grid(row = 3, column=0, rowspan=3, columnspan=2)
    tree11.heading("name", text="тип", anchor=W)
    tree11.heading("m", text="грузоподъёмность", anchor=W)
    tree11.heading("l1", text="длина", anchor=W)
    tree11.heading("w", text="ширина", anchor=W)
    tree11.heading("h", text="высота", anchor=W)
    tree11.heading("n", text="количество", anchor=W)
    tree11.column('#1', stretch=NO, width=60)
    tree11.column('#2', stretch=NO, width=120)
    tree11.column('#3', stretch=NO, width=50)
    tree11.column('#4', stretch=NO, width=60)
    tree11.column('#5', stretch=NO, width=50)
    tree11.column('#6', stretch=NO, width=80)
    cur.execute('''SELECT * FROM tTr''')
    for i in cur.fetchall():
        tree11.insert('', END, values=i)
    
    cur.execute('''SELECT * FROM tTr''')
    print(cur.fetchall())

def delit():
    na = com2.get()
    if na == "газель":
        k = 0
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="газель"''')
                n = cur.fetchall()[0][5]
                if n > 0:
                    trans1[k][5] = n - 1
                else:
                    trans1[k][5] = n
                cur.execute('''DELETE FROM tTr WHERE name="газель"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break
    elif na == "бычок":                                      
        k = 1
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="бычок"''')
                n = cur.fetchall()[0][5]
                if n > 0:
                    trans1[k][5] = n - 1
                else:
                    trans1[k][5] = n
                cur.execute('''DELETE FROM tTr WHERE name="бычок"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break

    elif na == "MAN-10":
        k = 2
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="MAN-10"''')
                n = cur.fetchall()[0][5]
                if n > 0:
                    trans1[k][5] = n - 1
                else:
                    trans1[k][5] = n
                cur.execute('''DELETE FROM tTr WHERE name="MAN-10"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break

    elif na == "фура":
        k = 3
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="фура"''')
                n = cur.fetchall()[0][5]
                if n > 0:
                    trans1[k][5] = n - 1
                else:
                    trans1[k][5] = n
                cur.execute('''DELETE FROM tTr WHERE name="фура"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break
    columns2 = ("name", "m", "l1", "w", "h", "n")
    com2.grid(row=1, column=0)
    tree = Treeview(window2, columns=columns2, show="headings")
    tree.grid(row = 0, column=1, rowspan=5)
    tree.heading("name", text="тип", anchor=W)
    tree.heading("m", text="грузоподъёмность", anchor=W)
    tree.heading("l1", text="длина", anchor=W)
    tree.heading("w", text="ширина", anchor=W)
    tree.heading("h", text="высота", anchor=W)
    tree.heading("n", text="количество", anchor=W)
    tree.column('#1', stretch=NO, width=60)
    tree.column('#2', stretch=NO, width=120)
    tree.column('#3', stretch=NO, width=50)
    tree.column('#4', stretch=NO, width=60)
    tree.column('#5', stretch=NO, width=50)
    tree.column('#6', stretch=NO, width=80)
    cur.execute('''SELECT * FROM tTr''')
    for i in cur.fetchall():
        tree.insert('', END, values=i)


    tree11 = Treeview(window, columns=columns2, show="headings")
    tree11.grid(row = 3, column=0, rowspan=3, columnspan=2)
    tree11.heading("name", text="тип", anchor=W)
    tree11.heading("m", text="грузоподъёмность", anchor=W)
    tree11.heading("l1", text="длина", anchor=W)
    tree11.heading("w", text="ширина", anchor=W)
    tree11.heading("h", text="высота", anchor=W)
    tree11.heading("n", text="количество", anchor=W)
    tree11.column('#1', stretch=NO, width=60)
    tree11.column('#2', stretch=NO, width=120)
    tree11.column('#3', stretch=NO, width=50)
    tree11.column('#4', stretch=NO, width=60)
    tree11.column('#5', stretch=NO, width=50)
    tree11.column('#6', stretch=NO, width=80)
    cur.execute('''SELECT * FROM tTr''')
    for i in cur.fetchall():
        tree11.insert('', END, values=i)


    
    cur.execute('''SELECT * FROM tTr''')
    print(cur.fetchall())


def delit1():
    na = na1
    if na == "газель":
        k = 0
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="газель"''')
                n = cur.fetchall()[0][5]
                if n > 0:
                    trans1[k][5] = n - 1
                else:
                    trans1[k][5] = n
                cur.execute('''DELETE FROM tTr WHERE name="газель"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break
    elif na == "бычок":                                      
        k = 1
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="бычок"''')
                n = cur.fetchall()[0][5]
                if n > 0:
                    trans1[k][5] = n - 1
                else:
                    trans1[k][5] = n
                cur.execute('''DELETE FROM tTr WHERE name="бычок"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break

    elif na == "MAN-10":
        k = 2
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="MAN-10"''')
                n = cur.fetchall()[0][5]
                if n > 0:
                    trans1[k][5] = n - 1
                else:
                    trans1[k][5] = n
                cur.execute('''DELETE FROM tTr WHERE name="MAN-10"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break

    elif na == "фура":
        k = 3
        cur.execute('''SELECT * FROM tTr''')
        for i in range(len(cur.fetchall())):
            cur.execute('''SELECT * FROM tTr''')
            if na in cur.fetchall()[i]:
                cur.execute('''SELECT * FROM tTr''')
                cur.execute('''SELECT * FROM tTr WHERE name="фура"''')
                n = cur.fetchall()[0][5]
                if n > 0:
                    trans1[k][5] = n - 1
                else:
                    trans1[k][5] = n
                cur.execute('''DELETE FROM tTr WHERE name="фура"''')
                conn.commit()
                cur.execute('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1[k])
                conn.commit()
                cur.execute('''SELECT * FROM tTr''')
                print(cur.fetchall())
                break


def fdel():
    global window2
    window2 = Tk()
    window2.title("add transport to delete")
    window2.geometry("600x400")
    lab = Label(window2, text="выберите транспорт")
    lab.grid(row=0, column=0)
    global com2
    com2 = Combobox(window2, width=20)
    com2['values'] = ('газель', 'бычок', 'MAN-10', 'фура')
    com2.current(0)

    columns2 = ("name", "m", "l1", "w", "h", "n")

    com2.grid(row=1, column=0)
    tree = Treeview(window2, columns=columns2, show="headings")
    tree.grid(row = 0, column=1, rowspan=5)

    tree.heading("name", text="тип", anchor=W)
    tree.heading("m", text="грузоподъёмность", anchor=W)
    tree.heading("l1", text="длина", anchor=W)
    tree.heading("w", text="ширина", anchor=W)
    tree.heading("h", text="высота", anchor=W)
    tree.heading("n", text="количество", anchor=W)


    tree.column('#1', stretch=NO, width=60)
    tree.column('#2', stretch=NO, width=120)
    tree.column('#3', stretch=NO, width=50)
    tree.column('#4', stretch=NO, width=60)
    tree.column('#5', stretch=NO, width=50)
    tree.column('#6', stretch=NO, width=80)


    cur.execute('''SELECT * FROM tTr''')

    for i in cur.fetchall():
        tree.insert('', END, values=i)

    b22 = Button(window2, text="Выбрать", command=delit)
    b22.grid(row=2, column=0)

def app():
    m0 = int(e1.get())
    l0 = int(e2.get())
    w0 = int(e3.get())
    h0 = int(e4.get())
    cur.execute('''SELECT * FROM tTr''')
    for i in cur.fetchall():
        print("i", i[0], i)
        m = i[1]
        l = i[2]
        w = i[3]
        h = i[4]
        n = i[5]
        print(m, l, w, h, n)
        print(m0, l0, w0, h0)
        if m0 < 0 or l0 < 0 or w0 < 0 or h0 < 0 or m0 > 20 or m0 > 20 or l0 > 13 or w0 > 2 or h0 > 3:
            lab311["text"] = "некорректное описание"
        elif m >= m0 and l >= l0 and w >= w0 and h >= h0 and n > 0:
            print("hi")
            global na1
            na1 = i[0]
            print("na", na1)
            delit1()
            lab311["text"] = "заявка успешна"
            
            orders.append([na1, m0, l0, w0, h0])
            print("or", orders)
            break
        else:
            lab311["text"] = "нет подходящего транспорта"
    columns3 = ["name", "m", "l", "w", "h", "n"]
    tree3 = Treeview(window3, columns=columns3, show="headings")
    tree3.grid(row = 1, column=2, rowspan=5)

    tree3.heading("name", text="транспорт", anchor=W)
    tree3.heading("m", text="масса", anchor=W)
    tree3.heading("l", text="длина", anchor=W)
    tree3.heading("w", text="ширина", anchor=W)
    tree3.heading("h", text="высота", anchor=W)


    tree3.column('#1', stretch=NO, width=70)
    tree3.column('#2', stretch=NO, width=60)
    tree3.column('#3', stretch=NO, width=60)
    tree3.column('#4', stretch=NO, width=60)
    tree3.column('#5', stretch=NO, width=60)

    for i in orders:
        tree3.insert('', END, values=i)


    tree12 = Treeview(window, columns=columns3, show="headings")
    tree12.grid(row=3, column=2, rowspan=3) #columnspan=1)

    tree12.heading("name", text="транспорт", anchor=W)
    tree12.heading("m", text="масса", anchor=W)
    tree12.heading("l", text="длина", anchor=W)
    tree12.heading("w", text="ширина", anchor=W)
    tree12.heading("h", text="высота", anchor=W)


    tree12.column('#1', stretch=NO, width=70)
    tree12.column('#2', stretch=NO, width=60)
    tree12.column('#3', stretch=NO, width=60)
    tree12.column('#4', stretch=NO, width=60)
    tree12.column('#5', stretch=NO, width=60)

    #print("orders", orders)
    for i in orders:
        tree12.insert('', END, values=i)

    columns2 = ("name", "m", "l1", "w", "h", "n")
        
    tree11 = Treeview(window, columns=columns2, show="headings")
    tree11.grid(row = 3, column=0, rowspan=3, columnspan=2)
    tree11.heading("name", text="тип", anchor=W)
    tree11.heading("m", text="грузоподъёмность", anchor=W)
    tree11.heading("l1", text="длина", anchor=W)
    tree11.heading("w", text="ширина", anchor=W)
    tree11.heading("h", text="высота", anchor=W)
    tree11.heading("n", text="количество", anchor=W)
    tree11.column('#1', stretch=NO, width=60)
    tree11.column('#2', stretch=NO, width=120)
    tree11.column('#3', stretch=NO, width=50)
    tree11.column('#4', stretch=NO, width=60)
    tree11.column('#5', stretch=NO, width=50)
    tree11.column('#6', stretch=NO, width=80)
    cur.execute('''SELECT * FROM tTr''')
    for i in cur.fetchall():
        tree11.insert('', END, values=i)
#    print("qwerty")



def appl():
    global window3
    window3 = Tk()
    window3.title("add application")
    window3.geometry("800x400")
    lab3 = Label(window3, text="введите параметры груза")
    lab3.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    lab31 = Label(window3, text="масса:")
    lab31.grid(row=1, column=0)
    lab32 = Label(window3, text="длина:")
    lab32.grid(row=2, column=0)
    lab33 = Label(window3, text="ширина:")
    lab33.grid(row=3, column=0)
    lab34 = Label(window3, text="высота:")
    lab34.grid(row=4, column=0)

    
    global e1
    e1 = Entry(window3, width=20)
    e1.grid(row=1, column=1)
    global e2
    e2 = Entry(window3, width=20)
    e2.grid(row=2, column=1)
    global e3
    e3 = Entry(window3, width=20)
    e3.grid(row=3, column=1)
    global e4
    e4 = Entry(window3, width=20)
    e4.grid(row=4, column=1)

    b3 = Button(window3, text="подобрать транспорт", command=app)
    b3.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    global lab311
    lab311 = Label(window3)
    lab311.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    
    lab312 = Label(window3, text="заявки:")
    lab312.grid(row=0, column=2)

if __name__ == "__main__":

    trans = [("газель", "2", "3", "2", "1.7 - 2.2"), ("бычок", "3", "4.2 - 5", "2 - 2.2", "2 - 2.4"), 
    ("MAN-10", "10", "6-8", "2.45", "2.3 - 2.7"), ("фура", "20", "13.6", "2.46", "2.5 - 2.7")]
    #print(trans[0][0])
    columns = ("name", "m", "l1", "w", "h")
    trans1 = [["газель", 2, 3, 2, 2, 0], ["бычок", 3, 5, 2, 2, 0], 
    ["MAN-10", 10, 8, 2, 2, 0], ["фура", 20, 13, 2, 3, 0]]
    #print(trans1[0])
    orders = []



    conn = sqlite3.connect("transport.db")
    cur = conn.cursor()
    #cur.execute('''DROP TABLE tTr;''')

    cur.execute('''CREATE TABLE IF NOT EXISTS tTr (name TEXT, m INT, l1 INT, w INT, h INT, n INT)''')
    conn.commit()
    #cur.executemany('''INSERT INTO tTr (name, m, l1, w, h, n) VALUES (?, ?, ?, ?, ?, ?);''', trans1)
    conn.commit()
    cur.execute('''SELECT * FROM tTr''')
    print("x", cur.fetchall())

    conn.commit()

    window = Tk()
    window.title("transport")
    window.geometry("900x500")
    b1 = Button(text="удалить\n транспорт", command=fdel)
    b1.grid(column=0, row=0)

    b2 = Button(text="добавить\n транспорт", command=fnew)
    b2.grid(column=1, row=0)

    b3 = Button(text="подобрать и забронировать транспорт", command=appl)
    b3.grid(column=0, row=1, columnspan=2, padx=10)

    lab111 = Label(window, text="заявки:")
    lab111.grid(row=2, column=2)

    lab112 = Label(window, text="доступный транспорт:")
    lab112.grid(row=2, column=0)


    #print("cur", cur.fetchall())
    #print("order", orders)
    window.mainloop()
    conn.close()
