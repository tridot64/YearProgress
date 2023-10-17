from tkinter import *
from datetime import date

today = date.today()
today = today.strftime("%d/%m/%y")

def update_date():
    with open("C:/Users/Rohith/Desktop/app_draw/test_date.txt","w") as file:
        str = today
        file.write(today)

def read_date():
    with open("C:/Users/Rohith/Desktop/app_draw/test_date.txt","r") as file:
        return file.readline()

def app():
    window = Tk()

    window.geometry("1080x720")

    window.attributes('-fullscreen',True)

    update_date()

    file_path = "C:/Users/Rohith/Desktop/app_draw/test.txt"

    def reg_up():
        with open(file_path,"a") as f:
            f.write("1,")
        window.destroy()

    def reg_down():
        with open(file_path,"a") as f:
            f.write("-1,")
        window.destroy()

    def reg_mid():
        with open(file_path,"a") as f:
            f.write("0,")
        window.destroy()

    buttonu = Button(window, text="Up",command=reg_up )
    buttonm = Button(window, text="mid",command=reg_mid )
    buttond = Button(window, text="down",command=reg_down )
    buttonu.pack(pady=20)
    buttonm.pack(pady=60)
    buttond.pack(pady=100)
    window.mainloop()

def main():
    if(read_date() != today):
        app()
    else:
        exit()


main()