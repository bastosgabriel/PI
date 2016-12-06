import serial
import matplotlib.pyplot as plt
import numpy as np


ser = serial.Serial('COM4', 9600, timeout=8,
                    parity=serial.PARITY_EVEN, rtscts=1)  # open and prepare serial port

data = ser.readline() #read incoming data
while (data!=""): # print data in real time
    data = ser.readline()


#print(np.fft.fft(np.exp(2j * np.pi * np.arange(8) / 8)))
'''
# Number of sample points
N = 256
# sample spacing
T = 1.0 / 40000.0

x = np.linspace(0.0, N*T, N)
y = np.sin(t)

#eixos do espectro
eixoX = np.linspace(0.0, 1.0/(2.0*T), N/2)
eixoY = np.fft.fft(y)

# plota
plt.plot(eixoX, y )
plt.grid()
plt.show()
'''


import matplotlib.animation as animation

s = 0;
dt = 0.01
Fs = 1/dt # frequencia
t = np.arange(0, 10, dt) # intervalo t


fig, ax = plt.subplots()
timeGraph= plt.subplot(2, 1, 1)
freqGraph = plt.subplot(2, 1, 2)



line, = timeGraph.plot(t, s)
timeGraph.set_ylim(-1, 1)


def update(data):
    line.set_ydata(data)
    return line,

def generateData():
    # simulate new data coming in
    while True:
        nse = np.random.randn(len(t))
        r = np.exp(-t/0.05)
        cnse = np.convolve(nse, r)*dt
        cnse = cnse[:len(t)]
        s =  0.1*np.sin(2*np.pi*t) + cnse
        yield s

#s = generateData()
#timeGraph.plot(t, s)
#freqGraph.magnitude_spectrum(s, Fs)


ani = animation.FuncAnimation(fig, update, generateData, interval = 10)
plt.show()


