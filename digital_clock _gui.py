'''
     pylint verification has to be done yet
     '''
import tkinter
import time
 
window = tkinter.Tk() 

window.title('Clock') 
  
def time_it():
    while 1:
        string_2 = str(time.strftime('%H:%M:%S %a'))
        var_digi.set(string_2)
        time.sleep(1)
        window.update()

var_digi = tkinter.StringVar()

digi_clock = tkinter.Label(window, textvariable = var_digi, font = ('calibri',  40,  'bold'), background = 'purple', foreground = 'white') 

digi_clock.grid(row = 0)

time_it() 
  
window.mainloop()
