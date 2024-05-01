from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import sqlite3

##Creating a function to show the Tkinter Interface.
def open_ihm(banco, tabela, dado_lido):
##Main window configs
    jan = Tk()
    jan.title("Objects Register")
    jan.geometry("900x450")
    jan.configure(background="royalblue4")
    jan.resizable(width=False, height=False)

##Screen division in two frames
    LeftFrame = Frame(jan, width=395, height=450, bg="mediumpurple", relief="raise")
    LeftFrame.pack(side=LEFT)
    RightFrame = Frame(jan, width=500, height=450, bg="lightskyblue", relief="raise")
    RightFrame.pack(side=RIGHT)

##Icon and RFID image request
    jan.iconbitmap("tech_rfid_icon_158141.ico")
    RFID = PhotoImage(file="rfid-safehouse.png")

##Creating a label to insert the RFID Image
    RfidLabel = Label(RightFrame, image=RFID, bg="slateblue")
    RfidLabel.place(x=120, y=60)

##Creating design labels
    label_welcome = ttk.Label(LeftFrame, justify=CENTER, width=35, background="lightskyblue", foreground="royalblue4", text="Welcome to the objects register!", font=("Segoe UI Black", 15,))
    label_welcome.place(x=0, y=70)
    label_name = ttk.Label(LeftFrame, justify=CENTER, width=35, background="royalblue4", foreground="lightskyblue", text="Write the name of the object, please", font=("Century Gothic", 10))
    label_name.place(x=70, y=170)
    label_num = ttk.Label(LeftFrame, justify=CENTER, width=35, background="royalblue4", foreground="lightskyblue", text="Write the number of the object, please", font=("Century Gothic", 10))
    label_num.place(x=70, y=270)

##Creating input value fields
    entry_name = ttk.Entry(LeftFrame, width=30)
    entry_name.place(x=100, y=150)

    entry_number = ttk.Entry(LeftFrame, width=30)
    entry_number.place(x=100, y=250)

## Creating the function to insert a new object whithin database
    def insert():
        hora = datetime.datetime.now()
        number = str(entry_number.get())
        name = str(entry_name.get())
        conn = sqlite3.connect(banco)
        cur = conn.cursor()
        cur.execute("INSERT INTO " + tabela + " (DIA_HORA, DADO_LIDO, NUMERO_PATRIMONIO, NOME_PATRIMONIO, STATE) VALUES (?,?,?,?,1)",(hora, dado_lido, number, name))
        conn.commit()
        messagebox.showinfo(title="Objects Register", message="Your object has been correctly registered!")
        jan.destroy()

##Creating a button to perform the "Insert" function
    update_bd = ttk.Button(LeftFrame, text="Update database", width=60, command=insert)
    update_bd.place(x=10, y=350)

##Creating window loop
    jan.mainloop()
