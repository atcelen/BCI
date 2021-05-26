import os
import numpy as np
import pandas as pd
import scipy.signal
from scipy import signal, fft
from sklearn.preprocessing import MinMaxScaler



import numpy as np
from scipy import signal, fft
# tqdm is a library for showing the progress bar
from tqdm.notebook import tqdm
# plotting library
import matplotlib.pyplot as plt

#%matplotlib inline
import matplotlib.pyplot as plt
plt.rc('axes', axisbelow=True)
plt.rcParams['figure.figsize'] = [16, 7]

def Y_loader(protocols):
    number_of_trials = 4
    number_of_runs = 32    
    Y=np.zeros((number_of_runs, number_of_trials))
    for k in range(number_of_runs):
        a = load_labels(protocols[k])
        Y[k] = a[0][0:number_of_trials]
    print(Y.shape)
    return Y

def load_data(file, channels): 
    '''
    Load data from csv file. 
    
    Params
    ------
    file: string
        path and name to the csv file 
    channels: np array
        channels to be returned
        
    Return
    ------
    data: np array (n_ch, n_s)
        EEG data 
    '''
    
    df= pd.read_csv(file,sep=',')# as df:
    data = np.asarray(df.values)
    
    return np.transpose(data[:,channels])
    
def load_labels(file): 
    '''
    Load data from txt file. 
    
    Params
    ------
    file: string
        path and name to the csv file 
        
    '''
    
    df= pd.read_csv(file,sep=',',header=None)# as df:
    data = np.asarray(df.values)
    return np.transpose(data[:,:])



def norm_freq(f, fs):
    return f * 2 / fs
    
def bandpass_multiEEG(data,f_low,f_high,fs):
    '''
    Bandpass multi channel EEG
    
    Params
    ------
    data: np array (n_ch,n_s)
        EEG data
    f_low: float
        lower corner frequency [Hz]
    f_high: float
        upper corner_frequency [Hz]
    fs: float
        sampling frequency
    
    Return
    ------
    data_filt: np array (n_ch, n_s)
        filtered EEG data 
    '''

    print("here", data.shape)
    
    low_freq = norm_freq(f_low, fs)
    high_freq = norm_freq(f_high, fs)
    #Wn=[low_freq, high_freq], btype='bandpass'
    coef_filt = scipy.signal.butter(N=4,Wn= 0.05, output='sos')
    data_filt = np.zeros(data.shape)
    for trial in range(data.shape[0]):
        for chan in range(data.shape[1]):
            data_filt[trial,chan,:] = scipy.signal.sosfiltfilt(coef_filt, x=data[trial, chan, :])
    return data_filt    
def trim_start_end(filename, num_channels):
    '''
    Find the beginning and the end of the recording
    based on the labels
    
    Params
    ------
    filename: string
        path and name to the csv file 
        
    '''    
    data = load_labels(filename)
    k,l=1,0
    return_list=[0,0]
    nan = np.nan
    for i in range(1,len(data[1,:])):
        if data[11,i] is nan:
            k+=1
            continue
        else:
            return_list[l]=k
            k+=1
            l+=1
            
    
    trimmed_data = data[:,return_list[0]:return_list[1]+1]
    print(trimmed_data.shape)
    #final_data_cross = np.ndarray((4,8,500))
    
    final_data_motor = np.ndarray((4,num_channels,1000))
    
    #final_data_break = np.ndarray((4,8,1000))
    
    for t in range(4):
    
        t_mul = 2500*t
        
        #fixation_cross = trimmed_data[2:10,t_mul:t_mul+500]
        if num_channels == 8:
            motor_movement = trimmed_data[2:10,t_mul+500:t_mul+1500]
        elif num_channels == 3:
            motor_movement = [None] * 3
            motor_movement[0] = trimmed_data[5,t_mul+500:t_mul+1500]
            motor_movement[1:3] = trimmed_data[7:9,t_mul+500:t_mul+1500]    
        
        #break_time = trimmed_data[2:10,t_mul+1500:t_mul+2500]
        
        #final_data_cross[t]=fixation_cross
        
        final_data_motor[t]=motor_movement
        
        #final_data_break[t]=break_time
        
    return final_data_motor


