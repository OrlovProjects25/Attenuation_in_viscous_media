from Spectro0.py import spectrogram
from main_body.py import out, sr

spectrogram(out, sr)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar(format="%+2.0f dB")
plt.show()
