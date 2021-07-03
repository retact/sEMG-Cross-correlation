import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

######## MDecompose the data #######
emglist=['emg1','emg2','emg3','emg4','emg5','emg6','emg7','emg8']
device1=[]
device1fig=[8]
device2=[]
device2fig=[8]
q=0

####### Device1 #######
data = pd.read_csv('data/device1.csv',encoding = 'UTF8')
df = pd.DataFrame(data)
del df['moving']
del df['characteristic_num']

plt.figure(figsize=(30,4))
plt.plot(df[emglist])
plt.xlabel('Number of data',fontsize=15)
plt.ylabel('EMG [-128-127]',fontsize=15)
plt.title("Myo raw-EMG device1",fontsize=25)
plt.show()

fig = plt.figure(figsize=(25,15))
for i in emglist:
  device1.append(df[i])#list
  plt.subplot(4,2,q+1)
  plt.plot(df[i])
  plt.subplots_adjust(wspace=0.2, hspace=0.6)
  plt.xlabel('Number of data',fontsize=10)
  plt.ylabel('EMG [-128-127]',fontsize=10)
  plt.title('Myo raw-EMG device1({})'.format(i),fontsize=15)
  q+=1
plt.show()

####### Device2 #######

data = pd.read_csv('data/device2.csv',encoding = 'UTF8')
df2 = pd.DataFrame(data)
del df2['moving']
del df2['characteristic_num']

plt.figure(figsize=(30,4))
plt.plot(df2[emglist])
plt.xlabel('Number of data',fontsize=15)
plt.ylabel('EMG [-128-127]',fontsize=15)
plt.title("Myo raw-EMG device2",fontsize=25)
plt.show()

fig = plt.figure(figsize=(25,15))
q=0
for i in emglist:
  device2.append(df2[i])#list
  plt.subplot(4,2,q+1)
  plt.plot(df2[i])
  plt.subplots_adjust(wspace=0.2, hspace=0.6)
  plt.xlabel('Number of data',fontsize=10)
  plt.ylabel('EMG [-128-127]',fontsize=10)
  plt.title('Myo raw-EMG device2({})'.format(i),fontsize=15)
  q+=1
plt.show()


######### Trimming ##########

length=1200

####### device1_emg1 #######
dev1_start=900
dev1_emg1=device1[0][dev1_start:length+dev1_start]
# Plotting
plt.figure(figsize=(15,6))
plt.plot(dev1_emg1)
plt.xlabel('Number of data',fontsize=15)
plt.ylabel('EMG [-128-127](mV)',fontsize=15)
plt.title("Myo raw-EMG device1 (emg1)",fontsize=25)
plt.show()

####### device2_emg1 #######
dev2_start=230
dev2_emg1=device2[0][dev2_start:length+dev2_start]
# Plotting
plt.figure(figsize=(15,6))
plt.plot(dev2_emg1,color='#ff7f00')
plt.xlabel('Number of data',fontsize=15)
plt.ylabel('EMG [-128-127](mV)',fontsize=15)
plt.title("Myo raw-EMG device2 (emg1)",fontsize=25)
plt.show()

####### device1and2_emg1 #######
signals_emg1=df1 = pd.DataFrame({'dev1':dev1_emg1, 'dev2':dev2_emg1})
# Plotting
plt.style.use('dark_background')
plt.figure(figsize=(15,4))
plt.plot(signals_emg1)
plt.xlabel('Number of data',fontsize=15)
plt.ylabel('EMG [-128-127](mV)',fontsize=15)
plt.title("Myo raw-EMG signals (emg1)",fontsize=25)
plt.show()
signals_emg1

########　Cross-correlation function　　for Raw data #######
#　Standardization
dev1_emg1=(dev1_emg1-np.mean(dev1_emg1))/np.std(dev1_emg1)
dev2_emg1=(dev2_emg1-np.mean(dev2_emg1))/np.std(dev2_emg1)

# Cross-correlation function
corr=np.correlate(dev1_emg1, dev2_emg1,"full")
estimated_delay = corr.argmax() - (len(dev2_emg1) - 1)
print("estimated delay is " + str(estimated_delay))

# Plotting
plt.figure(figsize=(15,8))

plt.subplot(2, 1, 1)
plt.plot(np.arange(len(dev1_emg1)), dev1_emg1)
plt.plot(np.arange(len(dev2_emg1)) + estimated_delay, dev2_emg1)
plt.xlabel('Number of data',fontsize=15)
plt.ylabel('EMG',fontsize=15)
plt.title("Myo raw-EMG signals (emg1)",fontsize=25)
plt.xlim([0, len(dev1_emg1)])

plt.subplot(2, 1, 2)
plt.plot(np.arange(len(corr)) - len(dev2_emg1) + 1, corr, color="r")
plt.xlabel('Delay',fontsize=15)
plt.ylabel("Cross-correlation",fontsize=15)
plt.xlim([0, len(dev1_emg1)])

plt.show()
