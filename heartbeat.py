import time,csv
import matplotlib
from time import gmtime,strftime
import matplotlib.pyplot as plt
import numpy as np
import serial

class heartbeat:

    def draw_canvas(self):
        plot_window = 20 
        y_var = np.array(np.zeros([plot_window]))
        plt.ion()
        fig, ax = plt.subplots()
        line, = ax.plot(y_var)

    def sound(self,ser):
        draw_canvas()
        while True:
            try:
                #receiving data from the arduino
                ser_bytes = ser.readline()
                #filter sound data
                if 's' in ser_bytes:
                    #cut off the first 3 characters of the string
                    ser_bytes = ser_bytes[3:]
            except:
                print("interrupt")
                break

    def water(self,ser):
        while True:
            try:
                #receiving data from the arduino
                ser_bytes = ser.readline()
                #filter sound data
                if 'w' in ser_bytes:
                    #cut off the first 3 characters of the string
                    ser_bytes = ser_bytes[3:]
            except:
                print("interrupt")
                break

    def fill_data(self,ser_bytes):
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
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

def main():
    #select serial port
    ser = serial.Serial('COM6',9600)
    ser.flushInput()
    sensors = raw_input("please select a sensor:\n")
    if sensors == "sound":
        sound(ser)
    elif sensors == "water":
        water(ser)

if __name__ == "__main__":
    main ()