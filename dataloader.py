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
    number_of_runs = 208    
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
    
def bandpass_multiEEG(data,fs):
    '''
    Bandpass multi channel EEG
    
    Params
    ------
    data: np array (n_ch,n_s)
        EEG data
    fs: float
        sampling frequency
    
    Return
    ------
    data_filt: np array (n_ch, n_s)
        filtered EEG data 
    '''

    print("here", data.shape)
    

    coef_filt = scipy.signal.butter(N=4,Wn=[0.008,0.32], output='sos',btype='bandpass')
    data_filt = np.zeros(data.shape)
    # Applying a 50Hz-Notch and 1-40Hz Butterworth bandpass
    for trial in range(data.shape[0]):
        for chan in range(data.shape[1]):
            b_notch, a_notch = signal.iirnotch(50, 30, fs)
            data_filt[trial,chan,:] = signal.filtfilt(b_notch, a_notch, data_filt[trial,chan,:])
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
    num_channels: integer
        number of channels to use for analysis     
        
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
    print(filename)
    final_data_motor = np.ndarray((4,num_channels,1000))
    
    for t in range(4):
    
        t_mul = 2500*t
        if num_channels == 8:
            motor_movement = trimmed_data[2:10,t_mul+500:t_mul+1500]
        elif num_channels == 3:
            motor_movement = [None] * 3
            motor_movement[0] = trimmed_data[5,t_mul+500:t_mul+1500]
            motor_movement[1:3] = trimmed_data[7:9,t_mul+500:t_mul+1500]    
        
        final_data_motor[t]=motor_movement
    return final_data_motor


