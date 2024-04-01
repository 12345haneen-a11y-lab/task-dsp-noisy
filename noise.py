import soundfile as sf
import sounddevice as sd
import librosa
import numpy as np

import matplotlib.pyplot as plt
y, sr = librosa.load('audio1.wav')
d = librosa.stft(y)
magnitude = np.abs(d)
noise_level = np.mean(magnitude[:1000])
cleaned_magnitude = np.maximum(magnitude - noise_level , 0)
cleaned_d = cleaned_magnitude * np.exp(1j * np.angle(d))
cleaned_audio = librosa.istft(cleaned_d)
sf.write('cleaned_audio.wav', cleaned_audio , sr)
r , st = sf.read('cleaned_audio.wav')
plt.subplot(2,1,1)
plt.plot(y)
plt.title("original signal")
plt.subplot(2,1,2)
plt.plot(r)
plt.title("enhanced signal")
plt.show()
