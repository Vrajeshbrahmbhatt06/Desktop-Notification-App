from socket import timeout
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from plyer import notification
import time

t = Tk()
t.title("Notifier-App")
t.geometry("500x400+300+200")
img = Image.open("notify-label.png")
tkimage = ImageTk.PhotoImage(img)

img_label = Label(t, image=tkimage).grid()

#creating function to get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
    
    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert","Fill all the fields !")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time*60
        messagebox.showinfo("Notifier Set","Do you want to set Notification ?")
        
        time.sleep(min_to_sec)
        
        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon="logo-icon.ico",
                            timeout=10)
        
        
        



#label 1
t_label = Label(t, text = "Title to notify", font=("poppins",10))
t_label.place(x=12, y=70)

#entry 1
title  = Entry(t, width="25", font=("poppins",13))
title.place(x=123 , y=70)

#label 2
m_label = Label(t, text = "Display message", font=("poppins",10))
m_label.place(x=12, y=120)

#entry 2
msg  = Entry(t, width="40", font=("poppins",13))
msg.place(x=125 , y=128 , height=30)

#label 3
time_label = Label(t, text="Set Time", font=("poppins",10))
time_label.place(x=12,y=175)

#entry 3
time1 = Entry(t, width="5", font=("poppins",13))
time1.place(x=123,y=175)


#label 4
time_min_label = Label(t, text="min", font=("poppins",10))
time_min_label.place(x=175, y=180)

#button
but = Button(t,text="SET NOTIFICATION",
             font=("poppins",10,'bold'), 
             fg='#ffffff', 
             bg="#528DFF", 
             width=20, 
             relief="raised",
             command = get_details)
but.place(x=170 , y=230)

t.resizable(0,0)
t.mainloop()