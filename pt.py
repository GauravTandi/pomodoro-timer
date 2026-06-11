import sys, time
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw() 


timer_set = sys.argv[1]
hr_min_sec = sys.argv[2]

if "hr" in hr_min_sec:
    print(f"setting time for {timer_set}hours")
    timer_set = int(timer_set * 60) * 60
    time.sleep(timer_set)
    print(f"{timer_set} hours timer finished.")
    messagebox.showinfo(title="Pomodoro Timer",message="Great work, timer finished")

elif "min" in hr_min_sec:
    print(f"setting time for {timer_set} minutes")
    timer_set = int(timer_set) * 60 
    time.sleep(timer_set)
    print(f"{timer_set} minutes timer finished.")
    messagebox.showinfo(title="Pomodoro Timer",message="Great work, timer finished")

elif "sec" in hr_min_sec:
    print(f"setting time for {timer_set} seconds")
    time.sleep(int(timer_set))
    print(f"{timer_set} seconds timer finished.")
    messagebox.showinfo(title="Pomodoro Timer",message="Great work, timer finished")

else:
    print("usage:- \npython pt.py 20min \npython pt.py 2 her  \npython pt.py 10 sec")

root.destroy()