#Load the CSV files from your sessions
protocols = ['run1.txt',
             'run2.txt',
             'run3.txt',
             'run4.txt',
             'run5.txt',
             'run6.txt',
             'run7.txt',
             'run8.txt',
             'run9.txt',
             'run10.txt',
             'run11.txt',
             'run12.txt',
             'run13.txt',
             'run14.txt',
             'run15.txt',
             'run16.txt',
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
            'superrun32.txt',
            'superrunS2_0.txt',
            'superrunS2_1.txt',
            'superrunS2_2.txt',
            'superrunS2_3.txt',
            'superrunS2_4.txt',
            'superrunS2_5.txt',
            'superrunS2_6.txt',
            'superrunS2_7.txt',
            'superrunS2_8.txt',
            'superrunS2_9.txt',
            'superrunS2_10.txt',
            'superrunS2_11.txt',
            'superrunS2_12.txt',
            'superrunS2_13.txt',
            'superrunS2_14.txt',
            'superrunS2_15.txt',
            'superrunS2_16.txt',
            'superrunS2_17.txt',
            'superrunS2_18.txt',
            'superrunS2_19.txt',
            'superrunS2_20.txt',
            'superrunS2_21.txt',
            'superrunS2_22.txt',
            'superrunS2_23.txt',
            'superrunS2_24.txt',
            'superrunS2_25.txt',
            'superrunS2_26.txt',
            'superrunS2_27.txt',
            'superrunS2_28.txt',
            'superrunS2_29.txt',
            'superrunS2_30.txt',
            'superrunS2_31.txt',
            'superrunS3_0.txt',
            'superrunS3_1.txt',
            'superrunS3_2.txt',
            'superrunS3_3.txt',
            'superrunS3_4.txt',
            'superrunS3_5.txt',
            'superrunS3_6.txt',
            'superrunS3_7.txt',
            'superrunS3_8.txt',
            'superrunS3_9.txt',
            'superrunS3_10.txt',
            'superrunS3_11.txt',
            'superrunS3_12.txt',
            'superrunS3_13.txt',
            'superrunS3_14.txt',
            'superrunS3_15.txt',
            'superrunS3_16.txt',
            'superrunS3_17.txt',
            'superrunS3_18.txt',
            'superrunS3_19.txt',
            'superrunS3_20.txt',
            'superrunS3_21.txt',
            'superrunS3_22.txt',
            'superrunS3_23.txt',
            'superrunS3_24.txt',
            'superrunS3_25.txt',
            'superrunS3_26.txt',
            'superrunS3_27.txt',
            'superrunS3_28.txt',
            'superrunS3_29.txt',
            'superrunS3_30.txt',
            'superrunS3_31.txt',
            'superrunS4_0.txt',
            'superrunS4_1.txt',
            'superrunS4_2.txt',
            'superrunS4_3.txt',
            'superrunS4_4.txt',
            'superrunS4_5.txt',
            'superrunS4_6.txt',
            'superrunS4_7.txt',
            'superrunS4_8.txt',
            'superrunS4_9.txt',
            'superrunS4_10.txt',
            'superrunS4_11.txt',
            'superrunS4_12.txt',
            'superrunS4_13.txt',
            'superrunS4_14.txt',
            'superrunS4_15.txt',
            'superrunS4_16.txt',
            'superrunS4_17.txt',
            'superrunS4_18.txt',
            'superrunS4_19.txt',
            'superrunS4_20.txt',
            'superrunS4_21.txt',
            'superrunS4_22.txt',
            'superrunS4_23.txt',
            'superrunS4_24.txt',
            'superrunS4_25.txt',
            'superrunS4_26.txt',
            'superrunS4_27.txt',
            'superrunS4_28.txt',
            'superrunS4_29.txt',
            'superrunS4_30.txt',
            'superrunS4_31.txt',
            'superrunS5_0.txt',
            'superrunS5_1.txt',
            'superrunS5_2.txt',
            'superrunS5_3.txt',
            'superrunS5_4.txt',
            'superrunS5_5.txt',
            'superrunS5_6.txt',
            'superrunS5_7.txt',
            'superrunS5_8.txt',
            'superrunS5_9.txt',
            'superrunS5_10.txt',
            'superrunS5_11.txt',
            'superrunS5_12.txt',
            'superrunS5_13.txt',
            'superrunS5_14.txt',
            'superrunS5_15.txt',
            'superrunS5_16.txt',
            'superrunS5_17.txt',
            'superrunS5_18.txt',
            'superrunS5_19.txt',
            'superrunS5_20.txt',
            'superrunS5_21.txt',
            'superrunS5_22.txt',
            'superrunS5_23.txt',
            'superrunS5_24.txt',
            'superrunS5_25.txt',
            'superrunS5_26.txt',
            'superrunS5_27.txt',
            'superrunS5_28.txt',
            'superrunS5_29.txt',
            'superrunS5_30.txt',
            'superrunS5_31.txt',
            'superrunS6_0.txt',
            'superrunS6_1.txt',
            'superrunS6_2.txt',
            'superrunS6_3.txt',
            'superrunS6_4.txt',
            'superrunS6_5.txt',
            'superrunS6_6.txt',
            'superrunS6_7.txt',
            'superrunS6_8.txt',
            'superrunS6_9.txt',
            'superrunS6_10.txt',
            'superrunS6_11.txt',
            'superrunS6_12.txt',
            'superrunS6_13.txt',
            'superrunS6_14.txt',
            'superrunS6_15.txt',
            'superrunS6_16.txt',
            'superrunS6_17.txt',
            'superrunS6_18.txt',
            'superrunS6_19.txt',
            'superrunS6_20.txt',
            'superrunS6_21.txt',
            'superrunS6_22.txt',
            'superrunS6_23.txt',
            'superrunS6_24.txt',
            'superrunS6_25.txt',
            'superrunS6_26.txt',
            'superrunS6_27.txt',
            'superrunS6_28.txt',
            'superrunS6_29.txt',
            'superrunS6_30.txt',
            'superrunS6_31.txt',
             ]
