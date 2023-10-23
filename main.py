from tkinter import *
from datetime import date

today = date.today()
today = today.strftime("%d/%m/%y")



def update_date():
    with open("test_date.txt","w") as file: 
        file.write(today)

def read_date():
    with open("test_date.txt","r") as file:
        return file.readline()
 
ans = read_date()
missed_days = int(today[0:2]) - int(ans[0:2])


def app():
    window = Tk()

    window.geometry("1080x720")

    window.attributes('-fullscreen',True)

    file_path = "test.txt"
 

    def kill():
        update_date()
        window.destroy()

    def reg_up():
        with open(file_path,"a") as f:
            f.write("1,")
        global missed_days
        if(missed_days != 0):
            missed_days = missed_days - 1
        if(missed_days == 0):
            kill()

    def reg_down():
        with open(file_path,"a") as f:
            f.write("-1,")
        global missed_days
        if(missed_days != 0):
            missed_days = missed_days - 1
        if(missed_days == 0):
            kill()

    def reg_mid():
        with open(file_path,"a") as f:
            f.write("0,")
        global missed_days
        if(missed_days != 0):
            missed_days = missed_days - 1
        if(missed_days == 0):
            kill()

    

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