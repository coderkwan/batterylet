import subprocess
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x200")
root.title("Battery Alert")
root.resizable(FALSE,FALSE)

root.columnconfigure(0, weight=1)

def close():
    root.destroy()

fraim = ttk.Frame(root, padding=(3,3,12,12)).grid(column=0,row=0)

ttk.Label(fraim,text="Low Battery, Please Recharge!").grid(column=0,row=1)

myimg = ImageTk.PhotoImage(Image.open('./lowbattery_icon.png'))
ttk.Label(fraim,image=myimg).grid(column=0,row=2)

ttk.Button(fraim, text="Okay!",command=close).grid(column=0, row=3)

def run():
    root.mainloop()


def main():
    battery_state = subprocess.check_output("upower --show-info $(upower --enumerate | grep 'BAT') | grep -E 'state' | awk '{print $2}'", shell=True)
    battery_level  = subprocess.check_output("upower --show-info $(upower --enumerate | grep 'BAT') | grep -E 'percentage' | awk '{print $2}'", shell=True)

    num_battery_level = (int(str(battery_level)[2:-4]))
    str_battery_state = (str(battery_state)[2:-3])

    if(num_battery_level < 20 and str_battery_state == "discharging"):
        run()
        return 0
    else:
        return 0


main()
