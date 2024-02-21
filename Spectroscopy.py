import matplotlib.pyplot as plt
import numpy as np 
import os 

cwd = os.getcwd()
print(cwd)
yes = os.listdir(cwd)
print(yes)

data0 = np.loadtxt('Red_filter_air(UDS).TXT',skiprows=50)#
data1 = np.loadtxt('Red_filter_silica(UDS).TXT',skiprows=50)
data2= np.loadtxt('Aaron_filter_2_silica(UDS).TXT',skiprows=50)
data3 = np.loadtxt('Air(UDS).TXT',skiprows=50)
data4 = np.loadtxt('Jiaqi_filter_1_silica_attempt2(UDS).TXT',skiprows=50)
data5 = np.loadtxt('Silicon_mirrors(UDS).TXT',skiprows=50)


def Plot(data):
    x = data[:, 0]
    #print(x[0])
    y = data[:, 1]
    #print(y[0])
    return(x,y)


plt.figure(1)
plt.plot(Plot(data0)[0], Plot(data0)[1], '.',markersize=2.5)
plt.title('Red_filter_air')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission %")
plt.ylim(-2,100)
plt.show()

plt.figure(2)
plt.plot(Plot(data1)[0],Plot(data1)[1], '.',markersize=2.5)
plt.title('Red_filter_silica')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission %")
plt.ylim(-2,100)
plt.show()

plt.figure(3)
plt.plot(Plot(data2)[0],Plot(data2)[1], '.',markersize=2.5)
plt.title('Aaron_filter_2_silica')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission %")
plt.ylim(-2,100)
plt.show()

plt.figure(4)
plt.title('Air')
plt.plot(Plot(data3)[0],Plot(data3)[1], '.',markersize=2.5)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission %")
plt.ylim(-2,110)
plt.show()

plt.figure(5)
plt.plot(Plot(data4)[0],Plot(data4)[1], '.',markersize=2.5)
plt.title('Jiaqi_filter_1_silica_attempt2')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission %")
plt.ylim(-2,100)
plt.show()

plt.figure(6)
plt.plot(Plot(data5)[0],Plot(data5)[1], '.',markersize=2.5)
plt.title('Silicon wafer')
plt.ylim(-2,100)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission %")
plt.show()

plt.figure(7)
plt.plot(Plot(data2)[0],Plot(data2)[1], '.', label = 'Aaron',markersize=2.5)
plt.plot(Plot(data4)[0],Plot(data4)[1], '.', label = 'Jiaqi',markersize=2.5)
plt.title('Aaron vs Jiaqi')
plt.legend(loc='best')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission %")
plt.ylim(-2,100)
plt.show()