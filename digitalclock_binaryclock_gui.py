'''
    Python programme to display GUI digital clock
    and binary version of it
    Note: If variables or indexing looks weired it's
    because of pylint
    but the code gets 10/10 :}
    '''
import tkinter
import time
WINDOW = tkinter.Tk()
WINDOW.title("Binary Clock")

def test(_x, _y):
    '''
        when converted to binary output may have
        len in range(5) hance to satisfy the empty
        spaces with zero
        '''
    try:
        return _x[_y]
    except IndexError:
        return '0'

def time_it():
    '''
        this function is used to
        convert time to respective labele text
        '''
    while 1:
        #extracting current time
        string = time.strftime('%H:%M:%S')
        string_2 = str(time.strftime('%H:%M:%S %a'))
        VAR_DIGI.set(string_2)
        #converting time to binary
        h_1 = bin(int(string[0]))[2:]
        h_2 = bin(int(string[1]))[2:]

        m_1 = bin(int(string[3]))[2:]
        m_2 = bin(int(string[4]))[2:]

        s_1 = bin(int(string[6]))[2:]
        s_2 = bin(int(string[7]))[2:]
        #assigning time to respective label variables
        VAR111.set(test(h_1, -4))
        VAR121.set(test(h_1, -3))
        VAR131.set(test(h_1, -2))
        VAR141.set(h_1[-1])

        VAR212.set(test(h_2, -4))
        VAR222.set(test(h_2, -3))
        VAR232.set(test(h_2, -2))
        VAR242.set(h_2[-1])

        VAR113.set(test(m_1, -4))
        VAR123.set(test(m_1, -3))
        VAR133.set(test(m_1, -2))
        VAR143.set(m_1[-1])

        VAR214.set(test(m_2, -4))
        VAR224.set(test(m_2, -3))
        VAR234.set(test(m_2, -2))
        VAR244.set(m_2[-1])

        VAR115.set(test(s_1, -4))
        VAR125.set(test(s_1, -3))
        VAR135.set(test(s_1, -2))
        VAR145.set(s_1[-1])

        VAR216.set(test(s_2, -4))
        VAR226.set(test(s_2, -3))
        VAR236.set(test(s_2, -2))
        VAR246.set(s_2[-1])

        time.sleep(1)
        WINDOW.update()
#using StingVar() label variable is dynamically allocated
VAR_DIGI = tkinter.StringVar()

VAR111 = tkinter.StringVar()
VAR121 = tkinter.StringVar()
VAR131 = tkinter.StringVar()
VAR141 = tkinter.StringVar()

VAR212 = tkinter.StringVar()
VAR222 = tkinter.StringVar()
VAR232 = tkinter.StringVar()
VAR242 = tkinter.StringVar()

VAR113 = tkinter.StringVar()
VAR123 = tkinter.StringVar()
VAR133 = tkinter.StringVar()
VAR143 = tkinter.StringVar()

VAR214 = tkinter.StringVar()
VAR224 = tkinter.StringVar()
VAR234 = tkinter.StringVar()
VAR244 = tkinter.StringVar()

VAR115 = tkinter.StringVar()
VAR125 = tkinter.StringVar()
VAR135 = tkinter.StringVar()
VAR145 = tkinter.StringVar()

VAR216 = tkinter.StringVar()
VAR226 = tkinter.StringVar()
VAR236 = tkinter.StringVar()
VAR246 = tkinter.StringVar()

#labels of each grid
DIGI_CLOCK = tkinter.Label(WINDOW, textvariable=VAR_DIGI,
                           font=('calibri', 30, 'bold'), background='purple', foreground='white')

H111 = tkinter.Label(WINDOW, textvariable=VAR111,
                     font=('Arial', 40, 'bold'), background='yellow', foreground='black')
H121 = tkinter.Label(WINDOW, textvariable=VAR121,
                     font=('Arial', 40, 'bold'), background='yellow', foreground='black')
H131 = tkinter.Label(WINDOW, textvariable=VAR131,
                     font=('Arial', 40, 'bold'), background='yellow', foreground='black')
H141 = tkinter.Label(WINDOW, textvariable=VAR141,
                     font=('Arial', 40, 'bold'), background='yellow', foreground='black')

H212 = tkinter.Label(WINDOW, textvariable=VAR212,
                     font=('Arial', 40, 'bold'), background='yellow', foreground='black')
