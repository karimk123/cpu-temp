



#solution for tkinter and win32 APi



import tkinter, win32api, win32con, pywintypes, wmi, playsound,subprocess, os




#getting CPU temperature

root = tkinter.Tk()



fraps_color = "#F6F705"
red_color = "#ef0928"

temp_sign = '°C'

started = False


os.startfile("OpenHardwareMonitor.exe")

label = tkinter.Label(text = "loading..." , font=('Arial','30'), fg=fraps_color, bg='black')
label.master.overrideredirect(True)
label.master.geometry("-25+0")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "black")

hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
# http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
# The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)



label.pack(padx=0.9, pady=0.1)
#label.destroy()

#while True:

 #   print("")


def temp_checker():
    global label
    global temp_sign
    global started

    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    
    

    
    

    for sensor in temperature_infos:
                if sensor.SensorType==u'Temperature' and sensor.Name == "CPU Package":
                    
                    label.config(text = (" "+str(sensor.Value)) + " " + temp_sign)
                    started = True
                    if sensor.Value >= 70:
                         playsound.playsound('alarm.mp3')

   
    
    
    if temperature_infos == [] and started:
        root.destroy()
        exit()
    root.after(1000, temp_checker)

   
        



  





root.after(1000, temp_checker)
label.mainloop()

