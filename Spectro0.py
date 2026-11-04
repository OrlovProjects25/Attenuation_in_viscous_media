


def spectrogram(y, sr):
  S = librosa.stft(y)
  S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)
  librosa.display.specshow(
      S_db,
      sr=sr,
      x_axis="time",
      y_axis="linear"
  )

spectrogram(y, sr)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar(format="%+2.0f dB")
plt.show()
