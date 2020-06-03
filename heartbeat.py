import time,csv
import matplotlib
from time import gmtime,strftime
import matplotlib.pyplot as plt
import numpy as np
import serial

class Heartbeat:

    plot_window = 20 
    y_var = np.array(np.zeros([plot_window]))
    plt.ion()
    fig, ax = plt.subplots()
    line, = ax.plot(y_var)

    def select_sensor (self, ser, name):
        while True:
            ser_bytes = ser.readline().decode()   
            if name[:1] in ser_bytes:
                ser_bytes = ser_bytes[3:]
                self.fill_data(ser_bytes,name)

    def fill_data(self,ser_bytes,graph_name):
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2])
        #saving the data on a csv file
        with open("data.csv","a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([strftime("%c", gmtime()),graph_name[:1],decoded_bytes])
        #appending the latest data to the graph
        self.y_var = np.append(self.y_var,decoded_bytes)
        self.y_var = self.y_var[1:self.plot_window + 1]
        self.line.set_ydata(self.y_var)
        self.ax.relim()
        self.ax.autoscale_view()
        #drawing the graph
        plt.title(graph_name)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

def main():
    pass

if __name__ == "__main__":
    hb = Heartbeat()
    #select serial port
    ser = serial.Serial('COM6',9600)
    ser.flushInput()
    sensors = input("please select a sensor:\n")
    if sensors == "sound":
        hb.select_sensor(ser,"sound sensor data")
    elif sensors == "water":
        hb.select_sensor(ser,"water sensor data")