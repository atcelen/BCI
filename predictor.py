from tensorflow import keras
import pylsl
from pylsl import StreamInlet, resolve_stream
import numpy as np
import dataloader as dl
import matplotlib.pyplot as plt
import time as time
import socket


#model = keras.models.load_model(r"C:\Users\atace\eegnet-based-embedded-bci-master\results\firstTryOurValues\model\global_class_4_ds1_nch8_T4_split_9.h5")
model = keras.models.load_model(r"C:\Users\atace\eegnet-based-embedded-bci-master\results\firstTryOurValues\good_models\global_class_2_ds1_nch8_T4_split_0.h5")


#first resolve an EEG stream on the lab network
# create a new inlet to read from the stream
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


# Create the socket connection with the navigating nao script
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print("here")
arr = []
sendData = None

#Start sampling data by pressing y
while True:
    inp = input("Press y to start sampling data \n")
    if inp == "y" :
        print("looking for an EEG stream...")
        streams = resolve_stream('type', 'EEG')
        inlet = StreamInlet(streams[0])
        count = 0
        data = [[]]
        print("START")
        print(time.time())
        # Get 4s of data with sampling frequency 250Hz
        while count < 1000:
            sample, timestamp = inlet.pull_sample()     
            data[0].append([elem for elem in sample])
            data[0][count].pop()
            count=count+1
        print(time.time())
        data[0] = np.array(data[0])
        data[0] = np.transpose(data[0])
        data = np.array(data)    
        #print(data[0][0])
        plt.figure(1)
        plt.plot(data[0,0,:])
        plt.show()
        data = dl.bandpass_multiEEG(data,250)
        #Normalize the data
        for trial in range(0, data.shape[0]):
            for channel in range(0, data.shape[1]):
                sum = np.sum(data[trial,channel,:])
                ave = sum / (data.shape[2])
                data[trial,channel,:] = np.asarray(data[trial,channel,:] - ave)
                max = np.argmax(data[trial,channel,:])
                max = data[trial,channel,max]
                data[trial,channel,:] = data[trial,channel,:] / max
        plt.figure(1)
        plt.plot(data[0,0,:])
        plt.show()
        y = model.predict(data)
        print("Data Sampling ended the result is: ",np.argmax(y))
        sendData = np.argmax(y)
        # Send the prediction to the navigating nao script 
        print('Connected by', addr)
        conn.sendall(sendData)
    else:
        sendData = None