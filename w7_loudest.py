# Author Rishab Shah rishah@bu.edu

import numpy as np

def loudest_band(music,frame_rate,bandwidth):
    m=np.fft.fft(music)
    
    nframes=len(music)
    
    tmp_max=0
    
    bandwidth_val=int(bandwidth/(frame_rate/nframes))
    
    high=bandwidth_val
    
    #finding low and high
    m_square=abs(m)*abs(m)
    
    for i in range(0,bandwidth_val):
        tmp_max+=m_square[i]

    MAX=tmp_max
    
    for i in range(bandwidth_val,nframes//2):
        tmp_max=tmp_max-m_square[i-bandwidth_val]+m_square[i]
        if tmp_max>MAX:
            MAX=tmp_max
            high=i+1
            
    low=high-bandwidth_val
    
    #finding loudest and ifft
    X=np.zeros((nframes,))
    
    for n in range(0,bandwidth_val):
        X[low+n]=1
        X[n+nframes-high]=1

    loudest=np.fft.ifft(X*m)
    
    high=high/(nframes/frame_rate)
    
    low=high-bandwidth
    
    return(low,high,loudest)