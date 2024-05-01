import serial
from NewData_Function import update_state, check_exi
import sqlite3
import pandas as pd
from Interface_Creation import open_ihm
import keyboard

##Creating a variable to store the RFID tag value
var_com = ''
'''
ser = serial.Serial('COM3', 115200)'''
    #######################################################################
while True:
    '''while True: ##Insert values through ESP 32
        var = str(ser.read(1))
        var_com = str(var_com+var)
        if var == "b\'\\n\'":
            break
    var_com = var_com.replace("b\'", '').replace("\'", '').replace("\\r", '').replace("\\n", '')
    ############################################################################
    print(var_com)'''

    while True: ##Insert values manually
        def get_input():
            print("Pressione a tecla desejada para abrir o comando input.")

            # Função para verificar se a tecla desejada foi pressionada
            def on_key_press(event):
                if event.name == 'r':  # Substitua 's' pela tecla desejada
                    var_com = str(input("Digite o valor desejado: "))
                    print(var_com)
                    keyboard.unhook_all()
            keyboard.on_press(on_key_press)
            keyboard.wait()

        if __name__ == "__main__":
            get_input()

##Condition in which the tag is already registered.
    if (check_exi("banco_db","ESP","DATA_READ",var_com)) == True:
        update_state("banco_db","ESP", var_com)
        print("Object updated in the DB")
        conn = sqlite3.connect("banco_db")
        cur = conn.cursor()
        var_com = ''

##Condition in which the tag isn't yet registered.
    else:
        open_ihm("banco_db", "ESP", var_com) ##COMANDO PARA CHAMAR A IHM
        print("Objeto cadastrado no BD")
        var_com = ''