filenames = ['session4_run1_Deniz.csv',
             'session4_run2_Deniz.csv',
             'session4_run3_Deniz.csv',
             'session4_run4_Deniz.csv',
             'session4_run5_Deniz.csv',
             'session4_run6_Deniz.csv',
             'session4_run7_Deniz.csv',
             'session4_run8_Deniz.csv',
             'session5_run1_Deniz.csv',
             'session5_run2_Deniz.csv',
             'session5_run3_Deniz.csv',
             'session5_run4_Deniz.csv',
             'session5_run5_Deniz.csv',
             'session5_run6_Deniz.csv',
             'session5_run7_Deniz.csv',
             'session5_run8_Deniz.csv',
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
            'SessionSuper2w_run32_Deniz.csv',
            'SessionSuper2w_run1_Deniz.csv',
            'SessionSuper2w_run2_Deniz.csv',
            'SessionSuper2w_run3_Deniz.csv',
            'SessionSuper2w_run4_Deniz.csv',
            'SessionSuper2w_run5_Deniz.csv',
            'SessionSuper2w_run6_Deniz.csv',
            'SessionSuper2w_run7_Deniz.csv',
            'SessionSuper2w_run8_Deniz.csv',
            'SessionSuper2w_run9_Deniz.csv',
            'SessionSuper2w_run10_Deniz.csv',
            'SessionSuper2w_run11_Deniz.csv',
            'SessionSuper2w_run12_Deniz.csv',
            'SessionSuper2w_run13_Deniz.csv',
            'SessionSuper2w_run14_Deniz.csv',
            'SessionSuper2w_run15_Deniz.csv',
            'SessionSuper2w_run16_Deniz.csv',
            'SessionSuper2w_run17_Deniz.csv',
            'SessionSuper2w_run18_Deniz.csv',
            'SessionSuper2w_run19_Deniz.csv',
            'SessionSuper2w_run20_Deniz.csv',
            'SessionSuper2w_run21_Deniz.csv',
            'SessionSuper2w_run22_Deniz.csv',
            'SessionSuper2w_run23_Deniz.csv',
            'SessionSuper2w_run24_Deniz.csv',
            'SessionSuper2w_run25_Deniz.csv',
            'SessionSuper2w_run26_Deniz.csv',
            'SessionSuper2w_run27_Deniz.csv',
            'SessionSuper2w_run28_Deniz.csv',
            'SessionSuper2w_run29_Deniz.csv',
            'SessionSuper2w_run30_Deniz.csv',
            'SessionSuper2w_run31_Deniz.csv',
            'SessionSuper2w_run32_Deniz.csv',
            'SessionSuper3w_run1_Deniz.csv',
            'SessionSuper3w_run2_Deniz.csv',
            'SessionSuper3w_run3_Deniz.csv',
            'SessionSuper3w_run4_Deniz.csv',
            'SessionSuper3w_run5_Deniz.csv',
            'SessionSuper3w_run6_Deniz.csv',
            'SessionSuper3w_run7_Deniz.csv',
            'SessionSuper3w_run8_Deniz.csv',
            'SessionSuper3w_run9_Deniz.csv',
            'SessionSuper3w_run10_Deniz.csv',
            'SessionSuper3w_run11_Deniz.csv',
            'SessionSuper3w_run12_Deniz.csv',
            'SessionSuper3w_run13_Deniz.csv',
            'SessionSuper3w_run14_Deniz.csv',
            'SessionSuper3w_run15_Deniz.csv',
            'SessionSuper3w_run16_Deniz.csv',
            'SessionSuper3w_run17_Deniz.csv',
            'SessionSuper3w_run18_Deniz.csv',
            'SessionSuper3w_run19_Deniz.csv',
            'SessionSuper3w_run20_Deniz.csv',
            'SessionSuper3w_run21_Deniz.csv',
            'SessionSuper3w_run22_Deniz.csv',
            'SessionSuper3w_run23_Deniz.csv',
            'SessionSuper3w_run24_Deniz.csv',
            'SessionSuper3w_run25_Deniz.csv',
            'SessionSuper3w_run26_Deniz.csv',
            'SessionSuper3w_run27_Deniz.csv',
            'SessionSuper3w_run28_Deniz.csv',
            'SessionSuper3w_run29_Deniz.csv',
            'SessionSuper3w_run30_Deniz.csv',
            'SessionSuper3w_run31_Deniz.csv',
            'SessionSuper3w_run32_Deniz.csv',
            'SessionSuper4w_run1_Deniz.csv',
            'SessionSuper4w_run2_Deniz.csv',
            'SessionSuper4w_run3_Deniz.csv',
            'SessionSuper4w_run4_Deniz.csv',
            'SessionSuper4w_run5_Deniz.csv',
            'SessionSuper4w_run6_Deniz.csv',
            'SessionSuper4w_run7_Deniz.csv',
            'SessionSuper4w_run8_Deniz.csv',
            'SessionSuper4w_run9_Deniz.csv',
            'SessionSuper4w_run10_Deniz.csv',
            'SessionSuper4w_run11_Deniz.csv',
            'SessionSuper4w_run12_Deniz.csv',
            'SessionSuper4w_run13_Deniz.csv',
            'SessionSuper4w_run14_Deniz.csv',
            'SessionSuper4w_run15_Deniz.csv',
            'SessionSuper4w_run16_Deniz.csv',
            'SessionSuper4w_run17_Deniz.csv',
            'SessionSuper4w_run18_Deniz.csv',
            'SessionSuper4w_run19_Deniz.csv',
            'SessionSuper4w_run20_Deniz.csv',
            'SessionSuper4w_run21_Deniz.csv',
            'SessionSuper4w_run22_Deniz.csv',
            'SessionSuper4w_run23_Deniz.csv',
            'SessionSuper4w_run24_Deniz.csv',
            'SessionSuper4w_run25_Deniz.csv',
            'SessionSuper4w_run26_Deniz.csv',
            'SessionSuper4w_run27_Deniz.csv',
            'SessionSuper4w_run28_Deniz.csv',
            'SessionSuper4w_run29_Deniz.csv',
            'SessionSuper4w_run30_Deniz.csv',
            'SessionSuper4w_run31_Deniz.csv',
            'SessionSuper4w_run32_Deniz.csv',
            'SessionSuper5w_run1_Deniz.csv',
            'SessionSuper5w_run2_Deniz.csv',
            'SessionSuper5w_run3_Deniz.csv',
            'SessionSuper5w_run4_Deniz.csv',
            'SessionSuper5w_run5_Deniz.csv',
            'SessionSuper5w_run6_Deniz.csv',
            'SessionSuper5w_run7_Deniz.csv',
            'SessionSuper5w_run8_Deniz.csv',
            'SessionSuper5w_run9_Deniz.csv',
            'SessionSuper5w_run10_Deniz.csv',
            'SessionSuper5w_run11_Deniz.csv',
            'SessionSuper5w_run12_Deniz.csv',
            'SessionSuper5w_run13_Deniz.csv',
            'SessionSuper5w_run14_Deniz.csv',
            'SessionSuper5w_run15_Deniz.csv',
            'SessionSuper5w_run16_Deniz.csv',
            'SessionSuper5w_run17_Deniz.csv',
            'SessionSuper5w_run18_Deniz.csv',
            'SessionSuper5w_run19_Deniz.csv',
            'SessionSuper5w_run20_Deniz.csv',
            'SessionSuper5w_run21_Deniz.csv',
            'SessionSuper5w_run22_Deniz.csv',
            'SessionSuper5w_run23_Deniz.csv',
            'SessionSuper5w_run24_Deniz.csv',
            'SessionSuper5w_run25_Deniz.csv',
            'SessionSuper5w_run26_Deniz.csv',
            'SessionSuper5w_run27_Deniz.csv',
            'SessionSuper5w_run28_Deniz.csv',
            'SessionSuper5w_run29_Deniz.csv',
            'SessionSuper5w_run30_Deniz.csv',
            'SessionSuper5w_run31_Deniz.csv',
            'SessionSuper5w_run32_Deniz.csv',
            'SessionSuper6w_run1_Deniz.csv',
            'SessionSuper6w_run2_Deniz.csv',
            'SessionSuper6w_run3_Deniz.csv',
            'SessionSuper6w_run4_Deniz.csv',
            'SessionSuper6w_run5_Deniz.csv',
            'SessionSuper6w_run6_Deniz.csv',
            'SessionSuper6w_run7_Deniz.csv',
            'SessionSuper6w_run8_Deniz.csv',
            'SessionSuper6w_run9_Deniz.csv',
            'SessionSuper6w_run10_Deniz.csv',
            'SessionSuper6w_run11_Deniz.csv',
            'SessionSuper6w_run12_Deniz.csv',
            'SessionSuper6w_run13_Deniz.csv',
            'SessionSuper6w_run14_Deniz.csv',
            'SessionSuper6w_run15_Deniz.csv',
            'SessionSuper6w_run16_Deniz.csv',
            'SessionSuper6w_run17_Deniz.csv',
            'SessionSuper6w_run18_Deniz.csv',
            'SessionSuper6w_run19_Deniz.csv',
            'SessionSuper6w_run20_Deniz.csv',
            'SessionSuper6w_run21_Deniz.csv',
            'SessionSuper6w_run22_Deniz.csv',
            'SessionSuper6w_run23_Deniz.csv',
            'SessionSuper6w_run24_Deniz.csv',
            'SessionSuper6w_run25_Deniz.csv',
            'SessionSuper6w_run26_Deniz.csv',
            'SessionSuper6w_run27_Deniz.csv',
            'SessionSuper6w_run28_Deniz.csv',
            'SessionSuper6w_run29_Deniz.csv',
            'SessionSuper6w_run30_Deniz.csv',
            'SessionSuper6w_run31_Deniz.csv',
            'SessionSuper6w_run32_Deniz.csv'
             ]

