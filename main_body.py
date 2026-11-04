import math
import random
import datetime as dt
import soundfile as sf
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import gdown
from scipy.io import wavfile
from IPython.display import Audio

filename = "White_noise.wav"
sr, y = wavfile.read(filename)
dur = librosa.get_duration(y = y, sr = sr)
t = np.arange(0, dur, 1 / sr)
if (len(y.shape) > 1):
  y = y.mean(axis=1) #stereo -> mono

max_ = np.max(np.abs(y))
y_norm = y / np.max(np.abs(y))

x = 5.0 #distance
c = 1020
Nu0 = 1000 #dynamic
Volumer0 = 1500
density = 970
f_rel_Nu = 4500 #relaxation frequency in dynamic viscosity for current f
f_rel_Vol = 6000 #relax. freq. in volume viscosity for cur. f
display(Audio(y, rate=sr))

delta_t = x / c

extra = int(delta_t * sr)
y_new = np.pad(y_norm, (0, extra), 'constant')

spectrum = np.fft.rfft(y_new)
ampl = 2/len(y_new) * np.abs(spectrum)
freq = np.fft.rfftfreq(len(y_new), d=1/sr)


Nu = Nu0 / (1 + (freq / f_rel_Nu) ** 2)
Volumer = Volumer0 / (1 + (freq / f_rel_Vol) ** 2)
gamma = (Nu + 4/3 * Volumer) / (2 * density)

omega = 2 * np.pi * freq


mu = gamma * omega / (c * c)
con = 1 / (1 + 4 * mu * mu) ** 0.5
k = (omega / (c * (2 ** 0.5))) * ((con + con * con) ** 0.5)
alpha = (omega / (c * (2 ** 0.5))) * ((con - con * con) ** 0.5)
vel = omega[1:] / k[1:]

shift = np.exp(-1j * k * x)
spectrum *= shift
spectrum *= np.exp(-alpha * x)
out = np.fft.irfft(spectrum)
out = out / np.max(np.abs(out)) * max_
out1 = np.int16(out)

display(Audio(out1, rate=sr))
wavfile.write("Changed_White_Noise.wav", sr, out1)
