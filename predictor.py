from tensorflow import keras
import pylsl
from pylsl import StreamInlet, resolve_stream
import numpy as np
import dataloader as dl
import matplotlib.pyplot as plt


model = keras.models.load_model(r"C:\Users\atace\eegnet-based-embedded-bci-master\results\firstTryOurValues\model\global_class_4_ds1_nch8_T4_split_4.h5")

#first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
arr = []
while True:
    count = 0
    data = [[]]
    while count < 1000:
        sample, timestamp = inlet.pull_sample()     
        data[0].append([elem for elem in sample])
        data[0][count].pop()
        #print(timestamp, data[0][count],count)
        count=count+1
    data[0] = np.array(data[0])
    data[0] = np.transpose(data[0])
    data = np.array(data)    
    print(data[0])
    # plt.figure(1)
    # plt.plot(data[0,0,:])
    # plt.show()
    data = dl.bandpass_multiEEG(data,4,48,250)
    # plt.figure(1)
    # plt.plot(data[0,0,:])
    # plt.show()
    y = model.predict(data)
    print(np.argmax(y))
    