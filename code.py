import scipy.io as sio
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

healthy_signal = sio.loadmat('97_Normal_0.mat')['X097_DE_time'].flatten()[:4096]
broken_signal = sio.loadmat('OR007_6_1_136.mat')['X136_DE_time'].flatten()[:4096]

pitches = np.fft.fftfreq(4096, d=1/12000)[:2048]
healthy_volume = np.abs(np.fft.fft(healthy_signal))[:2048]
broken_volume = np.abs(np.fft.fft(broken_signal))[:2048]

def get_metrics(signal):
    rms = np.sqrt(np.mean(signal**2))
    p2p = np.max(signal) - np.min(signal)
    kurt = stats.kurtosis(signal, fisher=False)
    return rms, p2p, kurt

healthy_rms, healthy_p2p, healthy_kurt = get_metrics(healthy_signal)
broken_rms, broken_p2p, broken_kurt = get_metrics(broken_signal)

def spotify_wrapped(name, rms, p2p, kurt):
    print(f"\n{name.upper()}'S SPOTIFY WRAPPED!")

    print(f"Kurtosis: {kurt:.2f}")
    if kurt < 3.5:
        print("Verdict: Smooth Jazz. No impacts detected.")
    else:
        print("Verdict: Heavy Metal! Huge spikes detected!")


    print(f"RMS: {rms:.3f}")
    if rms < 0.1:
        print("Verdict: Acoustic. Quiet background noise.")
    else:
        print("Verdict: EDM Bass Drop. Way too much energy.")

 
    print(f"Peak-to-Peak: {p2p:.3f}")
    if p2p < 0.5:
        print("Verdict: Chill Lo-Fi. Stable swings.")
    else:
        print("Verdict: Rollercoaster. Violent vibrations.")

spotify_wrapped("Healthy Machine", healthy_rms, healthy_p2p, healthy_kurt)
spotify_wrapped("Broken Machine", broken_rms, broken_p2p, broken_kurt)


plt.figure(figsize=(10, 3))

plt.subplot(1, 2, 1)
plt.plot(healthy_signal)
plt.title("Healthy Raw Wave")

plt.subplot(1, 2, 2)
plt.plot(broken_signal)
plt.title("Broken Raw Wave")

plt.show()


plt.figure(figsize=(10, 3))

plt.subplot(1, 2, 1)
plt.plot(pitches, healthy_volume)
plt.title("Healthy FFT Equalizer")
plt.ylim(0, 300) 

plt.subplot(1, 2, 2)
plt.plot(pitches, broken_volume)
plt.title("Broken FFT Equalizer")
plt.ylim(0, 300)

plt.show()