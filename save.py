import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation 
import soundfile as sf

fs = 44100
duration = 1

t=1
tempo=np.linspace(0, t, fs*t)
x = tempo

audio = sd.rec(int(duration*fs), fs, channels=1)
sd.wait()

y = audio[:,0]

sf.write('somD.wav', y, fs)
