
from turtle import color
import psutil
from tkinter import *
from tkinter.scrolledtext import *
import sys
import os


root = Tk()             
root.wm_title("Traffic Monitoring")


# Open window having dimension 600x500 and red colour
root.geometry('700x520')
root.minsize(700,520)
root.maxsize(700,520)

root.configure(bg='black')
root.iconbitmap("fox_creative_craft_paper_origami_icon_226504.ico")

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent
running = False


#Function for traffic monitoring loop
# -----------------------------------------------
def main():
    if running:
     last_received = psutil.net_io_counters().bytes_recv
     last_sent = psutil.net_io_counters().bytes_sent
     last_total = last_received + last_sent
     # ints for monitoring
     bytes_received = psutil.net_io_counters().bytes_recv
     bytes_sent = psutil.net_io_counters().bytes_sent
     bytes_total = bytes_received + bytes_sent

     

     new_receievd = bytes_received - last_received
     new_sent = bytes_sent - last_sent
     new_total = bytes_total - last_total
     #summary
     mb_new_received = new_receievd / 1024
     mb_new_sent = new_sent / 1024
     mb_new_total = new_total / 1024
 
     
     
     
        
     
   #we will print it into the txt file so we can log it and open on a GUI
     with open("log.txt", "a") as f:
        print(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total", file=f)
     last_received = bytes_received
     last_sent = bytes_sent
     last_total = bytes_total
     d = open("log.txt")
     text_file = d.read()
     txtarea.insert(END, text_file)
     txtarea.see("end")
     f.close()
     root.after(1000, main)
     
     
txtarea = Text(root, width=50, height=20)
txtarea.pack(side="top")
   
    

      # Do your thing 
      # until 'stop_button' is clicked
# -----------------------------------------------

#Define a function to start the programm


def start_monitorting():
    global running
    running = True
    main()
   
    


def stop_monitorting():
    global running
    running = False
    


def clear_log():
    global running 
    open('log.txt', 'w').close()
    txtarea.delete("1.0","end")
    running = False



#Size of buttons a=x of a start b = y, same for c and d but for stop button
a=3 
b=50
c=2
d=50

# Create a Button
clear_button= Button(root, text = 'Clear', height=1, width=10,command = clear_log)
start_button = Button(root, text = 'Start Monitoring or speed up for more accuracy',height=a, width=b, fg='#ff0000', bg='#262626', font=('Times New Roman',14,'bold'),
                          command = start_monitorting)
stop_button = Button(root, text = 'Stop Monitoring',height=c, width=d, fg='#262626', bg='#ff0000',font=('Times New Roman',14,'bold'),
                          command = stop_monitorting)
#where it will be 
start_button.pack(side = 'bottom')
stop_button.pack(side = 'bottom')
clear_button.pack(side="left", padx=1, pady=1)
root.after(1000, main)

root.mainloop()