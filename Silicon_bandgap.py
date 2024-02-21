import matplotlib.pyplot as plt
import numpy as np 
import os
from scipy.stats import linregress

data = np.loadtxt('Silicon_mirrors(UDS).TXT',skiprows=50)

def Plot(data):
    x = data[:, 0]
    #print(x[0])
    y = data[:, 1]
    #print(y[0])
    return(x,y)


plt.figure(6)                                                       #Plotting Transmission data
plt.plot(Plot(data)[0],Plot(data)[1], '.',markersize=2.5)
plt.title('Silicon wafer, transmission spectrum')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission %")
plt.ylim(-2,100)
plt.show()


h = 6.63*(10**-34)   #J.s                          #Define Planck's constant
n = 2                                          # 2 for indirect band gap transitions
L = 1.3*10**-4        #cm                           # Thickness of sample (1um) need to write in cm
T = []                #Dimensionless
hf = []               #eV
alpha = []            #1\cm
c = 299792458         #m/s
q = 1.6*(10**-19)       #C

for i in range(0,len(Plot(data)[0]),1 ):        #range(0,len(Plot(data)[0]),1 )
    f = c/((Plot(data)[0][i])*(10**-9))         #Calculating frequencies from wavelength
    f = f/q                                    #Multiplied by charge on electron to make 
                                               #hf in terms of eV
    hf = np.append(h* f,hf)                    #Create range of hf for x axis
    T = np.append((Plot(data)[1][i])/100,T)    #Defining an array of Transsmiscene 
                                               #In range 0-1. 

alpha = 1/L * np.log(1/T)                      # Absorption coefficient in terms of thickness (t)
                                               # Transmission (T)= (I/I0)
ahv = (alpha*hf)**(n)

P = linregress(hf,ahv)

#Lower_lim= 3.0
#Upper_lim= 4.0
#hf1= []
#for g in range(0,len(hf),1):
    #if hf[g] < Lower_lim:
   #     hf1 = np.append(hf1,0)
   # elif hf[g] > Upper_lim:
    #    hf1 = np.append(hf1,0)
   # else:
        #hf1 = np.append(hf1,hf[g])

#print(hf1[162],hf1[368])
#res_index = 0
#for item in hf1[-1::-1]:
    #if item == 0:
    #    res_index += 1
   # else:
    #    break
#print(len(hf1) - res_index)


#print(hf[0])
plt.figure(1)
plt.plot(hf,ahv)
##plt.plot(hf,P[0]*hf + P[1])
plt.xlabel('hf(eV)')
plt.ylabel('(alpha * hf)^2 (eV/cm)')
#plt.xlim(1.1*10**-37,1.4*10**-37)
plt.show

plt.figure(2)
plt.plot(hf,alpha)
plt.xlabel('hf(eV)')
plt.ylabel('alpha(cm^-1)')