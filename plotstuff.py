import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

#getting data
df=pd.read_csv("example_data_1_PHYS_433_533.csv")
print(df)

freq=df['f_res']
power_dbm=df['max_power_dBm']

#plotting data
plt.title('power vs freq')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Power (dBm)')
plt.scatter(freq,power_dbm,color='red')
plt.show()


#change from dBm to mW, then plot
power_mW=10**(np.array(power_dbm/10))
print(power_mW[:5])

plt.title('power vs freq')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Power (mW)')
plt.scatter(freq,power_mW,color='red')
plt.show()

mask=freq>4000
freq_masked=freq[mask]
power_mW_masked=power_mW[mask]

plt.title('power vs freq')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Power (mW)')
plt.scatter(freq_masked,power_mW_masked,color='red')
plt.show()

def linfit(x,m,b):
    return m*x + b

popt,pcov = curve_fit(linfit,freq_masked,power_mW_masked, p0=[-1,2])
print(popt)
print(pcov)

plt.title('power vs freq')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Power (mW)')
plt.scatter(freq_masked,power_mW_masked)
plt.plot(freq_masked,linfit(freq_masked,popt[0],popt[1]),color='orange')
plt.show()