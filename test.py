import serial,time,csv
import matplotlib
from time import gmtime,strftime
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('COM6',9600)
ser.flushInput()


plot_window = 20 
y_var = np.array(np.zeros([plot_window]))
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(y_var)

while True:
    try:
        #receiving data from the arduino
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        #saving the data on a csv file
        with open("song_data.csv","a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([strftime("%c", gmtime()),decoded_bytes])
        #appending the latest data to the graph
        y_var = np.append(y_var,decoded_bytes)
        y_var = y_var[1:plot_window + 1]
        line.set_ydata(y_var)
        ax.relim()
        ax.autoscale_view()
        #drawing the graph
        plt.title(""" song heartbeat """)
        fig.canvas.draw()
        fig.canvas.flush_events()
    except:
        print("interrupt")
        break