def trim_multiple(num_channels):
    trimmed_files = np.ndarray((4*len(filenames), num_channels,1000))
    counter = 0
    for file in filenames:
        trimmed_files[counter:counter+4]= trim_start_end(file, num_channels)
        counter+=4
    #Plot the trimmed data
    plt.figure(1)
    plt.plot(trimmed_files[0,0,:])
    plt.show()
    plt.plot(trimmed_files[1,0,:])
    plt.show()
    plt.plot(trimmed_files[2,0,:])
    plt.show()
    plt.plot(trimmed_files[3,0,:])
    plt.show()
    plt.plot(trimmed_files[4,0,:])
    plt.show()
    plt.plot(trimmed_files[5,0,:])
    plt.show()
    plt.plot(trimmed_files[6,0,:])
    plt.show()
    plt.plot(trimmed_files[7,0,:])
    plt.show()
    trimmed_files_filtered = bandpass_multiEEG(trimmed_files,250)
    trimmed_files_filtered = np.asarray(trimmed_files_filtered)
    #Plot the filtered data
    plt.figure(1)
    plt.plot(trimmed_files[0,0,:])
    plt.plot(trimmed_files_filtered[0,0,:])
    plt.show()
    plt.plot(trimmed_files[0,1,:])
    plt.plot(trimmed_files_filtered[1,0,:])
    plt.show()
    plt.plot(trimmed_files[0,2,:])
    plt.plot(trimmed_files_filtered[2,0,:])
    plt.show()
    plt.plot(trimmed_files[0,3,:])
    plt.plot(trimmed_files_filtered[3,0,:])
    plt.show()

    for trial in range(0, trimmed_files_filtered.shape[0]):
        for channel in range(0, trimmed_files_filtered.shape[1]):
            sum = np.sum(trimmed_files_filtered[trial,channel,:])
            ave = sum / (trimmed_files_filtered.shape[2])
            trimmed_files_filtered[trial,channel,:] = np.asarray(trimmed_files_filtered[trial,channel,:] - ave)
            max = np.argmax(trimmed_files_filtered[trial,channel,:])
            max = trimmed_files_filtered[trial,channel,max]
            trimmed_files_filtered[trial,channel,:] = trimmed_files_filtered[trial,channel,:] / max                     
    
    ##Plot the normalized data
    # plt.figure(1)
    # #plt.plot(trimmed_files[0,0,:])
    # plt.plot(trimmed_files_filtered[0,0,:])
    # plt.show()
    # #plt.plot(trimmed_files[0,1,:])
    # plt.plot(trimmed_files_filtered[1,0,:])
    # plt.show()
    # #plt.plot(trimmed_files[0,2,:])
    # plt.plot(trimmed_files_filtered[2,0,:])
    # plt.show()
    # #plt.plot(trimmed_files[0,3,:])
    # plt.plot(trimmed_files_filtered[3,0,:])
    # #plt.plot(trimmed_files[0,0,:])
    # plt.show()
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