#y = trim_start_end('session1_run1_Deniz.csv')
#print(y)
protocols = [#'run1.txt',
            #  'run2.txt',
            #  'run3.txt',
            #  'run4.txt',
            #  'run5.txt',
            #  'run6.txt',
            #  'run7.txt',
            #  'run8.txt',
            #  'run9.txt',
            #  'run10.txt',
            #  'run11.txt',
            #  'run12.txt',
            #  'run13.txt',
            #  'run14.txt',
            #  'run15.txt',
            #  'run16.txt',
            # #  #'run9.txt',
            # #  #'run10.txt',
            # #  #'run11.txt',
            # #  #'run12.txt',
            # #  #'run13.txt',
            # #  #'run14.txt',
            # #  #'run15.txt',
            # #  #'run16.txt',
            #   'run17.txt',
            #   'run18.txt',
            #   'run19.txt',
            #   'run20.txt',
            #   'run21.txt',
            #   'run22.txt',
            #   'run23.txt',
            #   'run24.txt'
            # #  'run1b.txt',
            # #  'run2b.txt',
            # #  'run3b.txt',
            # #  'run4b.txt',
            # #  'run5b.txt',
            # #  'run6b.txt',
            # #  'run7b.txt',
            # #  'run8b.txt'
            'superrun1.txt',
            'superrun2.txt',
            'superrun3.txt',
            'superrun4.txt',
            'superrun5.txt',
            'superrun6.txt',
            'superrun7.txt',
            'superrun8.txt',
            'superrun9.txt',
            'superrun10.txt',
            'superrun11.txt',
            'superrun12.txt',
            'superrun13.txt',
            'superrun14.txt',
            'superrun15.txt',
            'superrun16.txt',
            'superrun17.txt',
            'superrun18.txt',
            'superrun19.txt',
            'superrun20.txt',
            'superrun21.txt',
            'superrun22.txt',
            'superrun23.txt',
            'superrun24.txt',
            'superrun25.txt',
            'superrun26.txt',
            'superrun27.txt',
            'superrun28.txt',
            'superrun29.txt',
            'superrun30.txt',
            'superrun31.txt',
            'superrun32.txt'
             ]
filenames = [#'session4_run1_Deniz.csv',
            #  'session4_run2_Deniz.csv',
            #  'session4_run3_Deniz.csv',
            #  'session4_run4_Deniz.csv',
            #  'session4_run5_Deniz.csv',
            #  'session4_run6_Deniz.csv',
            #  'session4_run7_Deniz.csv',
            #  'session4_run8_Deniz.csv',
            #  'session5_run1_Deniz.csv',
            #  'session5_run2_Deniz.csv',
            #  'session5_run3_Deniz.csv',
            #  'session5_run4_Deniz.csv',
            #  'session5_run5_Deniz.csv',
            #  'session5_run6_Deniz.csv',
            #  'session5_run7_Deniz.csv',
            #  'session5_run8_Deniz.csv',
            #   'session2_run1_Deniz.csv',
            #   'session2_run2_Deniz.csv',
            #   'session2_run3_Deniz.csv',
            #   'session2_run4_Deniz.csv',
            #   'session2_run5_Deniz.csv',
            #   'session2_run6_Deniz.csv',
            #   'session2_run7_Deniz.csv',
            #  'session2_run8_Deniz.csv'
            # #  'bandFormation3_run1_Deniz.csv',
            # #  'bandFormation3_run2_Deniz.csv',
            # #  'bandFormation3_run3_Deniz.csv',
            # #  'bandFormation3_run4_Deniz.csv',
            # #  'bandFormation3_run5_Deniz.csv',
            # #  'bandFormation3_run6_Deniz.csv',
            # #  'bandFormation3_run7_Deniz.csv',
            # #  'bandFormation3_run8_Deniz.csv'
            # 'session2_run1_Deniz.csv',
            # 'session2_run2_Deniz.csv',
            # 'session2_run3_Deniz.csv',
            # 'session2_run4_Deniz.csv',
            # 'session2_run5_Deniz.csv',
            # 'session2_run6_Deniz.csv',
            # 'session2_run7_Deniz.csv',
            # 'session2_run8_Deniz.csv'
            'SessionSuper1w_run1_Deniz.csv',
            'SessionSuper1w_run2_Deniz.csv',
            'SessionSuper1w_run3_Deniz.csv',
            'SessionSuper1w_run4_Deniz.csv',
            'SessionSuper1w_run5_Deniz.csv',
            'SessionSuper1w_run6_Deniz.csv',
            'SessionSuper1w_run7_Deniz.csv',
            'SessionSuper1w_run8_Deniz.csv',
            'SessionSuper1w_run9_Deniz.csv',
            'SessionSuper1w_run10_Deniz.csv',
            'SessionSuper1w_run11_Deniz.csv',
            'SessionSuper1w_run12_Deniz.csv',
            'SessionSuper1w_run13_Deniz.csv',
            'SessionSuper1w_run14_Deniz.csv',
            'SessionSuper1w_run15_Deniz.csv',
            'SessionSuper1w_run16_Deniz.csv',
            'SessionSuper1w_run17_Deniz.csv',
            'SessionSuper1w_run18_Deniz.csv',
            'SessionSuper1w_run19_Deniz.csv',
            'SessionSuper1w_run20_Deniz.csv',
            'SessionSuper1w_run21_Deniz.csv',
            'SessionSuper1w_run22_Deniz.csv',
            'SessionSuper1w_run23_Deniz.csv',
            'SessionSuper1w_run24_Deniz.csv',
            'SessionSuper1w_run25_Deniz.csv',
            'SessionSuper1w_run26_Deniz.csv',
            'SessionSuper1w_run27_Deniz.csv',
            'SessionSuper1w_run28_Deniz.csv',
            'SessionSuper1w_run29_Deniz.csv',
            'SessionSuper1w_run30_Deniz.csv',
            'SessionSuper1w_run31_Deniz.csv',
            'SessionSuper1w_run32_Deniz.csv'
             ]

