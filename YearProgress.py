from tkinter import *
from datetime import date
from datetime import datetime
from datetime import timedelta
from pathlib import Path

today = date.today()
today_str = today.strftime("%d/%m/%y")

home = str(Path.home())

def update_date():
    with open(home + "\\AppData\\Local\\YearProgress\\curr_date.txt","w") as file: 
        file.write(today_str)

def read_date():
    with open(home + "\\AppData\\Local\\YearProgress\\curr_date.txt","r") as file:
        return file.readline()
 
ans = read_date()
var = "How was your day on " + ans
last_date = datetime.strptime(ans,"%d/%m/%y")
last_date = last_date.date()
missed_days = today - last_date
missed_days = missed_days.days


def app():
    window = Tk()

    window.geometry("1080x720")

    window.attributes('-fullscreen',True)

    global home
    file_path = home + "\\AppData\\Local\\YearProgress\\test.txt"
 

    def kill():
        update_date()
        window.destroy()

    def reg_up():
        with open(file_path,"a") as f:
            f.write("1,")
        global missed_days
        global Title
        if(missed_days != 0):
            missed_days = missed_days - 1
            day_iter = timedelta(days = missed_days)
            var = "How was your day on " + str(last_date + day_iter) 
            Title["text"] = var
        if(missed_days == 0):
            kill()

    def reg_down():
        with open(file_path,"a") as f:
            f.write("-1,")
        global missed_days
        global Title
        if(missed_days != 0):
            missed_days = missed_days - 1
            day_iter = timedelta(days = missed_days)
            var = "How was your day on " + str(last_date + day_iter) 
            Title["text"] = var
        if(missed_days == 0):
            kill()

    def reg_mid():
        with open(file_path,"a") as f:
            f.write("0,")
        global missed_days
        global Title
        if(missed_days != 0):
            missed_days = missed_days - 1
            day_iter = timedelta(days = missed_days)
            var = "How was your day on " + str(last_date + day_iter) 
            Title["text"] = var
        if(missed_days == 0):
            kill()

    def snooze():
        buttons.grid_remove()
        global missed_days
        if(missed_days == 1):
            window.destroy()
        global Title
        missed_days = missed_days - 1
        day_iter = timedelta(days = missed_days)
        var = "How was your day on " + str(last_date + day_iter) 
        Title["text"] = var
        

    global last_date
    global missed_days
    global Title
    day_iter = timedelta(days = missed_days)
    var = "How was your day on " + str(last_date + day_iter)
    Title = Label(window,text = var)
    buttonu = Button(window, text="Up",command=reg_up )
    buttonm = Button(window, text="mid",command=reg_mid )
    buttond = Button(window, text="down",command=reg_down )
    buttons = Button(window, text="snooze",command =snooze)
    buttonu.grid(row= 1,column=0)
    buttonm.grid(row= 2,column=0)
    buttond.grid(row= 3,column=0)
    buttons.grid(row=4,column=0)
    Title.grid(row= 0,column=0)
    window.mainloop()

def main():
    if(read_date() != today_str):
        app()
    else:
        exit()


main()