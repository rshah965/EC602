# Author Rishab Shah rishah@bu.edu

import scipy.io.wavfile as wavfile
import numpy as np

def dialer(file_name,frame_rate,phone,tone_time):
    a=file_name
    f=frame_rate
    p=phone
    t=tone_time
    
    f1={'1':697,'2':697,'3':697,'4':770,'5':770,'6':770,'7':852,'8':852,'9':852,'0':941}
    f2={'1':1209,'2':1336,'3':1477,'4':1209,'5':1336,'6':1477,'7':1209,'8':1336,'9':1477,'0':1336}
    data=np.array([])
    
    for i in p:
        k=f1[i]
        l=f2[i]

        npoints=f*t
        x=np.linspace(0,npoints/f,npoints)
        tmp_data=np.cos(2*np.pi*k*x)+np.cos(2*np.pi*l*x)
        data=np.concatenate((data,tmp_data))
        
    wavfile.write(a,f,data)

#dialer('abc.wav',44100,'9309383',0.1)