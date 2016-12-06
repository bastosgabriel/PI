#/////////////////////////////////////////#
#                                         #
# Universidade Federal do Rio de Janeiro  #
# Aluno: Gabriel Marcial Bastos           #
# Projeto Integrado - 2016.2              #
# Data: 06/12/2016                        #
#                                         #
#/////////////////////////////////////////#

import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

dt = 0.01
Fs = 44000.0              # sample rate
timestep = 1.0/Fs         # sample spacing (1/sample rate)
t = np.arange(0, 10, dt)  # intervalo t
n = 256                   # size of the array data
w = 10000                 # frequency of the input

data = np.sin(2*np.pi*w*t)
lines = []


def update(data):
    # update the curves with the incoming data
    line.set_ydata(data)
    #line2.set_ydata(magnitude)

    #for data,line in enumerate(lines):
    #    line.set_data(xlist[data], ylist[data])

    return line,

def generateData():
    # read new data from serial port
    while True:
        ser = serial.Serial('COM4', 9600, timeout=8,
                        parity=serial.PARITY_EVEN, rtscts=1)  # open and prepare serial port

        data = ser.readline()
        magnitude = np.fft.fft(data)/n
        magnitude = np.abs(magnitude[range(n//2)])
        yield data

fig = plt.figure()

# plot time graph axis
timeGraph = plt.subplot(2, 1, 1)
timeGraph.set_ylim(-0.2, 0.2)
timeGraph.set_xlabel('Time')
timeGraph.set_ylabel('Amplitude')

# plot frequency graph axis
freqGraph = plt.subplot(2, 1, 2)
freqGraph.set_xlabel('Freq (Hz)')
freqGraph.set_ylabel('|Y(freq)|')

# get frequency range
n = len(data) # length of the signal
print(len(data))
k = np.arange(n)
T = n/Fs
freq = k/T # two sides frequency range
freq = freq[range(n//2)] # one side frequency range

# fft computing and normalization
magnitude = np.fft.fft(data)/n
magnitude = np.abs(magnitude[range(n//2)])


line, = timeGraph.plot(np.linspace(0, 1, len(t)),'b')
line2, = freqGraph.plot(freq, magnitude,'g')


# animate the curves
ani = animation.FuncAnimation(fig, update, generateData,
                              interval = 10, blit=True)

plt.show() # open window