H222 = tkinter.Label(WINDOW, textvariable=VAR222,
                     font=('Arial', 40, 'bold'), background='yellow', foreground='black')
H232 = tkinter.Label(WINDOW, textvariable=VAR232,
                     font=('Arial', 40, 'bold'), background='yellow', foreground='black')
H242 = tkinter.Label(WINDOW, textvariable=VAR242,
                     font=('Arial', 40, 'bold'), background='yellow', foreground='black')

M113 = tkinter.Label(WINDOW, textvariable=VAR113,
                     font=('Arial', 40, 'bold'), background='red', foreground='white')
M123 = tkinter.Label(WINDOW, textvariable=VAR123,
                     font=('Arial', 40, 'bold'), background='red', foreground='white')
M133 = tkinter.Label(WINDOW, textvariable=VAR133,
                     font=('Arial', 40, 'bold'), background='red', foreground='white')
M143 = tkinter.Label(WINDOW, textvariable=VAR143,
                     font=('Arial', 40, 'bold'), background='red', foreground='white')

M214 = tkinter.Label(WINDOW, textvariable=VAR214,
                     font=('Arial', 40, 'bold'), background='red', foreground='white')
M224 = tkinter.Label(WINDOW, textvariable=VAR224,
                     font=('Arial', 40, 'bold'), background='red', foreground='white')
M234 = tkinter.Label(WINDOW, textvariable=VAR234,
                     font=('Arial', 40, 'bold'), background='red', foreground='white')
M244 = tkinter.Label(WINDOW, textvariable=VAR244,
                     font=('Arial', 40, 'bold'), background='red', foreground='white')

S115 = tkinter.Label(WINDOW, textvariable=VAR115,
                     font=('Arial', 40, 'bold'), background='orange', foreground='green')
S125 = tkinter.Label(WINDOW, textvariable=VAR125,
                     font=('Arial', 40, 'bold'), background='orange', foreground='green')
S135 = tkinter.Label(WINDOW, textvariable=VAR135,
                     font=('Arial', 40, 'bold'), background='orange', foreground='green')
S145 = tkinter.Label(WINDOW, textvariable=VAR145,
                     font=('Arial', 40, 'bold'), background='orange', foreground='green')

S216 = tkinter.Label(WINDOW, textvariable=VAR216,
                     font=('Arial', 40, 'bold'), background='orange', foreground='green')
S226 = tkinter.Label(WINDOW, textvariable=VAR226,
                     font=('Arial', 40, 'bold'), background='orange', foreground='green')
S236 = tkinter.Label(WINDOW, textvariable=VAR236,
                     font=('Arial', 40, 'bold'), background='orange', foreground='green')
S246 = tkinter.Label(WINDOW, textvariable=VAR246,
                     font=('Arial', 40, 'bold'), background='orange', foreground='green')

#forming the grid
DIGI_CLOCK.grid(row=0, columnspan=6, sticky='EW')

H111.grid(row=1, column=0, ipadx=10)
H121.grid(row=2, column=0, ipadx=10)
H131.grid(row=3, column=0, ipadx=10)
H141.grid(row=4, column=0, ipadx=10)

H212.grid(row=1, column=1, ipadx=10)
H222.grid(row=2, column=1, ipadx=10)
H232.grid(row=3, column=1, ipadx=10)
H242.grid(row=4, column=1, ipadx=10)

M113.grid(row=1, column=2, ipadx=10)
M123.grid(row=2, column=2, ipadx=10)
M133.grid(row=3, column=2, ipadx=10)
M143.grid(row=4, column=2, ipadx=10)

M214.grid(row=1, column=3, ipadx=10)
M224.grid(row=2, column=3, ipadx=10)
M234.grid(row=3, column=3, ipadx=10)
M244.grid(row=4, column=3, ipadx=10)

S115.grid(row=1, column=4, ipadx=10)
S125.grid(row=2, column=4, ipadx=10)
S135.grid(row=3, column=4, ipadx=10)
S145.grid(row=4, column=4, ipadx=10)

S216.grid(row=1, column=5, ipadx=10)
S226.grid(row=2, column=5, ipadx=10)
S236.grid(row=3, column=5, ipadx=10)
S246.grid(row=4, column=5, ipadx=10)

#calling for time allocation
time_it()

WINDOW.mainloop()
