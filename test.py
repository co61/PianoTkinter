

import sys
import serial

print("Your platform is : " ,sys.platform)
major=sys.version_info.major
minor=sys.version_info.minor
print("Your python version is : ",major,minor)
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 and minor==6 :
    import tkinter as tk
    from tkinter import filedialog
else :
    print("with your python version : ",major,minor)
    print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 



print("Hello world")

mw = tk.Tk() 
mw.geometry("360x300")
mw.title("Leçon de Piano")
#mw.mainloop()

ser = serial.Serial("COM5", 9600)
while True:
    cc=str(ser.readline())
    msg = cc[2:][:-9]
    print("message : ",msg)
    values=msg.split()
    print(values[0])