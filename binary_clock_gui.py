'''
    pylint verification has to be done yet
    '''
import tkinter
import time
window = tkinter.Tk()
window.title("Binary Clock")

def test(x, y):
    try:
        return x[y]
    except:
        return '0'

def time_it():
    while 1:
        string  =  time.strftime('%H:%M:%S')
        
        h1 = bin(int(string[0]))[2:]
        h2 = bin(int(string[1]))[2:]

        m1 = bin(int(string[3]))[2:]
        m2 = bin(int(string[4]))[2:]

        s1 = bin(int(string[6]))[2:]
        s2 = bin(int(string[7]))[2:]
        
        var111.set(test(h1, -4))
        var121.set(test(h1, -3))
        var131.set(test(h1, -2))
        var141.set(h1[-1])

        var212.set(test(h2, -4))
        var222.set(test(h2, -3))
        var232.set(test(h2, -2))
        var242.set(h2[-1])

        var113.set(test(m1, -4))
        var123.set(test(m1, -3))
        var133.set(test(m1, -2))
        var143.set(m1[-1])

        var214.set(test(m2, -4))
        var224.set(test(m2, -3))
        var234.set(test(m2, -2))
        var244.set(m2[-1])

        var115.set(test(s1, -4))
        var125.set(test(s1, -3))
        var135.set(test(s1, -2))
        var145.set(s1[-1])

        var216.set(test(s2, -4))
        var226.set(test(s2, -3))
        var236.set(test(s2, -2))
        var246.set(s2[-1])

        time.sleep(1)
        window.update()
        

var111 = tkinter.StringVar()
var121 = tkinter.StringVar()
var131 = tkinter.StringVar()
var141 = tkinter.StringVar()

var212 = tkinter.StringVar()
var222 = tkinter.StringVar()
var232 = tkinter.StringVar()
var242 = tkinter.StringVar()

var113 = tkinter.StringVar()
var123 = tkinter.StringVar()
var133 = tkinter.StringVar()
var143 = tkinter.StringVar()

var214 = tkinter.StringVar()
var224 = tkinter.StringVar()
var234 = tkinter.StringVar()
var244 = tkinter.StringVar()

var115 = tkinter.StringVar()
var125 = tkinter.StringVar()
var135 = tkinter.StringVar()
var145 = tkinter.StringVar()

var216 = tkinter.StringVar()
var226 = tkinter.StringVar()
var236 = tkinter.StringVar()
var246 = tkinter.StringVar()
    

H111 = tkinter.Label(window, textvariable = var111, font = ('Arial', 10, 'bold'), background = 'yellow', foreground = 'black')
H121 = tkinter.Label(window, textvariable = var121, font = ('Arial', 10, 'bold'), background = 'yellow', foreground = 'black')
H131 = tkinter.Label(window, textvariable = var131, font = ('Arial', 10, 'bold'), background = 'yellow', foreground = 'black')
H141 = tkinter.Label(window, textvariable = var141, font = ('Arial', 10, 'bold'), background = 'yellow', foreground = 'black')

H212 = tkinter.Label(window, textvariable = var212, font = ('Arial', 10, 'bold'), background = 'yellow', foreground = 'black')
H222 = tkinter.Label(window, textvariable = var222, font = ('Arial', 10, 'bold'), background = 'yellow', foreground = 'black')
H232 = tkinter.Label(window, textvariable = var232, font = ('Arial', 10, 'bold'), background = 'yellow', foreground = 'black')
H242 = tkinter.Label(window, textvariable = var242, font = ('Arial', 10, 'bold'), background = 'yellow', foreground = 'black')

M113 = tkinter.Label(window, textvariable = var113, font = ('Arial', 10, 'bold'), background = 'red', foreground = 'white')
M123 = tkinter.Label(window, textvariable = var123, font = ('Arial', 10, 'bold'), background = 'red', foreground = 'white')
M133 = tkinter.Label(window, textvariable = var133, font = ('Arial', 10, 'bold'), background = 'red', foreground = 'white')
M143 = tkinter.Label(window, textvariable = var143, font = ('Arial', 10, 'bold'), background = 'red', foreground = 'white')

M214 = tkinter.Label(window, textvariable = var214, font = ('Arial', 10, 'bold'), background = 'red', foreground = 'white')
M224 = tkinter.Label(window, textvariable = var224, font = ('Arial', 10, 'bold'), background = 'red', foreground = 'white')
M234 = tkinter.Label(window, textvariable = var234, font = ('Arial', 10, 'bold'), background = 'red', foreground = 'white')
M244 = tkinter.Label(window, textvariable = var244, font = ('Arial', 10, 'bold'), background = 'red', foreground = 'white')

S115 = tkinter.Label(window, textvariable = var115, font = ('Arial', 10, 'bold'), background = 'orange', foreground = 'green')
S125 = tkinter.Label(window, textvariable = var125, font = ('Arial', 10, 'bold'), background = 'orange', foreground = 'green')
S135 = tkinter.Label(window, textvariable = var135, font = ('Arial', 10, 'bold'), background = 'orange', foreground = 'green')
S145 = tkinter.Label(window, textvariable = var145, font = ('Arial', 10, 'bold'), background = 'orange', foreground = 'green')

S216 = tkinter.Label(window, textvariable = var216, font = ('Arial', 10, 'bold'), background = 'orange', foreground = 'green')
S226 = tkinter.Label(window, textvariable = var226, font = ('Arial', 10, 'bold'), background = 'orange', foreground = 'green')
S236 = tkinter.Label(window, textvariable = var236, font = ('Arial', 10, 'bold'), background = 'orange', foreground = 'green')
S246 = tkinter.Label(window, textvariable = var246, font = ('Arial', 10, 'bold'), background = 'orange', foreground = 'green')


H111.grid(row = 1, column = 0)
H121.grid(row = 2, column = 0)
H131.grid(row = 3, column = 0)
H141.grid(row = 4, column = 0)

H212.grid(row = 1, column = 1)
H222.grid(row = 2, column = 1)
H232.grid(row = 3, column = 1)
H242.grid(row = 4, column = 1)

M113.grid(row = 1, column = 2)
M123.grid(row = 2, column = 2)
M133.grid(row = 3, column = 2)
M143.grid(row = 4, column = 2)

M214.grid(row = 1, column = 3)
M224.grid(row = 2, column = 3)
M234.grid(row = 3, column = 3)
M244.grid(row = 4, column = 3)

S115.grid(row = 1, column = 4)
S125.grid(row = 2, column = 4)
S135.grid(row = 3, column = 4)
S145.grid(row = 4, column = 4)

S216.grid(row = 1, column = 5)
S226.grid(row = 2, column = 5)
S236.grid(row = 3, column = 5)
S246.grid(row = 4, column = 5)

time_it()

window.mainloop()