def trim_multiple(num_channels):
    trimmed_files = np.ndarray((128, num_channels,1000))
    counter = 0
    for file in filenames:
        trimmed_files[counter:counter+4]= trim_start_end(file, num_channels)
        counter+=4
    print(np.shape(trimmed_files))
    # plt.figure(1)
    # plt.plot(trimmed_files[0,0,:])
    # plt.show()
    # plt.plot(trimmed_files[0,1,:])
    # plt.show()
    # plt.plot(trimmed_files[0,2,:])
    # plt.show()
    # plt.plot(trimmed_files[0,3,:])
    # plt.show()
    trimmed_files_filtered = bandpass_multiEEG(trimmed_files,4,48,250)
    trimmed_files_filtered = np.asarray(trimmed_files_filtered)
    for trial in range(0, trimmed_files_filtered.shape[0]):
        for channel in range(0, trimmed_files_filtered.shape[1]):
            max = np.max(trimmed_files_filtered[trial,channel,:])
            min = np.min(trimmed_files_filtered[trial,channel,:])
            #X_std = (trimmed_files_filtered - min) /  (max-min)
            sum = np.sum(trimmed_files_filtered[trial,channel,:])
            ave = sum / (trimmed_files_filtered.shape[2])
            noBi = np.asarray(trimmed_files_filtered[trial][channel] - ave) 
            trimmed_files_filtered[trial][channel] = noBi
    plt.figure(1)
    #plt.plot(trimmed_files[0,0,:])
    plt.plot(trimmed_files_filtered[0,0,:])
    plt.show()
    #plt.plot(trimmed_files[0,1,:])
    plt.plot(trimmed_files_filtered[0,1,:])
    plt.show()
    #plt.plot(trimmed_files[0,2,:])
    plt.plot(trimmed_files_filtered[0,2,:])
    plt.show()
    #plt.plot(trimmed_files[0,3,:])
    plt.plot(trimmed_files_filtered[0,3,:])
    plt.show()
    print(trimmed_files.shape, Y_loader(protocols).shape)
    return trimmed_files_filtered, Y_loader(protocols)


def class_separator():
   
    x_trimmed, y = trim_multiple(8)

    x_new = np.ndarray(np.shape(x_trimmed[0:int(len(x_trimmed)/2),:,:]))
   
    y_shape=np.shape(y)
   
    new_shape_y = (y_shape[0],int(y_shape[1]/2))
   
    y_new = np.ndarray(new_shape_y)
   
    counter_x,counter_y = 0,0
   
    for k in range(len(protocols)):
       
        found = 0
       
        for i in range(len(y[k])):    
           
            if y[k][i]==0 or y[k][i]==1:
               
                print(y[k], y.shape)

                x_new[counter_x] = x_trimmed[k*4+i]
               
                y_new[counter_y][found] = y[k][i]
               
                found+=1
               
                counter_x += 1
                                 
        counter_y+=1        
               
               
    print(np.shape(y_new), np.shape(x_new))
   
    return x_new, y_new

