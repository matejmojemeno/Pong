"""numpy som si importol :)"""
import numpy as np

x = float(input())
y = float(input())
    
print(np.arccos(x/np.sqrt(x**2 + y**2))*180/np.pi)